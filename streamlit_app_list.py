import pandas as pd
import streamlit as st

df = pd.read_csv(r"final_drug_disease_1.xls")
df.drop('Unnamed: 0', axis=1, inplace=True)


medical_conditions = ['medical_condition', 'condition_1', 'condition_2',
       'condition_3', 'condition_4', 'condition_5', 'condition_6']

def get_corresponding_values(df, word, search_columns, target_columns):
    # Check if the word is in the specified columns
    mask = df[search_columns].apply(lambda row: row.astype(str).eq(word).any(), axis=1)
    
    # Get the values from the target columns where the mask is True
    corresponding_values = df.loc[mask, target_columns]
    
    return corresponding_values



st.title('Medical Condition Search')

word = st.text_input('Enter the medical condition to search:')
if st.button('Search'):
    if word:
        result = get_corresponding_values(df, word, medical_conditions, df.drop(columns=medical_conditions[1:], axis=1).columns)
        if not result.empty:
            st.write("Corresponding Values:")
            st.dataframe(result)
        else:
            st.write("No results found.")
    else:
        st.write("Please enter a word to search.")
