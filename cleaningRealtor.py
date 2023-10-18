import pandas as pd
import mysql.connector

file_path = "C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\president\\president_county_candidate.csv"
df = pd.read_csv(file_path)
dem_rep = df[df['party'].isin(['DEM', 'REP'])]
print(dem_rep)
#cleaned_df = df[df['state'] != 'Puerto Rico']
save_path = "C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\president-cleaned\\df.csv"
dem_rep.to_csv(save_path, index=False)
print(f"Data saved to {save_path}")