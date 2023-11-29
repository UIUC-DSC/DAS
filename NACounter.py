import pandas as pd

# Load the dataset
df = pd.read_csv('C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\datasets\\county_all_col_2.csv')

# Count the number of missing values in each column
na_counts = df.isna().sum()

# Filter the columns with more than 0 missing values
na_counts_filtered = na_counts[na_counts > 0]

# Convert the filtered series to a DataFrame for easier display
na_counts_df = pd.DataFrame(na_counts_filtered, columns=['Missing Values'])

# Display the number of missing values for each column with more than 0 missing values as a table
if not na_counts_filtered.empty:
    print("Number of missing values (NaN) for each column with more than 0 missing values:")
    print(na_counts_df)
else:
    print("No columns have more than 0 missing values.")
