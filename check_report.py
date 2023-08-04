# fucntion that takes in a dataframe, sorts it and groups it by column 'class', 
# then yields distinct rows from column 'pdf' within the group   
def check_report(df):
    df = df.sort_values(by=['class'])
    for pdf, group in df.groupby('class'):
        yield group['pdf'].unique() 

# Path: check_report.py

