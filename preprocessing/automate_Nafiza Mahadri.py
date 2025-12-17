import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import os
import argparse
from datetime import datetime


def load_data(filepath: str) -> pd.DataFrame:

    print(f" Memuat data dari: {filepath}")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File tidak ditemukan: {filepath}")
    
    df = pd.read_csv(filepath)
    print(f" Data berhasil dimuat. Shape: {df.shape}")
    
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    print("\n Membersihkan data")
    
    initial_rows = len(df)
    
    # Menghapus duplikat
    df = df.drop_duplicates()
    after_dedup = len(df)
    print(f"  - Duplikat dihapus: {initial_rows - after_dedup} baris")
    
    # Menghapus missing values (jika ada)
    df = df.dropna()
    after_na = len(df)
    print(f"  - Missing values dihapus: {after_dedup - after_na} baris")
    
    print(f" Data bersih. Shape: {df.shape}")
    
    return df


def feature_engineering(df: pd.DataFrame, current_year: int = 2024) -> pd.DataFrame:

    print("\n Melakukan feature engineering")
    
    # Menambahkan fitur car_age
    df['car_age'] = current_year - df['year']
    print(f"  - Fitur 'car_age' ditambahkan")
    
    # Menghapus kolom yang tidak diperlukan
    columns_to_drop = ['name', 'year']
    df = df.drop(columns=columns_to_drop, errors='ignore')
    print(f"  - Kolom dihapus: {columns_to_drop}")
    
    print(f" Feature engineering selesai. Kolom: {list(df.columns)}")
    
    return df


def encode_features(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:

    print("\n Melakukan encoding fitur kategorikal")
    
    categorical_cols = ['fuel', 'seller_type', 'transmission', 'owner']
    encoders = {}
    
    for col in categorical_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            encoders[col] = le
            print(f"  - {col}: {len(le.classes_)} kategori di-encode")
    
    print(f" Encoding selesai.")
    
    return df, encoders


def normalize_features(df: pd.DataFrame, target_col: str = 'selling_price') -> tuple[pd.DataFrame, StandardScaler]:

    print("\n Melakukan normalisasi fitur numerik")
    
    # Kolom yang akan dinormalisasi
    cols_to_scale = ['km_driven', 'car_age']
    cols_to_scale = [col for col in cols_to_scale if col in df.columns]
    
    scaler = StandardScaler()
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    
    print(f"  - Kolom ternormalisasi: {cols_to_scale}")
    print(f" Normalisasi selesai.")
    
    return df, scaler


def split_data(df: pd.DataFrame, target_col: str = 'selling_price', 
               test_size: float = 0.2, random_state: int = 42) -> dict:

    print("\n Membagi data (train-test split)")
    
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    print(f"  - Training set: {len(X_train)} samples ({(1-test_size)*100:.0f}%)")
    print(f"  - Testing set: {len(X_test)} samples ({test_size*100:.0f}%)")
    
    return {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test
    }


def preprocess_data(input_path: str, output_path: str) -> pd.DataFrame:

    
    print("AUTOMATED DATA PREPROCESSING")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    
    # Step 1: Load data
    df = load_data(input_path)
    
    # Step 2: Clean data
    df = clean_data(df)
    
    # Step 3: Feature engineering
    df = feature_engineering(df)
    
    # Step 4: Encode categorical features
    df, encoders = encode_features(df)
    
    # Step 5: Normalize numerical features
    df, scaler = normalize_features(df)
    
    # Step 6: Save processed data
    print("\n Menyimpan data terproses")
    
    # Membuat direktori output jika belum ada
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"  - Direktori dibuat: {output_dir}")
    
    df.to_csv(output_path, index=False)
    print(f"  - Data disimpan ke: {output_path}")
   
    print("PREPROCESSING SELESAI!")
    
    print(f"Output shape: {df.shape}")
    print(f"Kolom: {list(df.columns)}")
    
    return df


def main():

    parser = argparse.ArgumentParser(
        description='Automated Data Preprocessing for Used Car Price Prediction'
    )
    parser.add_argument(
        '--input', 
        type=str, 
        default='D:\Dicoding\SMSML_Nafiza Mahadri W\Eksperimen_SML_Nafiza Mahadri W\dataset_raw\CAR DETAILS FROM CAR DEKHO.csv',
        help='Path ke file CSV mentah'
    )
    parser.add_argument(
        '--output', 
        type=str, 
        default='D:\Dicoding\SMSML_Nafiza Mahadri W\Eksperimen_SML_Nafiza Mahadri W\dataset_preprocessing\car_data_processed2.csv',
        help='Path untuk menyimpan hasil preprocessing'
    )
    
    args = parser.parse_args()
    
    # Jalankan preprocessing
    df_processed = preprocess_data(args.input, args.output)
    
    return df_processed


if __name__ == "__main__":
    main()
