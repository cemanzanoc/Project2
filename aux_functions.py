# aux functions 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


def create_frequency_table(df_control, df_test,name):
    
    # control
    frequency_table_control = df_control[name].value_counts()
   
    proportion_table_control = df_control[name].value_counts(normalize=True)
    
    # test
    frequency_table_test = df_test[name].value_counts()
   
    proportion_table_test = df_test[name].value_counts(normalize=True)
    
    return frequency_table_control, proportion_table_control, frequency_table_test, proportion_table_test


def no_repetition(df):
    
    df_no_repetition = df[(df['process_step'].shift() != df['process_step']) | (df['visit_id'].shift() != df['visit_id'])]
    
    return df_no_repetition

def step_rate(df, state):
    
    
    df_step = df[df["process_step"] == state].groupby("client_id").agg({"process_step":"count"})
    return round(df_step.shape[0]/df.groupby("client_id").agg({"process_step":"count"}).shape[0]*100, 2)

def time_spent_each_step(df):
    
    df = df.sort_values(by=['client_id', 'visit_id', 'date_time'])
    df['time_spent'] = df.groupby('visit_id')['date_time'].diff()
    
    return df

def mean_time_spent(df):
    
    return df.groupby('process_step')['time_spent'].mean()


def transform_to_errores(df):
    
    step_order = {'start': 0, 'step_1': 1, 'step_2': 2, 'step_3': 3, 'confirm': 4}
    df['step_order'] = df['process_step'].map(step_order)
    df = df.sort_values(by=['client_id', 'visit_id', 'date_time'])
    df['previous_step_order'] = df.groupby('visit_id')['step_order'].shift(1)
    df['is_error'] = (df['step_order'] < df['previous_step_order'])
    
    return df

def percentage_errors(df):
    
    error_count = df['is_error'].sum()
    percentage = (error_count/df.shape[0])*100
    
    print(f'Percentage of errors : {percentage}')
    
    return percentage


def mean_errors_per_category(df, category):
    
    error_rate_per_category = df.groupby(category)['is_error'].mean()
    
    print(f'Error rate per {category}: {error_rate_per_category}')
    
    return error_rate_per_category


def create_barplot_error(df_control, df_test, category):
    
    df_control = df_control.reset_index()
    df_control.columns = [category, 'error_rate_control']


    df_test = df_test.reset_index()
    df_test.columns = [category, 'error_rate_test']

    max_ylim = max(df_control['error_rate_control'].max(), df_test['error_rate_test'].max())*1.1
    # Crear el gráfico con Seaborn
    plt.figure(figsize=(11, 6))
    plt.subplot(1,2,1)
    sns.barplot(x=category, y='error_rate_control', data=df_control, palette='Set2')
    plt.ylim([0,max_ylim])

    # Título y etiquetas
    plt.title(f'Average of error rate per {category} in control')
    plt.xlabel(category)
    plt.ylabel('Error rate average')

    plt.subplot(1,2,2)
    sns.barplot(x=category, y='error_rate_test', data=df_test, palette='Set2')
    plt.ylim([0,max_ylim])
    # Título y etiquetas
    plt.title(f'Average of error rate per {category} in test')
    plt.xlabel(category)
    plt.ylabel('Error rate average')

    # Mostrar gráfico
    plt.tight_layout()
    plt.show()
    
def without_error(df):
    
    error_count = df.groupby('visit_id')['is_error'].sum()
    valid_id = error_count[error_count == 0].index
    df_without_error = df[df['visit_id'].isin(valid_id)]
    
    return df_without_error
    
def t_student(df_test, df_control, columna):
    grupo_test= df_test[columna]
    grupo_control = df_control[columna]
    t_stat, p_value = st.ttest_ind(grupo_test, grupo_control, equal_var=False)
    
    if p_value < 0.05:
        resultado = "Rechazamos la hipótesis nula: son significativamente diferentes."
    else:
        resultado = "No rechazamos la hipótesis nula: no hay diferencia significativa."
    
    return t_stat, p_value, resultado
