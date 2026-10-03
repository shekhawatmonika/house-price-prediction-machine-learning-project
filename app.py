import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Jaipur House Price Estimator", layout="centered")

st.title("🏠 Jaipur House Price Estimator")
st.write("Sample Prototype for Local Property Dealer - Raja Park, C-Scheme, Vaishali Nagar")

@st.cache_data
def load_data():
    return pd.read_csv('jaipur_housing_data.csv')

df = load_data()

locality_list = df['Locality'].unique() if 'Locality' in df.columns else ["Vaishali Nagar", "Mansarovar", "Jagatpura", "C-Scheme", "Raja Park", "Malviya Nagar", "Tonk Road"]
selected_locality = st.selectbox("Select Locality (Jaipur)", locality_list)

st.divider()
st.subheader("Property Details")

col1, col2 = st.columns(2)
with col1:
    income = st.slider("Avg Area Income (LPA)", 4.0, 25.0, 12.0)
    rooms = st.slider("Total Rooms", 2, 12, 6)
    bhk = st.slider("Bedrooms (BHK)", 1, 5, 3)
with col2:
    age = st.slider("Property Age (Years)", 0.0, 30.0, 5.0)
    pop = st.slider("Population Density", 3000, 10000, 6000)

# Train model fresh with 5 features
X = df[['Avg_Area_Income_LPA', 'Property_Age_Years', 'Total_Rooms', 'Bedrooms_BHK', 'Area_Population_Density']]
y = df['Price_Lakhs']

model = LinearRegression()
model.fit(X, y)

if st.button("Estimate Price in Lakhs", type="primary"):
    input_data = [[income, age, rooms, bhk, pop]]
    price = model.predict(input_data)[0]
    st.success(f"**Estimated Price in {selected_locality}: ₹ {price:.2f} Lakhs**")
    st.balloons()
    st.write(f"For Plot No. {rooms*45+10}, {selected_locality}, Jaipur")