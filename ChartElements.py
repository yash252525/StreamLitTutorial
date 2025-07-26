import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Streamlit Charts Demo")

#Creation of sample data for charts
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)


# Area Chart
st.subheader('Area Chart')
st.area_chart(chart_data)

# Bar chart
st.subheader('Area Chart')
st.bar_chart(chart_data)

# Scatter Chart
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame(
    {
        'x': np.random.randn(100),
        'y': np.random.randn(100),
    }
)
st.scatter_chart(scatter_data)

#Map section
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100,2) /[50,50] + [37.76 -122.4],
    columns=['lat','lon']
)
st.map(map_data)


# Pyplot
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'],label='A')
ax.plot(chart_data['B'],label='B')
ax.plot(chart_data['C'],label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)