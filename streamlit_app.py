import streamlit as st
import streamlit.components.v1 as components
#st.set_page_config(layout="wide")
import pandas as pd
import sweetviz as sv

def main():

    st.set_page_config(page_title="Exploratory Data Analysis")
    st.title("Exploratory Data Analysis")

    # CSV file upload
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if csv_file:

      df = pd.read_csv(csv_file)
      st.dataframe(df.head(), hide_index=True)

      analysis = sv.analyze([df,'EDA'], feat_cfg=sv.FeatureConfig(
        #skip=skip_columns_time_series,
        force_text=[]), target_feat=None)

      analysis.show_html(filepath='./frontend/public/EDA.html', open_browser=False, layout='vertical', scale=1.0)
      components.iframe(src='http://localhost:3001/EDA.html', width=1100, height=1200, scrolling=True)

if __name__ == '__main__':
    main()
