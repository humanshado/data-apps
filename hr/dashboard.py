import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")
st.subheader('ABC Human Resources Dashboard')
"""
***
"""
# import data
df = pd.read_csv('data.csv')
st.write(df.info())
st.dataframe(df)

# clean data
def clean_df(data, col, col_name):
    l = []
    for i in col.items():
        temp = i[1].split(',')
        temp = ''.join(map(str, temp))
        l.append(temp)

    col = pd.to_numeric(pd.Series(l))
    data[col_name] = col


col_names = ['Locals', 'Expatriates', 'Headcount','Incentive Paid', 'Overtime Paid']

for col_name in col_names:
    col = df[col_name]
    clean_df(df, col, col_name)
cleaned_df = df
cleaned_df.info()

months = df.Month
col1, col2 = st.beta_columns([1, 3])
col1.selectbox('Select Month', months)
col2.empty()
"""
***
"""
mask = cleaned_df.Month == 'Jan'
# m_selection = cleaned_df[mask][['Locals', 'Expatriates']]
# m_selection = m_selection.melt(var_name='Staff', value_name='#StaffCount')
# px.pie(m_selection, values='#StaffCount', names='Staff',
#        color_discrete_sequence=['#6a8d92', 'orange'])

with st.beta_container():
  c1, c2, c3, c4, c5, c6 = st.beta_columns([2.6, 1.5, 1.5, 2, 2.6, 1.5])

  #components
  m_selection = cleaned_df[mask][['Locals', 'Expatriates']]
  m_selection = m_selection.melt(var_name='Staff', value_name='#StaffCount')

  #c1
  with st.beta_container():
    # p = px.pie(m_selection, values='#StaffCount', names='Staff',
    #             color_discrete_sequence=['green', 'orange'],
    #             width=800, height=400, title='Locals vs Expatriates staff')
    # p.update_layout(showlegend=False)
    # c1.plotly_chart(p, use_container_width=True)
    p = plt.pie(m_selection['#StaffCount'])
    c1.pyplot(p)

  #c2
  with st.beta_container():
    c2.image(Image.open('../images/ring.png'), width=105)
  #c3
  with st.beta_container():
    c2.image(Image.open('../images/bracelet.png'), width=105)
  c4.selectbox('incent-overTime-payroll', months)
  c5.selectbox('performance', months)
  c6.selectbox('outsource-partimers', months)
"""
***
"""
with st.beta_container():
  c1, c2, c3, c4, c5, c6 = st.beta_columns(6)
  c1.selectbox('pie chart2', months)
  c2.selectbox('gender-workers2', months)
  c3.selectbox('SickL-latehrs2', months)
  c4.selectbox('incent-overTime-payroll2', months)
  c5.selectbox('performance2', months)
  c6.selectbox('outsource-partimers2', months)
"""
***
"""
with st.beta_container():
  c1, c2, c3, c4, c5 = st.beta_columns([4, 2.6, 1.5, 2, 2])
  c1.selectbox('pie chart23', months)
  c2.selectbox('gender-workers23', months)
  c3.selectbox('SickL-latehrs23', months)
  c4.selectbox('incent-overTime-payroll23', months)
  c5.selectbox('performance23', months)
"""
***
"""

