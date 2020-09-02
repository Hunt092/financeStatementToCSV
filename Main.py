from tabula import read_pdf
from tabula import convert_into
import pandas as pd
import os

# Makes a list of files present in PDfs folder (give the name of folder 
# you have your pdfs in) 
try:
    filenames = os.listdir('Pdfs') 
except:
    print("Give a Valid folder")
# The accuracy depends upon the API[tabula] to 
# recognise the tables


for filename in filenames:
    print(f"Scaning {filename} file now")
    dffs=[]
    #Loading in the file to find all the tables in the Particulars
    try:
        dfS =read_pdf(f"Pdfs\{filename}", multiple_tables=True,pages='all')
    except:
        print("Failed to Scan the PDF")
        continue
    #The Pdfs has gto be replaced by the folder in which you have the pds files

    for df in dfS:
        if "Particulars" in df.columns:
    # Following block will Extract the Needed rows  from the the table we need
    #Have to give it a value check so table with particulars is been processed

            Total_expensive=df.loc[df['Particulars']=="Total Expenses"]
            Total_Incomes=df.loc[df['Particulars']=="Total Income"]
            Profit_before_tax=df.loc[df ['Particulars']=="Profit before Tax"]
            Profit_before_tax2=df.loc[df ['Particulars']=="Profit before tax"]
            Profit_after_tax=df.loc[df ['Particulars']=="Net Profit after Tax (A)"]
            
    # A list of need Data frames is made and then added to each other to form 
    # the needed dataframe which we need

            dfs = [Total_Incomes, Total_expensive, Profit_before_tax, 
            Profit_before_tax2, Profit_after_tax]
            try:
                df_final= pd.concat(dfs)
            except:
                df_final=dfs

            dffs.append(df_final) #Making a list of all the dataframes collected

    # Here me make so that all the tables we got are made into one to safe
    # as a single Csv file. Finally the dataFrame is Saved for the File
    #  name .csv Format

    try:
        df_last= pd.concat(dffs)
        df_last.to_csv(f"{filename[:-4]}.csv",index=False)
        print(f"{filename[:-4]}.csv is Made")
    except:
        try:
            df_final.to_csv(f"{filename[:-4]}.csv",index=False)
        except: 
            print("Couldn't find the Table")
            continue

print("Finished")