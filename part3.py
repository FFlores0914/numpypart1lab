import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]


df = pd.DataFrame(data)


print(df.dtypes)


df['age'] = df['age'].astype(float)
df['ejection_fraction'] = df['ejection_fraction'].astype(float)
df['serum_creatinine'] = df['serum_creatinine'].astype(float)


fumadores_por_genero = df.groupby(['is_male', 'is_smoker']).size().reset_index(name='count')
print(fumadores_por_genero)