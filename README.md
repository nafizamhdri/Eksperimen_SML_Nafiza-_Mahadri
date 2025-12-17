# MLOps Project: Used Car Price Prediction

Proyek ini bertujuan untuk membangun pipeline Machine Learning end-to-end untuk memprediksi harga mobil bekas. Proyek ini menerapkan praktik MLOps modern termasuk **Data Version Control (DVC)**, **Automation Script**, dan **CI/CD (GitHub Actions)**.

## 📂 Struktur Project

```
Eksperimen_SML_Nafiza-_Mahadri/
├── .github/workflows/       # CI/CD Pipelines
├── dataset_raw/             # Dataset mentah (Tracked by DVC)
├── dataset_preprocessing/   # Dataset hasil proses (Tracked by DVC)
├── preprocessing/           # Script preprocessing
│   └── automate_Nafiza Mahadri.py
├── requirements.txt         # Dependencies project
└── README.md                # Dokumentasi ini
```

## 🚀 Fitur Utama

1.  **Automated Preprocessing**: Script Python untuk membersihkan data, feature engineering, dan normalisasi secara otomatis.
2.  **Data Version Control**: Menggunakan DVC untuk melacak perubahan dataset raw dan processed.
3.  **CI/CD Pipeline**: GitHub Actions yang otomatis menjalankan preprocessing setiap ada perubahan code, memastikan pipeline selalu valid dan menghasilkan artifact data terbaru.

## 🛠️ Cara Menjalankan (Local)

1.  **Clone Repository**
    ```bash
    git clone https://github.com/nafizamhdri/Eksperimen_SML_Nafiza-_Mahadri.git
    cd Eksperimen_SML_Nafiza-_Mahadri
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Pull Data (DVC)**
    ```bash
    dvc pull
    ```

4.  **Jalankan Preprocessing**
    ```bash
    python "preprocessing/automate_Nafiza Mahadri.py"
    ```
    Hasilnya akan tersimpan di `dataset_preprocessing/car_data_processed2.csv`.

## 🤖 GitHub Actions

Pipeline CI/CD dikonfigurasi di `.github/workflows/preprocessing.yml`.
Setiap kali ada **Push** ke branch master:
1.  Environment Python disiapkan.
2.  Dependencies diinstall.
3.  Script preprocessing dijalankan.
4.  Dataset hasil proses di-upload sebagai **Artifact**.

---
**Author:** Nafiza Mahadri
**Dataset:** CAR DETAILS FROM CAR DEKHO (Kaggle)
