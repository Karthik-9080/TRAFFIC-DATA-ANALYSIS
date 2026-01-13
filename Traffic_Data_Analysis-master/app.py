import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_cleaning import clean_data
from src.model import train_model

st.set_page_config(
    page_title="Traffic Accident Analysis & Severity Prediction",
    layout="wide"
)

st.title("Traffic Accident Analysis & Severity Prediction")

st.write(
    "This application analyzes Indian traffic accident data, "
    "visualizes key patterns, and predicts accident severity "
    "using a machine learning model."
)

@st.cache_data
def load_data():
    return pd.read_csv("data/india_traffic_accidents.csv")

data = load_data()

st.subheader("Dataset Preview")
st.dataframe(data.head())

data = clean_data(data)

st.subheader("Exploratory Data Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Accident Severity Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(x="Severity", data=data, ax=ax1)
    ax1.set_xlabel("Severity (1 = Low, 4 = High)")
    ax1.set_ylabel("Number of Accidents")
    st.pyplot(fig1)

with col2:
    st.markdown("Accidents by Hour of Day")
    fig2, ax2 = plt.subplots()
    sns.countplot(x="Hour", data=data, ax=ax2)
    ax2.set_xlabel("Hour of Day")
    ax2.set_ylabel("Accident Count")
    st.pyplot(fig2)

col3, col4 = st.columns(2)
with col3:
    st.markdown("Accidents by Weather Condition")
    fig3, ax3 = plt.subplots()
    sns.countplot(
        x="Weather",
        data=data,
        order=data["Weather"].value_counts().index,
        ax=ax3
    )
    ax3.set_xlabel("Weather Condition")
    ax3.set_ylabel("Accident Count")
    plt.xticks(rotation=45)
    st.pyplot(fig3)

with col4:
    st.markdown("Weekday vs Weekend Accidents")
    fig4, ax4 = plt.subplots()
    sns.countplot(x="Is_Weekend", data=data, ax=ax4)
    ax4.set_xticklabels(["Weekday", "Weekend"])
    ax4.set_xlabel("Day Type")
    ax4.set_ylabel("Accident Count")
    st.pyplot(fig4)

st.subheader("Machine Learning Model")

accuracy = train_model(data)

st.success("Model trained successfully!")
st.metric(label="Model Accuracy", value=f"{accuracy:.2f}")
