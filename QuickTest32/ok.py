import adodbapi
import pandas as pd

accdb_path = r'E:\Common Data\Master.accdb'
connection_string = (
    r'Provider=Microsoft.ACE.OLEDB.12.0;'
    r'Data Source='+accdb_path+';'
    r'Persist Security Info=False;'
)

try:
    print('connecting')
    print(connection_string)
    conn = adodbapi.connect(connection_string)
    print('connected')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Master")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns = columns)
    csv_path = r'E:\Common Data\Master.csv'
    df.to_csv(csv_path, index=False)

except adodbapi.Error as e:
    print(e)   
finally:
    cursor.close()
    conn.close()   