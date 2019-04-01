#import packages
import pandas as pd
import numpy as np
from pandas import Timestamp


#read the file
df = pd.read_csv('台灣電力公司_過去電力供需資訊.csv')
temp_sub = {'date': [],'peak_load(MW)':[]}
sub_df = pd.DataFrame(data=temp_sub)

#setting index as date
df['日期'] = pd.to_datetime(df.日期,format='%Y%m%d')
df.index = df['日期']

#creating dataframe with date and the target variable
data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0,len(df)),columns=['日期', '尖峰負載(MW)'])

for i in range(0,len(data)):
     new_data['日期'][i] = data['日期'][i]
     new_data['尖峰負載(MW)'][i] = data['尖峰負載(MW)'][i]

#train
train = new_data[:]

new_data.shape, train.shape
((424, 2), (424, 2))

train['日期'].min(), train['日期'].max()

(Timestamp('2018-01-24 00:00:00'),
Timestamp('2019-02-28 00:00:00'))

#make predictions
preds = []
for i in range(0,7):
    a = train['尖峰負載(MW)'][len(train)-7+i:].sum() + sum(preds)
    b = a/7
    preds.append(b)
    sub_df=sub_df.append({'date': '2019040'+str(i+2),'peak_load(MW)':b}, ignore_index=True)



#output
sub_df.set_index('date' , inplace=True)
sub_df.to_csv('submission.csv')

