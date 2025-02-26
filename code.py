import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://Cluster0:123@cluster0.wi9dl.mongodb.net/"
client = MongoClient(MONGO_URI)

# Select Database and Collection
db = client["university"]
collection = db["students"]

# Streamlit App
st.title("📚 Student Database Viewer")

# Fetch Data
students = list(collection.find({}, {"_id": 0}))  # Exclude ObjectId

if students:
    df = pd.DataFrame(students)
    st.dataframe(df)

    # 📊 Bar Chart: Age Distribution
    st.subheader("📊 Age Distribution")
    fig, ax = plt.subplots()
    df["age"].value_counts().sort_index().plot(kind="bar", ax=ax, color="skyblue")
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Students")
    st.pyplot(fig)

    # 🏫 Pie Chart: Course Distribution
    st.subheader("🏫 Course Distribution")
    fig, ax = plt.subplots()
    df["course"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax, startangle=90, colors=["lightcoral", "lightblue", "lightgreen"])
    st.pyplot(fig)

else:
    st.warning("No student records found!")
