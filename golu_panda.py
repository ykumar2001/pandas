import pandas as pd
from datetime import datetime
df=pd.read_csv('employee_data.csv')
dt=pd.DataFrame(df)
# dt=dt.head()
# dt['Age'].fillna(dt['Age'].mean(),inplace=True)
# dt['Salary'].fillna(dt['Salary'].median(),inplace=True)
# dt['LeaveDays'].fillna(0,inplace=True)
# dt['JoinDate']=pd.to_datetime(dt['JoinDate'])
# avg_sal=dt.groupby('Department')['Salary'].mean()
# count=dt.groupby('Department')['EmployeeID'].count()
# high_sal=dt.loc[dt['Salary'].idxmax()]
# print(count)
# print(high_sal)
# most_leave=dt.loc[dt['LeaveDays'].idxmax()]
# print(most_leave)
# dm=dt[dt['LeaveDays']>10]
# print(dm)
# sal_60000=dt[dt['Salary']>60000]
# print(sal_60000)
dt['JoinDates']=pd.to_datetime(df['JoinDates'])
current_date= datetime.now()
dt['workdays']=(current_date-dt['JoinDates']).dt.days
print(dt)