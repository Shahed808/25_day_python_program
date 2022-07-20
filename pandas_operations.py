''' operators in pandas'''

import pandas as pd

# b = pd.read_csv("C:\\Users\shahed\Downloads\My Uber Drives - 2016.csv")
# print(b.shape)                        # (1156, 7) - (rows,columns)
# print(b,type(b))                      # [1156 rows x 7 columns] <class 'pandas.core.frame.DataFrame'>

# print(b.head())                         # It will give you the 1st five roms in your data sets

# print(b.head(3))                          # If you specify the count of rows you want then we can use this command

# print(b.tail())                             # It will fetch the last 5 rows in your data set

# print(b.tail(2)) 

# print(b[:])

v = pd.read_csv("C:\\Users\shahed\Downloads\player_stats.csv")
# print(v[2:10])                                            # will display only from rows 2 to 
# print(v.columns)                                          # Will display only columns present in the data set
# print(v.rpow)

# print(v.centuries)
# print(v[['Player_Name','strike_rate']])
# print(v.describe())                                         # Overall of the data set

# print(v['Player_Id'][v.centuries].max())                  # Doubt
# print(v[['centuries','Player_Name']])
# print(v)

# print(v['total_runs'].max())                                # 4106

# print(v[v.strike_rate<100])                                     # [263 rows x 26 columns]

# print(v['Player_Name'][v.half_centuries<2])

# print(v[v.total_runs == v.total_runs.max()])                #Doubt

# print(v.loc[5])        # to print a particular person wecan use location method

# print(v)

# r = v.set_index('Player_Id')
# print(r)                                            # It is setting the Player_Id as index 

print(dir(pd))
