import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://gist.githubusercontent.com/jennioksman/6396cb1bfa9db6c247c9e2a2d44f343e/raw/e7e4919fc02f478ca31aebac997919d3fbfd609a/gistfile1.csv'
df = pd.read_csv(url)


with st.sidebar:
    st.subheader("Facts About Titanic")
    st.text("RMS Titanic was a British ocean liner that tragically sank in the early hours of 15 April 1912 as a result of striking an iceberg on her maiden voyage from Southampton, England, to New York City, United States.\nIt was the second time White Star Line had lost a ship on its maiden voyage, the first being the RMS Tayleur in 1854. Of the estimated 2,224 passengers and crew aboard, approximately 1,500 died (figures vary), making the incident one of the deadliest peacetime sinkings of a single ship.(Wikipedia)")

st.header("Titanic Data Explore")
st.image("./titanic-6972725_640.jpg")

st.divider()

col1, col2 = st.columns(2)

with col1:
    survived_by_gender = df.groupby('Sex')['Survived'].sum()
    fig, ax = plt.subplots()

    st.subheader("Survived by Gender")
    colors = ['#eeb4a9', '#98b9e5']
    ax.bar(survived_by_gender.index, survived_by_gender.values, color=colors)

    st.write(fig)

with col2:
    fig, ax = plt.subplots()
    survived_by_pclass = df.groupby('Pclass')['Survived'].sum()
    st.subheader("Survived by Passenger Class")
    colors2 = ['#d3a7b4', '#9396cb', '#fdda89']
    ax.pie(survived_by_pclass.values, labels=survived_by_pclass.index, colors=colors2, autopct='%1.1f%%')
    st.write(fig)

st.divider()

st.subheader("Survived by Passenger Class Displayd by Chosen Gender")

selection = st.selectbox(
    "Select Gender:",
    df["Sex"].unique()
)

fig, ax = plt.subplots()
survived_by_pclass_gender = df[df['Sex'] == selection].groupby('Pclass')['Survived'].sum()
ax.pie(survived_by_pclass_gender.values, labels=survived_by_pclass_gender.index, colors=colors2, autopct='%1.1f%%')

st.write(fig)








