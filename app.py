import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Jaipur House Price Estimator")
st.title("🏠 Jaipur House Price Estimator")
st.write("Sample Prototype for Local Property Dealer - Raja Park, C-Scheme, Vaishali Nagar")

np.random.seed(42)
df = pd.DataFrame({
    'Locality': np.random.choice(['Vaishali Nagar','Mansarovar','Jagatpura','C-Scheme','Raja Park','Malviya Nagar'], 500),
    'Avg_Area_Income_LPA': np.random.uniform(5, 20, 500),
    'Property_Age_Years': np.random.uniform(0, 20, 500),
    'Total_Rooms': np.random.randint(2, 10, 500),
    'Bedrooms_BHK': np.random.randint(1, 5, 500),
    'Area_Population_Density': np.random.uniform(3000, 9000, 500),
})
df['Price_Lakhs'] = df['Avg_Area_Income_LPA']*4 + df['Total_Rooms']*5 + df['Bedrooms_BHK']*8 - df['Property_Age_Years']*0.5 + np.random.normal(0,5,500)

locality = st.selectbox("Select Locality (Jaipur)", df['Locality'].unique())
col1, col2 = st.columns(2)
with col1:
    income = st.slider("Avg Area Income (LPA)", 4.0, 25.0, 12.0)
    rooms = st.slider("Total Rooms", 2, 12, 6)
    bhk = st.slider("Bedrooms (BHK)", 1, 5, 3)
with col2:
    age = st.slider("Property Age (Years)", 0.0, 30.0, 5.0)
    pop = st.slider("Population Density", 3000, 10000, 6000)

X = df[['Avg_Area_Income_LPA', 'Property_Age_Years', 'Total_Rooms', 'Bedrooms_BHK', 'Area_Population_Density']]
y = df['Price_Lakhs']
model = LinearRegression()
model.fit(X, y)

if st.button("Estimate Price in Lakhs", type="primary"):
    price = model.predict([[income, age, rooms, bhk, pop]])[0]
    st.success(f"Estimated Price in {locality}: Rs {price:.2f} Lakhs")
    st.balloons()
