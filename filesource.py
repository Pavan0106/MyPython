import pandas as pd
import numpy as np

#ti read a csv file
df = pd.read_csv("filename")

#to read a csav file with no headers
df = pd.read_csv("filename", Header = None)

#to read a csv file with no headers and we can give our own headers
df = pd.read_csv("filename", Names = ["h1","h2","h3"])

#to readcsv file with headers but to overwrite with our own header names
df = pd.read_csv("filename", Header = 0, Names = ["h1","h2","h3"])

#to read a csv file and skip few rows
df = pd.read_csv("filename", skiprows = 2)

#to read csv file and skip first 2 rows and skip footer too
#to skip footer we need to enable python engine
df = pd.read_csv("filename", skiprows = 2, skipfooter = 1, engine = 'python')

#to read scv files with only first 5 rows
df = pd.read_csv("filename", nrows = 5)

#read a large csv file in chunks ( 5 chunks of 10 rows in each chunk)
data_list = []
rows_in_a_chunk = 10
num_chunks = 5
skip_rows = 1

df_dummy = pd.read_csv("file",nrows = 2)
col_names = df_dummy.columns

for i in range(0,rows_in_a_chunk*num_chunks, rows_in_a_chunk):
    df = pd.read_csv("file", Header = 0, skiprows = i, nrows = rows_in_a_chunk,
                     Nmaes = col_names)
    data_list.append(df)

#to skip NOT reading blank lines
df = pd.read_csv("file1", skip_blank_lines = False)

#to read different tabs on an excelfile

df1 = pd.read_csv("filename", sheet_name="tab1")
df2 = pd.read_csv("filename",sheet_name = "tab2")

#if we prefer to get data from all tabs at one go, get it ina dict

dict1 = pd.read_csv("file", sheet_name = "none")
dict1.keys() -> dict1["tab1","tab2"]

#read table fomr a normal text file
df = pd.read_table("filename",  sep = ',')

#read tables embedded in a html file
df1 = pd.read_html("url")

df = df1[0]
df.head() will give the table




