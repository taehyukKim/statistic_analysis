# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
 
# colling the excel files
excel_file = "PO 18660 TR-QQ13T-N00 40G QSFP+ IR4 160PCS (80134213) Shipment Data.xlsx"
raw_data = pd.read_excel(excel_file) 
# Creating dataset

data = []
 
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()