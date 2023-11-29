import pandas as pd
from sklearn.impute import KNNImputer

df = pd.read_csv('C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\smallerCrime.csv')
df = df.replace('NA', pd.NA)
columns = ["percent_no_highschool_diploma", "percent_children_in_poverty", "percent_fair_or_poor_health"]
data = df[columns]
impute_knn = KNNImputer(n_neighbors = 55)
df_imputed = pd.DataFrame(impute_knn.fit_transform(data))

df[columns] = df_imputed
df.to_csv('noCrimeNA.csv')
