import pandas as pd

def process_hackathon_csv(input_file, output_file):
    # Read the input CSV into a DataFrame
    df = pd.read_csv(input_file)
    
    # Reshape the DataFrame from wide format to long format
    df_long = df.melt(id_vars=['Project Name'], 
                      value_vars=['Hacker Name 1', 'Hacker Name 2', 'Hacker Name 3', 'Hacker Name 4'], 
                      var_name='Hacker Column', value_name='Hacker Name')
    
    # Drop rows where 'Hacker Name' is NaN or empty
    df_long = df_long.dropna(subset=['Hacker Name'])
    df_long = df_long[df_long['Hacker Name'].str.strip() != '']
    
    # Capitalize the first letter of each word in 'Hacker Name'
    df_long['Hacker Name'] = df_long['Hacker Name'].str.title()
    
    # Select only 'Project Name' and 'Hacker Name' for the final output
    df_final = df_long[['Project Name', 'Hacker Name']]
    
    # Write the output CSV
    df_final.to_csv(output_file, index=False)

# Example usage:
input_csv = 'input.csv'  # Replace with your input CSV file path
output_csv = 'players_per_row.csv'  # Replace with your desired output CSV file path
process_hackathon_csv(input_csv, output_csv)
