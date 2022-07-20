import pandas as pd
''' with the help of dict we are creating data frames from it'''
# create = {'ravi':['andhra','full stack','josh innovations'],
# 'Babu':['ameerpet','fullstack','satya technologies'],
# 'gautham':['warangal','python and sql','naresh it'],
# 'niharika':['begumpet','python','qspyder'],
# 'mandaram':['ecil','python with django','hari technologies']
# }

# print(create)
# df1= pd.DataFrame(create)
# print(df1)


''' Now we are using tuple to create the data frame'''

# h = (['josh innovations','python',10000],['naresh it','full stack',8500],['satya technologies','Django',12000],['hari technologies','Aws',25000],['network institue','Power bi',18000])
# d = pd.DataFrame(h,columns=['Institutes','courses offered','price'])
# print(d)


''' we need to import any file and read the csv file
To read the csv file we need to instal xlrd'''

# w = pd.read_csv("C:\\Users\shahed\Downloads\My Uber Drives - 2016.csv")
# print(w)

# t = pd.read_csv("C:\\Users\shahed\Downloads\player_stats.csv")
# print(t)

''' Now we need to read the excel file
we need to download the openpyxl'''

v = pd.read_excel("C:\\Users\shahed\Downloads\excel_data.xlsx")
print(v)

