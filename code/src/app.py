import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from data_profiling import load_data, generate_summary, visualize_all_columns
from report_generation import generate_report

def generate_charts(data):
    # Create a directory to save the charts
    if not os.path.exists("charts"):
        os.makedirs("charts")
    
    # Generate a histogram for each numeric column
    numeric_columns = data.select_dtypes(include=['number']).columns
    for column in numeric_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(f'charts/{column}_distribution.png')
        plt.close()

def main():
    # Load custom CSS
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.title("Data Profiling Application")
    
    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = "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"
    
    # File uploader for data
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Load data
        data = load_data(uploaded_file)
        
        # Create tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Data Summary", "Data Visualizations", "Query Customer Details", "Generate Report", "Feedback"])
        
        with tab1:
            st.subheader("Data Summary")
            summary = generate_summary(data)
            st.write(summary)
        
        with tab2:
            st.subheader("Data Visualizations")
            visualize_all_columns(data)
            st.write(data)
        
        with tab3:
            st.subheader("Query Customer Details")
            query_column = st.selectbox("Select Column to Query", data.columns)
            query_value = st.text_input("Enter Query Value")
            if st.button("Query"):
                query_result = data[data[query_column].astype(str) == query_value]
                st.write(query_result)

        with tab4:
            st.subheader("Generate Report")
            if st.button("Generate Report"):
                # Generate charts
                generate_charts(data)
                
                # Generate report
                report = generate_report(summary, None, None)
                st.write(report)
                
                # Display charts
                st.subheader("Generated Charts")
                for column in data.select_dtypes(include=['number']).columns:
                    st.image(f'charts/{column}_distribution.png')
        
        with tab5:
            st.subheader("Feedback")
            feedback = st.radio(
                "How would you rate your experience?",
                ("😃 Great", "🙂 Good", "😐 Okay", "🙁 Bad", "😡 Terrible")
            )
            if st.button("Submit Feedback"):
                st.write("Thank you for your feedback!")

if __name__ == "__main__":
    main()
