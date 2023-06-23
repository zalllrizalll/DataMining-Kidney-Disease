import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    #judul halaman aplikasi
    st.title("Aplikasi Prediksi Penyakit Batu Ginjal")
    df = pd.read_csv('kidney-disease.csv')
    st.write("Tampilan Dataset")
    st.dataframe(df)

    st.write("Tampilan Bar Chart untuk setiap atribut")
    for column in df.columns:
        if df[column].dtype != 'object':
            plt.figure()
            plt.title('persebaran data - {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            sns.countplot(data=df, x=column)
            st.pyplot(plt)