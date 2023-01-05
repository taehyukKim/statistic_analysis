# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
 
# colling the excel files
excel_file = r'C:\Users\ktkim\Documents\BOX_plot\PO 18660 TR-QQ13T-N00 40G QSFP+ IR4 160PCS (80134213) Shipment Data.xlsx'
raw_data = pd.read_excel(excel_file, header=1)
raw_data.head()

raw_data.columns
print(raw_data.columns)
size = raw_data.shape
# Creating dataset
## select the 25 degree
tem25_raw_data = raw_data.loc[raw_data['Temps(C)'] == 25]
each_lane_data = []
## make the variable for each lane
for i in range(4):
    globals()["each_temp25_{}".format(i+1)] = tem25_raw_data.loc[tem25_raw_data["Channel"] == i+1]
    each_lane_data.append(globals()["each_temp25_{}".format(i+1)])
## cutting the colum for ["SN","Temps(C)","TxLOP_DCA(dBm)","DMI_TxLOP_Err(dB)","Csen(dBm)","DMI_RxPWR_MaxErr(dB)"]
for j in range(len(each_lane_data)):
    each_lane_data[j] = each_lane_data[j].loc[:,["SN","Channel","Temps(C)","TxLOP_DCA(dBm)","DMI_TxLOP_Err(dB)","Csen(dBm)","DMI_RxPWR_MaxErr(dB)"]]
    each_lane_data[j]["TX DDM/DMI"] = each_lane_data[j]["TxLOP_DCA(dBm)"] + each_lane_data[j]["DMI_TxLOP_Err(dB)"]
    each_lane_data[j]["RX DDM/DMI"] = each_lane_data[j]["Csen(dBm)"] + each_lane_data[j]["DMI_RxPWR_MaxErr(dB)"]
    
    globals()["data{}".format(j+1)] = pd.DataFrame(each_lane_data[j])
    print(each_lane_data[1].shape)
    print(type(each_lane_data[1]))
## creating the new column as ["TX DDM/DMI","RX DDM/DMI "]


    
#data = []
 
#fig = plt.figure(figsize =(10, 7))
 
# Creating plot
#plt.boxplot(data)
 
# show plot
#plt.show()