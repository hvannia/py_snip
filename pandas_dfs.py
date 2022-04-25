import pandas as pd


# apply a function to a df column, save to new column
def func_name(v):
	return v+1

df['z'] = df['x'].apply(func_name)

## DATE ops
# make a stringc olumn date type
df['date']= pd.to_datetime(df['date'])
df['bdate']=  [ '2003-10-05' for x in range(len((df)))]
df['bdate']= pd.to_datetime(df['bdate'])
# differemce an save as numer
df['ddiff']=(df['date']-df['bdate']).dt.days


#Group by and iterate
grouped = df.group_by('group_column')
for index, grouped_row in grouped:
	for i in list(grouped_row.index):
		x = grouped_row.field[i]


#Iterate over df
for index, row in df.iterrows():
	pass


# Sort by
df = pd.DataFrame.from_dict(name).T
df = df.sort_values(by=['col1','col2'])


#Save dict to csv
outdf = DataFrame.from_dict(outdata)
outdf.to_csv(outfilename)


#Save to excel with multiple sheets
import pandas as pd
import xlswriter

writer = pd.ExcelWriter('filename.xlsx', engine='xlsxwriter')
	# a dataframe for each sheet
if not df1.empty:
	df1.to_excel(writer,sheet_name='df1')
writer.save()


# print nice table
from rich import print
from rich_tools import df_to_table
filename='homes.csv'
df = pd.read_csv(filename)
table = df_to_table(df)
print(table)


# colros
def color_df(val):
	color = 'red' if val <0 else 'green'
	return 'color: %s' % color

df = pd.DataFrame(dict(
	col1 = [1.53, -2.5, 3.53],
	col2 = [-4.1, 5.9, 0]
))
df.style.applymap(color_df)