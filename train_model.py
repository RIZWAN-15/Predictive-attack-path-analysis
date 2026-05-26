print("Program Started")

import pandas as pd
print("Pandas Imported")

import numpy as np
print("NumPy Imported")

import os
import time
import joblib
import glob
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA_FOLDER = r"C:\s4\machine learning\projects\ML_project\data set 2.0\CSV'S"

MODEL_FILENAME = "attack_detection_model.pkl"

ROWS_PER_FILE = 10000

FEATURES = [
    'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
    'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Flow IAT Mean',
    'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Total', 'Bwd IAT Total',
    'Packet Length Mean', 'ACK Flag Count', 'PSH Flag Count', 'SYN Flag Count'
]

def clean_column_names(df):
    df.columns = df.columns.str.strip()
    return df

def load_data():

    print("=" * 60)
    print("LOADING NETWORK DATA")
    print("=" * 60)

    print(f"Searching in: {DATA_FOLDER}")

    csv_files = glob.glob(
        os.path.join(DATA_FOLDER, "**", "*.csv"),
        recursive=True
    )

    if len(csv_files) == 0:
        csv_files = glob.glob(
            os.path.join(DATA_FOLDER, "**", "*.CSV"),
            recursive=True
        )

    print(f"Found {len(csv_files)} CSV files")

    if len(csv_files) == 0:
        print("\nNo CSV files found!")
        return None

    all_data = []

    for file_path in csv_files:

        file_name = os.path.basename(file_path)

        print(f"\nProcessing: {file_name}")

        try:

            df = pd.read_csv(file_path, nrows=ROWS_PER_FILE)

            df = clean_column_names(df)

            print(f"  Rows: {len(df)}")
            print(f"  Columns: {len(df.columns)}")

            label_col = None

            for col in df.columns:
                if col.lower() == 'label':
                    label_col = col
                    break

            if label_col is None:
                print(f"  Warning: No 'Label' column found")
                continue

            df.rename(columns={label_col: 'Label'}, inplace=True)

            existing_features = []

            for feature in FEATURES:
                if feature in df.columns:
                    existing_features.append(feature)

            if len(existing_features) < 5:
                print(f"  Warning: Only {len(existing_features)} features found")
                continue

            columns_to_keep = existing_features + ['Label']

            df = df[columns_to_keep]

            all_data.append(df)

            print(f"  Success! Using {len(existing_features)} features")
            print(f"  Unique labels: {df['Label'].unique()}")

        except Exception as e:

            print(f"  Error: {e}")
            continue

    if not all_data:
        print("\nNo valid data loaded!")
        return None

    combined = pd.concat(all_data, ignore_index=True)

    print(f"\nTotal data loaded: {len(combined)} rows")

    return combined

def clean_data(df):

    print("\n" + "=" * 60)
    print("CLEANING DATA")
    print("=" * 60)

    original = len(df)

    print(f"Before cleaning: {original} rows")

    for col in df.columns:

        if col != 'Label':
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.replace([np.inf, -np.inf], np.nan)

    df = df.dropna()

    print(f"After cleaning: {len(df)} rows")
    print(f"Removed: {original - len(df)} rows")

    return df

def prepare_data(df):

    print("\n" + "=" * 60)
    print("PREPARING DATA")
    print("=" * 60)

    print("\nLabel distribution:")

    label_counts = df['Label'].value_counts()

    for label, count in label_counts.items():

        print(f"  {label}: {count} ({count / len(df) * 100:.1f}%)")

    X = df.drop('Label', axis=1)

    y = df['Label']

    le = LabelEncoder()

    y_encoded = le.fit_transform(y)

    print(f"\nEncoded classes:")

    for i, name in enumerate(le.classes_):

        print(f"  {i}: {name}")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=0.2,
        random_state=42,
        stratify=y_encoded
    )

    print(f"\nSplit data:")
    print(f"  Training: {len(X_train)} samples")
    print(f"  Testing: {len(X_test)} samples")

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    print(f"  Features scaled: {X.shape[1]} features")

    return (
        X_train_scaled,
        X_test_scaled,
        y_train,
        y_test,
        scaler,
        le,
        X.columns.tolist()
    )

def train_model(X_train, y_train):

    print("\n" + "=" * 60)
    print("TRAINING MODEL")
    print("=" * 60)

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1
    )

    print("Training Random Forest...")

    start = time.time()

    model.fit(X_train, y_train)

    train_time = time.time() - start

    print(f"Training completed in {train_time:.2f} seconds")

    return model, train_time

def evaluate_model(model, X_test, y_test, le):

    print("\n" + "=" * 60)
    print("EVALUATING MODEL")
    print("=" * 60)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nOverall Accuracy: {accuracy * 100:.2f}%")

    print("\nClassification Report:")

    unique_classes = np.unique(y_test)

    class_names = le.classes_[unique_classes]

    print(
        classification_report(
            y_test,
            y_pred,
            labels=unique_classes,
            target_names=class_names
        )
    )

    return accuracy

def save_model(model, scaler, le, features, accuracy):

    print("\n" + "=" * 60)
    print("SAVING MODEL")
    print("=" * 60)

    package = {
        'model': model,
        'scaler': scaler,
        'label_encoder': le,
        'feature_names': features,
        'accuracy': accuracy,
        'trained_date': time.strftime("%Y-%m-%d %H:%M:%S")
    }

    joblib.dump(package, MODEL_FILENAME)

    print(f"Model saved to: {MODEL_FILENAME}")

    print(
        f"File size: {os.path.getsize(MODEL_FILENAME) / 1024:.1f} KB"
    )

def main():

    print("\n" + "=" * 60)
    print("NETWORK ATTACK DETECTION SYSTEM")
    print("CIC-2017 Dataset Training")
    print("=" * 60)

    data = load_data()

    if data is None:
        print("\nERROR: Could not load data!")
        return

    data = clean_data(data)

    if len(data) == 0:
        print("No data after cleaning!")
        return

    (
        X_train,
        X_test,
        y_train,
        y_test,
        scaler,
        le,
        features
    ) = prepare_data(data)

    model, train_time = train_model(X_train, y_train)

    accuracy = evaluate_model(model, X_test, y_test, le)

    save_model(model, scaler, le, features, accuracy)

    print("\n" + "=" * 60)
    print("TRAINING COMPLETE!")
    print(f"Model saved: {MODEL_FILENAME}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("=" * 60)

if __name__ == "__main__":
    main()