🏠 **Jaipur House Price Estimator – Live Project**

Live Demo: https://house-price-prediction-machine-learning-project.streamlit.app

📍Problem Statement

Local property dealers in Jaipur—such as those serving Raja Park, C-Scheme, Vaishali Nagar, and Mansarovar—often need to provide quick property price estimates to clients.

 I developed a localized house price prediction prototype using Jaipur-specific, privacy-safe sample data.

The application uses 5 key property and demographic inputs to estimate the property price in Indian Lakhs.

✨ Features
Locality Selection: C-Scheme, Vaishali Nagar, Mansarovar, Jagatpura, Raja Park, and Malviya Nagar
5 Smart Inputs:
Average Area Income (LPA)
Property Age
Total Rooms
BHK
Population Density
Instant Prediction: Linear Regression model generates a price estimate within seconds
Interactive UI: Built using Streamlit
Deployment: Deployed on Streamlit Cloud and available online
🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-learn
Linear Regression
Streamlit
Streamlit Cloud
🔒 Data Privacy Note

The original dealer/property data was covered under a Non-Disclosure Agreement (NDA). Therefore, I created a privacy-safe dummy dataset designed to represent realistic Jaipur market patterns.

This project should therefore be considered a prototype for demonstrating machine learning and application development, rather than an official real-estate valuation tool.

🚀 How to Run Locally
pip install -r requirements.txt
streamlit run app.py
