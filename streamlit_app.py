import streamlit as st
#st.set_page_config(layout="wide")
import pandas as pd

def on_text_area_change():

    st.session_state.page_text = st.session_state.my_text_area
    

def main():

    st.set_page_config(page_title="Exploratory Data Analysis")
    st.title("Exploratory Data Analysis")

    # CSV file upload
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if csv_file:

      df = pd.read_csv(csv_file)
      st.dataframe(csv_file.head())

if __name__ == '__main__':
    main()
