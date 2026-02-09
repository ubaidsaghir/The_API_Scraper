import pandas as pd 

df = pd.read_csv("patients.csv")

print(df.head(10))
print(df.dtypes)
print(df.shape)

# Rename columns:

df.rename(columns={
    "patient_id": "ID",
    "name": "First Name",
    "age": "Patient_age",
}, inplace=True)

print(df.head(10))


senior_patients = df[df["Patient_age"] > 60]
print(senior_patients.head())
print("Count:", senior_patients.shape[0])


#select specify columns
# print(df)
# print(df.loc[:, ["First Name","Patient_age"]])
