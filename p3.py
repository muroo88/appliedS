import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
data = pd.read_csv('Car_Prices_Poland.csv')

# Create a figure object
fig = plt.figure()

st.title('Car Prices in Poland 🚗')
st.markdown(
    '<h1 style="color: #000080; font-size: 20px;">Select this option to show only Hybrid cars in the chart</h1>',
    unsafe_allow_html=True
)
# Add a plot to the figure
plt.plot(data['year'], data['price'])

# Create a check box
checkbox = st.checkbox('Show Only Hybrid Cars')

# Define a function to filter the data based on the check box value
def filter_data():
    if checkbox:
        # Show only electric cars
        data_filtered = data[data['fuel'] == 'Hybrid']
    else:
        # Show all cars
        data_filtered = data
    
    # Update the plot with the filtered data
    plt.cla()
    plt.plot(data_filtered['year'], data_filtered['price'])
    

# Call the function to filter and update the plot when the check box value changes
if checkbox:
    filter_data()

# Display the plot
st.pyplot(fig)
