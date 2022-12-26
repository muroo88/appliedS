import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties

st.title('Car Prices in Poland 🚗')
st.markdown(
    '<h1 style="color: maroon; font-size: 20px;">welcome to page 2</h1>',
    unsafe_allow_html=True
)
car = pd.read_csv('Car_Prices_Poland.csv')
fig, ax = plt.subplots()
ax.bar(car['year'], car['mileage'])
font = FontProperties(fname='pages/NotoEmoji-Regular.ttf')
plt.text(2015, 500, '🚗', fontproperties=font,color='red',fontsize=50)
st.pyplot(fig)
