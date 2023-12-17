import streamlit as st
#st.set_page_config(layout="wide")
import pandas as pd

def main():

    st.set_page_config(page_title="Exploratory Data Analysis")
    st.title("Exploratory Data Analysis")

    # CSV file upload
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if csv_file:

      df = pd.read_csv(csv_file)
      st.dataframe(df.head(), hide_index=True)

if __name__ == '__main__':
    main()
