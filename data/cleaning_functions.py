# functions 

import pandas as pd

def replace_age(df):
    
    bins = [0,30,40,50,70,100]
    labels = ['Z generation', 'millennials', 'X generation', 'boomers', '70+']
    df['generation'] = pd.cut(df['clnt_age'], bins = bins, labels = labels, right = False, include_lowest=True)
    
    return df

def handle_duplicates(df):
    """
    Identify and handle duplicate rows in the dataframe by removing them.
    
    Args:
    df (pd.DataFrame): The input dataframe with potential duplicate rows.
    
    Returns:
    pd.DataFrame: The dataframe with duplicates handled and index reset.
    """
    # Check for duplicated values
    duplicates = df.duplicated()  # Identify duplicated values
    number_of_duplicates = duplicates.sum()
    
    # Print the number of duplicated rows
    print(f"Number of duplicated rows before cleaning: {number_of_duplicates}")
    # Remove duplicates and reset index
    df_cleaned = df.drop_duplicates().reset_index(drop=True)
    
    # Check for duplicates after cleaning
    duplicates_after = df_cleaned.duplicated().sum()
    print(f"Number of duplicated rows after cleaning: {duplicates_after}")
    return df_cleaned

def convert_num(df):
    
    df['num_accts'] = df['num_accts'].astype(int)
    bins = [0, 5, 10]
    labels = ['low', 'high']
    df['testing_engagement'] = pd.cut(df['num_accts'], bins = bins, labels = labels, right = False, include_lowest=True)
    
    return df

def convert_bal(df):
    
    bins = [0, 100000, 500000, 1000000, 20000000]
    labels = ['0-100k', '100-500k', '500-1M', '+1M']
    df['balance_level'] = pd.cut(df['bal'], bins = bins, labels = labels, right = False, include_lowest=True)
    
    return df

def convert_tenure(df):
    
    bins = [0, 60, 120, 180, 240, 600, 800]
    labels = ['0-5', '5-10', '10-15', '15-20', '20-50', '+50']
    df['tenure'] = pd.cut(df['clnt_tenure_mnth'], bins = bins, labels = labels, right = False, include_lowest=True)
    
    return df

def handle_merge(df1, df2, df3):
    df_all = pd.merge(df1, df2, on='client_id', how='inner')
    df_all = pd.merge(df_all, df3, on='client_id', how='inner')

    return df_all

