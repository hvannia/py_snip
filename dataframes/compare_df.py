# porgram to compare two pandas dataframes
import pandas as pd

# read in the two files
df1 = pd.read_csv('df1.csv')
df2 = pd.read_csv('df2.csv')

# compare the two files
# GitHub Copilot: This line of code performs an outer join between two dataframes `df1` and `df2` 
# and adds a column `_merge` to the resulting dataframe `compare` to indicate the source of each row. 
# The `_merge` column will have one of three values: `left_only` if the row is only present in `df1`, 
# `right_only` if the row is only present in `df2`, and `both` if the row is present in both dataframes.

# do not include the column 'con' in the comparison
df1 = df1.drop(columns=['con'])
df2 = df2.drop(columns=['con'])
compare = df1.merge(df2, indicator=True, how='outer')
compare = compare[compare['_merge'] != 'both']
compare.to_csv('compare.csv', index=False)
print(compare)

# function to make a POST HTTPS request to endpoint, including a Token header
# include data in in the request body
def make_https_request(endpoint, token, data):
    headers = {'Token': token}
    response = requests.post(endpoint, headers=headers, data=data)
    return response
