import streamlit as st
import numpy as np
import pickle

st.set_page_config(
    page_title='Prediction of Disease Outbreaks',
    page_icon=":male-doctor:",
    layout='wide',
    initial_sidebar_state='expanded'
)

if 'diabetesModel' not in st.session_state:
    with open('models\Diabetes\DecisionTree_notUndersampled.pkl', 'rb') as f:
        st.session_state['diabetesModel'] = pickle.load(f)

if 'diabetesScaler' not in st.session_state:
    with open('models\Diabetes\MinMaxScaler_notUndersampled.pkl', 'rb') as f:
        st.session_state['diabetesScaler'] = pickle.load(f)

if 'heartModel' not in st.session_state:
    with open('models\HeartDisease\KNN_beforeUndersampled.pkl', 'rb') as f:
        st.session_state['heartModel'] = pickle.load(f)

if 'heartScaler' not in st.session_state:
    with open('models\HeartDisease\StandardScaler_beforeUndersampled.pkl', 'rb') as f:
        st.session_state['heartScaler'] = pickle.load(f)

if 'parkinsonsModel' not in st.session_state:
    with open('models\Parkinsons\RandomForest_Undersampled.pkl', 'rb') as f:
        st.session_state['parkinsonsModel'] = pickle.load(f)

if 'parkinsonsScaler' not in st.session_state:
    with open('models\Parkinsons\MinMaxScaler_Undersampled.pkl', 'rb') as f:
        st.session_state['parkinsonsScaler'] = pickle.load(f)

if 'page' not in st.session_state:
    st.session_state['page']='diabetes'

def diabetes_page():
    st.title("**Diabetes Prediction using ML**")

    left, center, right = st.columns(3, gap='small', vertical_alignment='top', border=False)

    # all input fields
    with left:
        pregnancy_count = st.number_input(
            label='**Number of Pregnancies**',
            min_value=0.0,
            placeholder='Enter pregnancy count',
        )
        skin_thickness = st.number_input(
            label='**Skin Thickness value**',
            min_value=0.0,
            step=0.001,
            format='%0.3f',
            placeholder='Enter skin thickness',        
        )
        diabetes_pedigree = st.number_input(
            label='**Diabetes Pedigree function value**',
            min_value=0.0,
            step=0.001,
            format='%0.3f',
            placeholder='Enter diabetes pedigree function value',
        )
    with center:
        glucose_level = st.number_input(
            label='**Glucose Level**',
            min_value=0.0,
            step=0.001,
            format='%0.3f',
            placeholder='Enter glucose level',
        )
        insulin_level = st.number_input(
            label='**Insulin Level**',
            min_value=0.0,
            step=0.001,
            format='%0.3f',
            placeholder='Enter insulin level',
        )
        age = st.number_input(
            label='**Age of the Person**',
            min_value=0,
            placeholder='Enter age of the person',
        )
    with right:
        blood_pressure = st.number_input(
            label='**Blood Pressure value**',
            min_value=0.0,
            step=0.001,
            format='%0.3f',
            placeholder='Enter blood pressure',
        )
        bmi = st.number_input(
            label='**BMI value**',
            min_value=0.0,
            step=0.1,
            format='%0.1f',
            placeholder='Enter BMI value',
        )

    # submit button
    btn = st.button(
        label='**Diabetes Test Result**',
        type='secondary',
    )
    if(btn):
        vars = [pregnancy_count, glucose_level, blood_pressure, skin_thickness, insulin_level, bmi, diabetes_pedigree, age]
        user_input = [float(x) for x in vars]
        user_input_array = np.array(user_input).reshape(1, -1)
        model = st.session_state['diabetesModel']
        scaler = st.session_state['diabetesScaler']
        scaled_input = scaler.transform(user_input_array)
        prediction = model.predict(scaled_input)
        result = prediction[0]
        if(result):
            st.success('**Result : You are Diabetic**')
        else:
            st.success('**Result : You are not Diabetic**')

def heart_disease_page():
    st.title('**Heart Disease Prediction using ML**')

    left, center, right = st.columns(3, gap='small', vertical_alignment='top', border=False)

    # all input fields
    with left:
        age = st.number_input(
            label='**Age**',
            min_value=0,
            placeholder='Enter your age',
        )
        rbp = st.number_input(
            label='**Resting Blood Pressure**',
            min_value=0.0,
            placeholder='Enter your resting blood pressure',
        )
        recg = st.number_input(
            label='**Resting Electrocardiographic results**',
            min_value=0.0,
            placeholder='Enter your resting ecg value',
        )
        stdep = st.number_input(
            label='**ST depression induced by exercise**',
            min_value=0.0,
            step=0.1,
            format='%0.1f',
            placeholder='Enter your st depression value',
        )
        thal = st.number_input(
            label='**Thal : 0=Normal; 1=Fixed defect; 2=Reversable defect**',
            min_value=0,
            placeholder='Enter age of the person',
        )
    with center:
        sex = st.number_input(
            label='**Sex**',
            min_value=0,
            placeholder='Enter your gender',
        )
        schol = st.number_input(
            label='**Serum Cholestrol in mg/dl**',
            min_value=0.0,
            placeholder='Enter your serum cholestrol level',
        )
        maxhrate = st.number_input(
            label='**Maximum Heart rate achieved**',
            min_value=0,
            placeholder='Enter your max heart rate',
        )
        slope = st.number_input(
            label='**Slope of the peak exercise ST segment**',
            min_value=0.0,
            placeholder='Enter the slope value',
        )
    with right:
        cpain = st.number_input(
            label='**Chest Pain types**',
            min_value=0,
            placeholder='Enter your ches pain type',
        )
        fbs = st.number_input(
            label='**Fasting Blood Sugar > 120 md/dl**',
            min_value=0.0,
            placeholder='Enter your fasting blood sugar level',
        )
        exang = st.number_input(
            label='**Exercise induced Angina**',
            min_value=0.0,
            placeholder='Enter your exang value',
        )
        majorvessels = st.number_input(
            label='**Major vessels colored by fluoroscopy**',
            min_value=0.0,
            placeholder='Enter your major vessels',
        )

    # submit button
    btn = st.button(
        label='**Heart Disease Test Result**',
        type='secondary',
    )
    if(btn):
        vars = [age, sex, cpain, rbp, schol, fbs, recg, maxhrate, exang, stdep, slope, majorvessels, thal]
        user_input = [float(x) for x in vars]
        user_input_array = np.array(user_input).reshape(1, -1)
        model = st.session_state['heartModel']
        scaler = st.session_state['heartScaler']
        scaled_input = scaler.transform(user_input_array)
        prediction = model.predict(scaled_input)
        result = prediction[0]
        if(result):
            st.success('**Result : You have heart Disease**')
        else:
            st.success('**Result : You don\'t have Heart Disease**')

def parkinsons_page():
    st.title('**Parkinsons Disease Prediction using ML**')

    one, two, three, four, five = st.columns(5, gap='small', vertical_alignment='top', border=False)

    # all input fields
    with one:
        mdvp11 = st.text_input(label='**MDVP (Hz)**',placeholder='MDVP : Fo(Hz)')
        mdvp21 = st.text_input(label='**MDVP**',placeholder='MDVP : RAP')
        shimmer31 = st.text_input(label='**Shimmer**',placeholder='Shimmer : APQ3')
        hnr = st.text_input(label='**HNR**',placeholder='HNR')
        d2 = st.text_input(label='**D2**',placeholder='D2')
    with two:
        mdvp12 = st.text_input(label='**MDVP (Hz)**',placeholder='MDVP : Fhi(Hz)')
        mdvp22 = st.text_input(label='**MDVP**',placeholder='MDVP : PPQ')
        shimmer32 = st.text_input(label='**Shimmer**',placeholder='Shimmer : APQ5')
        rpde = st.text_input(label='**RPDE**',placeholder='RPDE')
        ppe = st.text_input(label='**PPE**',placeholder='PPE')
    with three:
        mdvp13 = st.text_input(label='**MDVP (Hz)**',placeholder='MDVP : Flo(Hz)')
        jitter = st.text_input(label='**Jitter**',placeholder='Jitter : DDP')
        mdvp33 = st.text_input(label='**MDVP**',placeholder='MDVP : APQ')
        dfa = st.text_input(label='**DFA**',placeholder='DFA')
    with four:
        mdvp14 = st.text_input(label='**MDVP (%)**',placeholder='MDVP : Jitter(%)')
        mdvp24 = st.text_input(label='**MDVP**',placeholder='MDVP : Shimmer')
        shimmer34 = st.text_input(label='**Shimmer**',placeholder='Shimmer : DDA')
        spread1 = st.text_input(label='**spread1**',placeholder='spread1')
    with five:
        mdvp15 = st.text_input(label='**MDVP (Abs)**',placeholder='MDVP : Jitter(Abs)')
        mdvp25 = st.text_input(label='**MDVP (dB)**',placeholder='MDVP : Shimmer(dB)')
        nhr = st.text_input(label='**NHR**',placeholder='NHR')
        spread2 = st.text_input(label='**spread2**',placeholder='spread2')
    
    # submit button
    btn = st.button(
        label='**Parkinson\'s Test Result**',
        type='secondary',
    )
    if(btn):
        vars = [mdvp11, mdvp12, mdvp13, mdvp14, mdvp15, mdvp21, mdvp22, jitter, mdvp24, mdvp25, shimmer31, shimmer32, mdvp33, shimmer34, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
        user_input = [eval(x) for x in vars]
        user_input = [float(x) for x in user_input]
        user_input_array = np.array(user_input).reshape(1, -1)
        model = st.session_state['parkinsonsModel']
        scaler = st.session_state['parkinsonsScaler']
        scaled_input = scaler.transform(user_input_array)
        prediction = model.predict(scaled_input)
        result = prediction[0]
        if(result):
            st.success('**Result : You have Parkinson\'s Disease**')
        else:
            st.success('**Result : You don\'t have Parkinson\'s Disease**')

if(st.session_state['page']=='diabetes'):
    diabetes_page()
elif(st.session_state['page']=='heart_disease'):
    heart_disease_page()
else:
    parkinsons_page()

with st.sidebar:
    with st.container(border=True):
        st.title('**:material/apartment: Prediction of Disease Outbreaks System**')
        st.divider()

        btn1 = st.button(
            label='**Diabetes Prediction**' if st.session_state['page']=='diabetes' else 'Diabetes Prediction',
            type='primary' if st.session_state['page']=='diabetes' else 'secondary',
            icon=':material/vital_signs:',
            use_container_width=True,
        )
        btn2 = st.button(
            label='**Heart Disease Prediction**' if st.session_state['page']=='heart_disease' else 'Heart Disease Prediction',
            type='primary' if st.session_state['page']=='heart_disease' else 'secondary',
            icon=':material/favorite:',
            use_container_width=True,
        )
        btn3 = st.button(
            label='**Parkinsons Prediction**' if st.session_state['page']=='parkinson' else 'Parkinsons Prediction',
            type='primary' if st.session_state['page']=='parkinson' else 'secondary',
            icon=':material/person:',
            use_container_width=True,
        )

        if(btn1):
            st.session_state['page']='diabetes'
            st.rerun()
        if(btn2):
            st.session_state['page']='heart_disease'
            st.rerun()
        if(btn3):
            st.session_state['page']='parkinson'
            st.rerun()