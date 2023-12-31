import streamlit as st
#st.set_page_config(layout="wide")

import streamlit.components.v1 as components
import pandas as pd
import codecs
import sweetviz as sv

sv.config_parser.read("override.ini")

def st_display_sweetviz(report_html, width=1000, height=500):

	report_file = codecs.open(report_html, 'r')
	page = report_file.read()
	components.html(page, width=width, height=height, scrolling=True)


def main():

	st.set_page_config(page_title="Exploratory Data Analysis")
	st.title("Exploratory Data Analysis")

	st.subheader('Analyze a comma-separated values file to gain insight into unique values in each column, missing values, values distribution histograms, and more.')
	st.warning('See https://docs.streamlit.io/streamlit-community-cloud/get-started/trust-and-security for information from Steamlit on security', icon='⚠️')

	# CSV file upload
	csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

	if csv_file:

		df = pd.read_csv(csv_file)
		
		st.write('Five random rows')
		df = df.sample(frac=1)
		st.dataframe(df.head(), hide_index=True)

		report = sv.analyze(df)
		report.show_html()
		st.balloons()
		#st.snow()
		st.error('Clicking on Associations doesn\'t yet work', icon="🚨")

		st_display_sweetviz("SWEETVIZ_REPORT.html")


if __name__ == '__main__':
	main()		
