import pandas as pd
import numpy as np
#Load dataset
data=pd.read_csv(r"C:\Users\Admin\Downloads\Mall_Customers.csv")
data
#To check total number of rows and columns
data.shape
data.columns
#To check the datatypes of columns
data.dtypes
#Check for missing values
data.isna().sum()
#Check the information and description
data.info()
data.describe()
#Check the duplicated rows
data.duplicated().sum()
#To Standardize text columns i.e., Gender column
data['Gender'] = data['Gender'].str.strip().str.lower()
print(data['Gender'].unique())
#Rename the header column
data.columns = data.columns.str.lower().str.replace(' ', '_')
print(data.columns)
data
