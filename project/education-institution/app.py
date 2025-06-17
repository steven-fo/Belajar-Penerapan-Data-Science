import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model and scaler
@st.cache_resource
def load_model():
    try:
        model = joblib.load('project/education-institution/model/random_forest_model.pkl')
        scaler = joblib.load('project/education-institution/model/scaler.pkl')
        return model, scaler
    except FileNotFoundError:
        st.error("Model files not found. Please ensure the model files are in the 'model' directory.")
        return None, None

def predict_dropout(model, scaler, input_data):
    """Predict student dropout probability"""
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction_proba = model.predict_proba(input_scaled)
    prediction = model.predict(input_scaled)
    return prediction[0], prediction_proba[0]

def main():
    # Page configuration
    st.set_page_config(
        page_title="Student Dropout Prediction",
        page_icon="🎓",
        layout="wide"
    )

    # Load model
    model, scaler = load_model()
    
    if model is None or scaler is None:
        st.stop()

    # Title and description
    st.title("🎓 Student Dropout Prediction System")
    st.markdown("---")
    st.markdown("**Predict whether a student is likely to dropout, stay enrolled, or graduate based on their profile and academic performance.**")

    # Create columns for better layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📋 Personal Information")
        
        # Personal data inputs
        marital_status = st.selectbox(
            'Marital Status',
            options=[1, 2, 3, 4, 5, 6],
            format_func=lambda x: {1: 'Single', 2: 'Married', 3: 'Widower', 
                                 4: 'Divorced', 5: 'Facto union', 6: 'Legally separated'}[x]
        )
        
        gender = st.selectbox(
            'Gender',
            options=[1, 0],
            format_func=lambda x: 'Male' if x == 1 else 'Female'
        )
        
        age_at_enrollment = st.number_input(
            'Age at Enrollment',
            min_value=17, max_value=70, value=20, step=1
        )
        
        nacionality = st.number_input(
            'Nationality Code',
            min_value=1, max_value=999, value=1, step=1,
            help="1=Portuguese, 2=German, etc."
        )
        
        international = st.selectbox(
            'International Student',
            options=[0, 1],
            format_func=lambda x: 'Yes' if x == 1 else 'No'
        )

        st.header("🏫 Application & Course Info")
        
        application_mode = st.number_input(
            'Application Mode',
            min_value=1, max_value=99, value=1, step=1,
            help="Method of application (e.g., 1=1st phase, 2=2nd phase)"
        )
        
        application_order = st.number_input(
            'Application Order',
            min_value=0, max_value=9, value=1, step=1,
            help="Order of preference (0=1st choice)"
        )
        
        course = st.number_input(
            'Course Code',
            min_value=1, max_value=9999, value=33, step=1
        )
        
        daytime_evening_attendance = st.selectbox(
            'Class Schedule',
            options=[1, 0],
            format_func=lambda x: 'Daytime' if x == 1 else 'Evening'
        )

    with col2:
        st.header("👨‍👩‍👧‍👦 Family Background")
        
        mothers_qualification = st.number_input(
            "Mother's Qualification",
            min_value=1, max_value=99, value=1, step=1
        )
        
        fathers_qualification = st.number_input(
            "Father's Qualification", 
            min_value=1, max_value=99, value=1, step=1
        )
        
        mothers_occupation = st.number_input(
            "Mother's Occupation",
            min_value=0, max_value=999, value=1, step=1
        )
        
        fathers_occupation = st.number_input(
            "Father's Occupation",
            min_value=0, max_value=999, value=1, step=1
        )

        st.header("🎯 Academic Background")
        
        previous_qualification = st.number_input(
            'Previous Qualification',
            min_value=1, max_value=99, value=1, step=1
        )
        
        previous_qualification_grade = st.number_input(
            'Previous Qualification Grade',
            min_value=0.0, max_value=200.0, value=120.0, step=0.1
        )
        
        admission_grade = st.number_input(
            'Admission Grade',
            min_value=0.0, max_value=200.0, value=120.0, step=0.1
        )

        st.header("💰 Financial & Social Status")
        
        displaced = st.selectbox(
            'Displaced',
            options=[1, 0],
            format_func=lambda x: 'Yes' if x == 1 else 'No'
        )
        
        educational_special_needs = st.selectbox(
            'Educational Special Needs',
            options=[0, 1],
            format_func=lambda x: 'Yes' if x == 1 else 'No'
        )
        
        debtor = st.selectbox(
            'Debtor',
            options=[0, 1],
            format_func=lambda x: 'Yes' if x == 1 else 'No'
        )
        
        tuition_fees_up_to_date = st.selectbox(
            'Tuition Fees Up to Date',
            options=[1, 0],
            format_func=lambda x: 'Yes' if x == 1 else 'No'
        )
        
        scholarship_holder = st.selectbox(
            'Scholarship Holder',
            options=[1, 0],
            format_func=lambda x: 'Yes' if x == 1 else 'No'
        )

    # Academic performance section
    st.markdown("---")
    st.header("📚 Academic Performance")
    
    col3, col4 = st.columns([1, 1])
    
    with col3:
        st.subheader("1st Semester")
        curricular_units_1st_sem_credited = st.number_input(
            'Units Credited (1st Sem)', min_value=0, max_value=30, value=0
        )
        curricular_units_1st_sem_enrolled = st.number_input(
            'Units Enrolled (1st Sem)', min_value=0, max_value=30, value=6
        )
        curricular_units_1st_sem_evaluations = st.number_input(
            'Units Evaluated (1st Sem)', min_value=0, max_value=30, value=6
        )
        curricular_units_1st_sem_approved = st.number_input(
            'Units Approved (1st Sem)', min_value=0, max_value=30, value=6
        )
        curricular_units_1st_sem_grade = st.number_input(
            'Average Grade (1st Sem)', min_value=0.0, max_value=20.0, value=12.0, step=0.1
        )
        curricular_units_1st_sem_without_evaluations = st.number_input(
            'Units Without Evaluations (1st Sem)', min_value=0, max_value=30, value=0
        )

    with col4:
        st.subheader("2nd Semester")
        curricular_units_2nd_sem_credited = st.number_input(
            'Units Credited (2nd Sem)', min_value=0, max_value=30, value=0
        )
        curricular_units_2nd_sem_enrolled = st.number_input(
            'Units Enrolled (2nd Sem)', min_value=0, max_value=30, value=6
        )
        curricular_units_2nd_sem_evaluations = st.number_input(
            'Units Evaluated (2nd Sem)', min_value=0, max_value=30, value=6
        )
        curricular_units_2nd_sem_approved = st.number_input(
            'Units Approved (2nd Sem)', min_value=0, max_value=30, value=6
        )
        curricular_units_2nd_sem_grade = st.number_input(
            'Average Grade (2nd Sem)', min_value=0.0, max_value=20.0, value=12.0, step=0.1
        )
        curricular_units_2nd_sem_without_evaluations = st.number_input(
            'Units Without Evaluations (2nd Sem)', min_value=0, max_value=30, value=0
        )

    # Economic indicators
    st.markdown("---")
    st.header("📊 Economic Indicators")
    
    col5, col6, col7 = st.columns([1, 1, 1])
    
    with col5:
        unemployment_rate = st.number_input(
            'Unemployment Rate (%)', min_value=0.0, max_value=50.0, value=10.0, step=0.1
        )
    
    with col6:
        inflation_rate = st.number_input(
            'Inflation Rate (%)', min_value=-10.0, max_value=20.0, value=1.0, step=0.1
        )
    
    with col7:
        gdp = st.number_input(
            'GDP Growth Rate (%)', min_value=-10.0, max_value=20.0, value=1.0, step=0.1
        )

    # Prediction section
    st.markdown("---")
    st.header("🔮 Prediction")
    
    # Prepare input data
    input_data = [
        marital_status, application_mode, application_order, course,
        daytime_evening_attendance, previous_qualification, previous_qualification_grade,
        nacionality, mothers_qualification, fathers_qualification, mothers_occupation,
        fathers_occupation, admission_grade, displaced, educational_special_needs,
        debtor, tuition_fees_up_to_date, gender, scholarship_holder, age_at_enrollment,
        international, curricular_units_1st_sem_credited, curricular_units_1st_sem_enrolled,
        curricular_units_1st_sem_evaluations, curricular_units_1st_sem_approved,
        curricular_units_1st_sem_grade, curricular_units_1st_sem_without_evaluations,
        curricular_units_2nd_sem_credited, curricular_units_2nd_sem_enrolled,
        curricular_units_2nd_sem_evaluations, curricular_units_2nd_sem_approved,
        curricular_units_2nd_sem_grade, curricular_units_2nd_sem_without_evaluations,
        unemployment_rate, inflation_rate, gdp
    ]

    # Prediction button
    if st.button("🎯 Predict Student Outcome", type="primary", use_container_width=True):
        try:
            prediction, probabilities = predict_dropout(model, scaler, input_data)
            
            # Status mapping
            status_mapping = {
                0: ("Dropout", "🔴", "high"),
                1: ("Enrolled", "🟡", "medium"), 
                2: ("Graduate", "🟢", "low")
            }
            
            status_name, emoji, risk_level = status_mapping[prediction]
            
            # Display results
            st.markdown("### 📋 Prediction Results")
            
            col_result1, col_result2 = st.columns([1, 1])
            
            with col_result1:
                # Different background colors based on prediction
                if prediction == 0:  # Dropout
                    bg_color = "#ffebee"  # Light red
                    border_color = "#f44336"
                elif prediction == 1:  # Enrolled  
                    bg_color = "#fff3e0"  # Light orange
                    border_color = "#ff9800"
                else:  # Graduate
                    bg_color = "#e8f5e8"  # Light green
                    border_color = "#4caf50"
                    
                st.markdown(f"""
                <div style="padding: 20px; border-radius: 10px; background-color: {bg_color}; 
                            border: 2px solid {border_color}; text-align: center; margin: 10px 0;">
                    <h2 style="color: {border_color}; margin: 0;">{emoji} {status_name}</h2>
                    <p style="font-size: 18px; color: #333; margin: 10px 0;">Predicted Outcome</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_result2:
                st.markdown("#### 📊 Confidence Levels")
                
                labels = ["Dropout", "Enrolled", "Graduate"]
                colors = ["#f44336", "#ff9800", "#4caf50"]
                
                for i, (label, prob, color) in enumerate(zip(labels, probabilities, colors)):
                    percentage = prob * 100
                    st.markdown(f"""
                    <div style="margin: 10px 0; padding: 5px; background-color: #fafafa; border-radius: 5px;">
                        <span style="font-weight: bold; color: #333;">{label}:</span>
                        <div style="background-color: #e0e0e0; border-radius: 10px; overflow: hidden; margin: 5px 0;">
                            <div style="background-color: {color}; height: 25px; width: {percentage}%; 
                                        display: flex; align-items: center; justify-content: center; 
                                        color: white; font-weight: bold; transition: width 0.3s ease;">
                                {percentage:.1f}%
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Risk assessment
            if prediction == 0:  # Dropout
                st.error("⚠️ **High Risk**: This student shows signs of potential dropout. Consider intervention strategies.")
            elif prediction == 1:  # Enrolled
                st.warning("⚡ **Medium Risk**: Student likely to continue but monitor progress closely.")
            else:  # Graduate
                st.success("✅ **Low Risk**: Student shows strong indicators for successful graduation.")
                
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

    # Information section
    st.markdown("---")
    st.markdown("""
    ### ℹ️ About This Prediction System
    
    This system uses machine learning to predict student outcomes based on:
    - **Personal demographics** and background information
    - **Academic performance** in first and second semesters  
    - **Socio-economic factors** and family background
    - **Financial status** and support systems
    - **Macro-economic indicators** affecting education
    
    **Note**: This is a prediction tool to assist in identifying at-risk students for early intervention. 
    It should be used alongside human judgment and other assessment methods.
    """)

if __name__ == "__main__":
    main()