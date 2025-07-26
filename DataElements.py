import streamlit as st
import pandas as pd

st.title("Streamlit Data Elements Demo")


st.subheader("Dataframe")

df = pd.DataFrame({
    'Name': ['Alice','Bob'],
    'Age' : [25,30],
    'Occupation' : ['Engineer', 'AI Engineer']

})
# if you click on keys on webpage we can sort it ascending and descending
st.dataframe(df)


# Data Editor Section (Editable dataframe)
# These dataframes can be edited
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)


# Static Table
st.subheader('Static Table')
st.table(df)


# Metrics
st.subheader('Metrics')
st.metric(label="Total rows",value= len(df))
st.metric(label="Average Age",value=round(df['Age'].mean(),1))


# JSON and Dict
st.subheader('JSON and Dictionary')
sample_dict = {
    "name" : "Yash",
    "age" : 25,
    "skills" : ["AWS","Python","AI-ML","DevOps"]
}

# we can also use st.write()
st.json(sample_dict)