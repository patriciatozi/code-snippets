import pandas as pd

# Read the file and load it inside a DataFrame
df = pd.read_excel('sample.xlsx', engine='openpyxl')

# Include a row while creating a new DataFrame
df_final = df.append({'Nome':'Alessandra', 'Idade': 13}, 
                     ignore_index=True)

# Save the new DataFrame in another file
df_final.to_excel('sample_v2.xlsx', 
                  sheet_name='Pessoal', 
                  engine='xlsxwriter', index=False)