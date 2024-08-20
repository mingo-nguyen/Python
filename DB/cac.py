import adodbapi
import pandas as pd

# Path to your Access database file
database_path = r'D:\OneDrive\RPA\Python\DB\Go.accdb'

# Connection string
connection_string = (
    r'Provider=Microsoft.ACE.OLEDB.12.0;'
    r'Data Source=' + database_path + ';'
    r'Persist Security Info=False;'
)

# Connect to the database
conn = adodbapi.connect(connection_string)
cursor = conn.cursor()

# Select data from the "Master" table
cursor.execute("SELECT * FROM [Go]")
rows = cursor.fetchall()

# Get column names
columns = [desc[0] for desc in cursor.description]

# Close the cursor and connection
cursor.close()
conn.close()

# Create a DataFrame
df = pd.DataFrame(rows, columns=columns)

# Write DataFrame to a CSV file
csv_file_path = r"D:\OneDrive\RPA\Python\DB\cac.csv"
df.to_csv(csv_file_path, index=False)

print(f"Data successfully written to {csv_file_path}")
