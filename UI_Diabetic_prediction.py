import streamlit as st
import joblib

# Load the trained model
model = joblib.load('Diabetes_Prediction_Model.pkl')

# Set the page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="wide"
)

# Add custom CSS to style widgets and buttons
st.markdown(
    """
    <style>
    .stSelectbox, .stNumberInput {
        border: 2px solid #2B579A !important;
        border-radius: 5px !important;
        padding: 10px !important;
    }
    .stButton > button {
        background-color: #2B579A !important;
        color: white !important;
        border-radius: 5px !important;
        padding: 10px 20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a sidebar for navigation
st.sidebar.title("Diabetes Prediction App")
st.sidebar.image(
    "diabetic_logo.png", caption="Empowering Health Decisions", use_container_width=True
)

# Main page title
st.markdown(
    """
    <h1 style="text-align: center; color: #2B579A;">Diabetes Prediction App 👨🏻‍⚕️</h1>
    <p style="text-align: center; font-size: 18px; color: #555555;">
        <ul style="list-style-type: none; padding: 0;">
            <li>🔹 Diabetes affects millions worldwide but can be managed effectively.</li>
            <li>🔹 Early detection and timely intervention are critical for prevention.</li>
            <li>🔹 Lifestyle choices play a significant role in diabetes management.</li>
            <li>🔹 Understand your risk factors and take proactive steps for better health.</li>
            <li>🔹 Empower yourself with knowledge and tools for diabetes care.</li>
        </ul>
    </p>
    """,
    unsafe_allow_html=True
)

# Add an image or banner to fill the gap
st.markdown(
    """
    <div style="text-align: center; font-size: 16px; color: #2B579A;">
        <p><strong>"Stay informed, stay healthy: Knowledge is the best prevention."</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)


# Reset functionality
if "reset" not in st.session_state:
    st.session_state.reset = False

# Reset values logic
def reset_values():
    st.session_state.gender = "Female"
    st.session_state.age = 0
    st.session_state.hypertension = "No"
    st.session_state.heart_disease = "No"
    st.session_state.smoking_history = "Never Smoked"
    st.session_state.bmi = 0.0
    st.session_state.hba1c = 0.0
    st.session_state.blood_glucose = 0

if st.session_state.reset:
    reset_values()
    st.session_state.reset = False

# Create a form layout for user inputs
with st.form("diabetes_form"):
    st.subheader("Enter Your Details")
    
    # Create two columns for aligning widgets
    col1, col2 = st.columns(2)
    
    # Widgets in the first column
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"], key="gender")
        age = st.number_input("Age", min_value=0, max_value=120, step=1, key="age")
        hypertension = st.selectbox("Do you have Hypertension?", ["No", "Yes"], key="hypertension")
        heart_disease = st.selectbox("Do you have Heart Disease?", ["No", "Yes"], key="heart_disease")
    
    # Widgets in the second column
    with col2:
        smoking_history = st.selectbox(
            "Smoking History",
            ["Never Smoked", "Former Smoker", "Current Smoker", "Occasional", "Unknown"],
            key="smoking_history"
        )
        bmi = st.number_input("Enter your BMI (e.g., 25.4)", format="%.1f", key="bmi")
        HbA1c_level = st.number_input("Enter your HbA1c Level (e.g., 6.5)", format="%.1f", key="hba1c")
        blood_glucose_level = st.number_input("Enter your Blood Glucose Level (e.g., 120)", step=1, key="blood_glucose")
    
    # Buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        predict_button = st.form_submit_button("Predict")
    with col2:
        reset_button = st.form_submit_button("Reset")

# Handle reset button
if reset_button:
    st.session_state.reset = True

# When the Predict button is pressed
if predict_button:
    # Encode inputs
    gender_encoded = 0 if st.session_state.gender == "Female" else 1
    hypertension_encoded = 0 if st.session_state.hypertension == "No" else 1
    heart_disease_encoded = 0 if st.session_state.heart_disease == "No" else 1
    smoking_history_encoded = {
        "Never Smoked": 0,
        "Former Smoker": 1,
        "Current Smoker": 2,
        "Occasional": 3,
        "Unknown": 4,
    }[st.session_state.smoking_history]

    # Prepare the input for the model
    input_data = [
        [
            gender_encoded,
            st.session_state.age,
            hypertension_encoded,
            heart_disease_encoded,
            smoking_history_encoded,
            st.session_state.bmi,
            st.session_state.hba1c,
            st.session_state.blood_glucose,
        ]
    ]

    # Make the prediction
    try:
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1]  # Probability of diabetes

        # Display results
        if prediction[0] == 1:
            st.markdown(
                f"""
                <div style="background-color: #FFD1D1; padding: 10px; border-radius: 5px; border: 1px solid #FF0000;">
                    <h3 style="text-align: center; color: #FF0000;">High Risk of Diabetes</h3>
                    <h4 style="text-align: center; color: #FF0000;">Kindly consult a doctor as soon as possible</h4>
                </div>
                """,
                unsafe_allow_html=True,
            ) 
        else:
            st.markdown(
                f"""
                <div style="background-color: #DFF6DD; padding: 10px; border-radius: 5px; border: 1px solid #4CAF50;">
                    <h3 style="text-align: center; color: #388E3C;">Low Risk of Diabetes</h3>
                    <h4 style="text-align: center; color: #388E3C;">You are healthy</h4>
                </div>
                """,
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.sidebar.markdown(
    """
    ---
    **"Diabetes is not a curse, it's a challenge. Face it with strength, manage it with care."**  
    ---
    """
)
