import pandas as pd
import joblib
import ast

# 1. Load model dan encoder
model = joblib.load('models/model.pkl')
encoder = joblib.load('models/onehot_encoder.pkl')

# 2. Fitur penting
important_categorical = ['OverTime', 'MaritalStatus', 'BusinessTravel', 'JobRole']
important_numerical = ['JobLevel', 'JobInvolvement', 'MonthlyIncome', 'TotalWorkingYears',
                       'EnvironmentSatisfaction', 'WorkLifeBalance', 'YearsAtCompany']

# 3. Baca file input.txt
with open('data/input.txt', 'r') as f:
    input_str = f.read()

try:
    input_data = ast.literal_eval(input_str)
except Exception as e:
    print("Format input.txt salah. Harus dictionary Python.")
    print("Contoh isi:\n{'OverTime': 'Yes', 'JobRole': 'Research Scientist', ...}")
    exit()

# 4. Konversi ke DataFrame
df_input = pd.DataFrame([input_data])

# 5. Encode kategori
X_cat = encoder.transform(df_input[important_categorical])
cat_cols = encoder.get_feature_names_out(important_categorical)

# 6. Gabungkan dengan numerik
X_num = df_input[important_numerical].reset_index(drop=True)
X_ready = pd.concat([X_num, pd.DataFrame(X_cat, columns=cat_cols)], axis=1)

# 7. Prediksi
prediction = model.predict(X_ready)[0]
proba = model.predict_proba(X_ready)[0][1]

# 8. Tampilkan hasil
print("Hasil Prediksi:")
if prediction == 1:
    print(f"Karyawan diprediksi AKAN keluar (Attrition = 1), kemungkinan: {proba:.2%}")
else:
    print(f"Karyawan diprediksi TIDAK AKAN keluar (Attrition = 0), kemungkinan keluar: {proba:.2%}")