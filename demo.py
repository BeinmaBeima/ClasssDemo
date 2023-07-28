import streamlit as st
import pandas as pd

st.title('Groceries Data Visualization')

@st.cache
def load_data():
    data_url = "https://drive.google.com/uc?export=download&id=1hFGHv3k7Bj3gZo58u9Ty_T1oO_AEjqiw"
    data = pd.read_csv(data_url)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('10 Most Frequently Purchased Items')
item_counts = data['itemDescription'].value_counts().head(10)
st.bar_chart(item_counts)
