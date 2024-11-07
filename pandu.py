import pandas as pd
df=pd.read_csv('sample.csv',index_col=0)
# df['Name']=df['Name'].str.upper()
# df['Name']=df['Name'].str.strip()
# df.rename(columns={'Name':'Name'},inplace=True)
# df.replace({'Linda':'Linda'},inplace=True)
df.loc[4, 'Name'] = 'Sonali'
df['Name']=df['Name'].str.upper()
print(df)