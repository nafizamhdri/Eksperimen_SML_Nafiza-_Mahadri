# Used Car Price Prediction - MLOps Project

## Dataset: CarDekho Used Car Dataset

Proyek ini merupakan implementasi sistem Machine Learning end-to-end untuk prediksi harga mobil bekas.

## Struktur Folder

```
Eksperimen_SML_Nafiza Mahadri W/
├── .github/
│   └── workflows/
│       └── preprocessing.yml
├── namadataset_raw/
│   └── car_data.csv
├── preprocessing/
│   ├── Eksperimen_MSML_Nafiza_Mahadri.ipynb
│   └── automate_Nafiza Mahadri.py
├── namadataset_preprocessing/
│   └── (output dari preprocessing)
├── requirements.txt
└── README.md
```

## Cara Penggunaan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Preprocessing Manual
Buka dan jalankan notebook `preprocessing/Eksperimen_MSML_Nafiza_Mahadri.ipynb`

### 3. Jalankan Preprocessing Otomatis
```bash
python preprocessing/automate_Nafiza\ Mahadri.py
```

## Dataset Features

| Feature | Type | Description |
|---------|------|-------------|
| name | String | Nama model mobil |
| year | Integer | Tahun pembuatan |
| selling_price | Integer | Harga jual (target) |
| km_driven | Integer | Jarak tempuh (km) |
| fuel | Categorical | Petrol/Diesel/CNG/LPG |
| seller_type | Categorical | Individual/Dealer/Trustmark Dealer |
| transmission | Categorical | Manual/Automatic |
| owner | Categorical | First Owner/Second Owner/etc |

## Author
Nafiza Mahadri W - Dicoding MLOps Submission
