import streamlit as st
import pandas as pd
import altair as alt
from IPython.display import Markdown
import baseline as base
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Car Prices in Poland 🚗')
st.markdown(
    '<h1 style="color: maroon; font-size: 20px;">welcome to page 1</h1>',
    unsafe_allow_html=True
)


car = pd.read_csv('Car_Prices_Poland.csv')
carname = st.selectbox("Select your car",car['mark'].unique())
st.write(carname)
plot_type=st.radio("select the plot type",['scatter','line','bar','slope','Natural Disasters','Donut Chart'])
if plot_type == 'scatter':
  pl = alt.Chart(car[car['mark']==carname]).mark_circle().encode(
    x = 'vol_engine',
    y ='price',
    tooltip = ['vol_engine','price']
).interactive()
elif plot_type == 'line':
  pl = alt.Chart(car[car['mark']==carname]).mark_line().encode(
    x = 'vol_engine',
    y ='price',
    color = 'fuel',
    tooltip = ['vol_engine','price']
).interactive()
elif plot_type == 'bar':
   pl = alt.Chart(car[car['mark']==carname]).mark_bar(opacity=0.7).encode(
    x='year:O',
    y=alt.Y('price:Q', stack=None),
    color="city",
).interactive()
elif plot_type == 'slope':
   pl = alt.Chart(car).mark_line().encode(
    x='year:O',
    y='mark',
    color='city'
).interactive()
elif plot_type == 'Natural Disasters':
  pl = alt.Chart(car[car['mark']==carname]).mark_circle(
    opacity=0.8,
    stroke='black',
    strokeWidth=1
).encode(
    alt.X('price:O', axis=alt.Axis(labelAngle=0)),
    alt.Y('city:N'),
    alt.Size('mileage:Q',
        scale=alt.Scale(range=[0, 4000]),
        legend=alt.Legend(title='Car Prices Poland')
    ),
    alt.Color('city:N', legend=None)
).properties(
    width=450,
    height=320
).transform_filter(
    alt.datum.Entity != 'All natural disasters'
).interactive()
else:
 pl = alt.Chart(car[car['mark']==carname]).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field="year", type="quantitative"),
    color=alt.Color(field="city", type="nominal"),
).interactive()

st.altair_chart(pl)
