import pandas as pd


def delete_odd_rows(input_csv, output_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Define a function to filter out odd rows starting from row 3 (index 2)
    def is_odd_row(index):
        return index < 2 or index % 2 == 0

    # Filter the DataFrame
    filtered_df = df[df.index.to_series().apply(is_odd_row)]

    # Save the modified DataFrame back to a CSV file
    filtered_df.to_csv(output_csv, index=False)
    print(f"The modified DataFrame has been saved to {output_csv}")


# Input: Path to the input CSV file
input_csv = "C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\president-cleaned\\CLEANED_presidential_counties.csv"

# Output: Path to the output CSV file
output_csv = "C:\\Users\\dansi\\OneDrive\\DSC Sem 1\\president-cleaned\\CLEANED_presidential_counties.csv"

# Call the function
delete_odd_rows(input_csv, output_csv)
