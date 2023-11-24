import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
# For example, if it's a CSV file named 'your_dataset.csv'
df = pd.read_csv('NetflixOriginals.csv')

# Title of the dashboard
st.title('Interactive Dashboard')

# Display the raw dataset
st.subheader('Raw Data')
st.write(df)

# Sidebar to select options
option = st.sidebar.selectbox('Select an option', ['Graph 1', 'Graph 2'])

# Create graphs based on the selected option
if option == 'Graph 1':
    # Example: Bar chart
    st.subheader('Bar Chart')
    bar_data = df['Genre'].value_counts()
    st.bar_chart(bar_data)

elif option == 'Graph 2':
    # Example: Line chart
    st.subheader('Line Chart')
    line_data = df.groupby('Title')['Runtime'].sum()
    st.line_chart(line_data)

# You can add more graphs or customize the existing ones based on your dataset.

# Save the script as 'app.py' and run it using the following command in your terminal:
# streamlit run app.py
