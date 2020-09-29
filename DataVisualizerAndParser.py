import streamlit as st
import pandas as pd

st.title('Data Visualizer and Parser for CO2 Emissions')

st.header('Overview')
st.markdown('This data visualizer was made to understand and analyse the CO2 emissions of a given country. It also takes a look at some peculiar countries that have drastically different CO2 emissions compared to the rest of the world. All values on this page are of the unit: metric tons per capita. Furthermore, all the data used in this project is open source and available at the World Bank Open Data.')

@st.cache   #To reduce load time during future use
def load_data(nrows):
    data = pd.read_csv('transposed_co2_data.csv', nrows=nrows)
    return data

data = load_data(300)

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)

#The world's graph

st.markdown('The following graph shows the average CO2 emission of the world. This acts as a reference graph while analyzing other country\'s statistics.')
world_data = pd.DataFrame(data, columns = ['World'])
st.bar_chart(world_data)
st.markdown('Not a surprise to anyone that the trendline of the world CO2 emissions is increasing :(.')

#Comparison graphs

st.header('Comparison of certain countries')
st.subheader('India & Canada')
st.markdown('Something I found interesting was looking at the trend of developing countries and developed countries and seeing how their trends were so different from each other.')
chart_data1 = pd.DataFrame(data, columns = ['India', 'Canada'])
st.line_chart(chart_data1)
st.markdown('It\'s clearly visible from the graph that the values in emission for the two countries are miles apart, but another thing to notice would be their trendlines which in the case of India is increasing compared to Canada which is decreasing because it has crossed the threshold of a developed country.')

st.subheader('Albania & Middle-East')
chart_data2 = pd.DataFrame(data, columns = ['Albania', 'Arab World'])
st.line_chart(chart_data2)
st.markdown('An intresting comparison to do is between Albania and the Middle-East. Albania started with a relatively higher CO2 emission value than the Middle-East, but due to the rapid expansion of the middle-eastern countries and the spiked growth of oil companies in the area during the late 80s gave rise to this polarity between the two places.')

#Data parser for displaying certain CO2 emissions

st.header('Compare any two countries for CO2 emissions')
st.markdown('Enter the name of any two countries to compare and analyze their CO2 emissions. You can even compare a certain country\'s emission data with that of the world average by typing in World in any of the two input areas.')
st.text('Verify if a country\'s data is available in the raw data table.')

country1 = st.text_input('Enter Country 1: ')
country2 = st.text_input('Enter Country 2: ')
cap_country1 = country1.capitalize()    #If users write in lowercase
cap_country2 = country2.capitalize()
if st.button('Enter'):
    chart_data3 = pd.DataFrame(data, columns = ['{}'.format(cap_country1), '{}'.format(cap_country2)])
    st.line_chart(chart_data3)