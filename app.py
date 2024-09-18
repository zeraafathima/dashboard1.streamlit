import streamlit as st
import pandas as pd
import plotly.express as px
st.header('Dashboard')
data=pd.read_csv('/workspaces/dashboard1.streamlit/mentornow/bank.csv')
with st.expander('show data'):
    st.write(data)
jobs=data['job'].unique()
option=st.selectbox('select a job',jobs)
df = data[data['job']==option]
st.write(df)
average=df['age'].mean()
st.write(round(average))
st.metric(label='average age',value=round(average))
