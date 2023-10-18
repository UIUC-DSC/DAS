import pandas as pd
import mysql.connector
#Get the file path of the csv we are trying to clean
file_path = "C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\president\\president_county_candidate.csv"
df = pd.read_csv(file_path)

#Create a new df from the original df where the only rows are ones that contain DEM or REP under the party column
dem_rep = df[df['party'].isin(['DEM', 'REP'])]
print(dem_rep)

#Save this new df as a csv
save_path = "C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\president-cleaned\\df.csv"
dem_rep.to_csv(save_path, index=False)
print(f"Data saved to {save_path}")
