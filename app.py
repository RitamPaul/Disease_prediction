import streamlit as st

if 'page' not in st.session_state:
    st.session_state['page']='diabetes'

def diabetes_page():
    st.title("**Diabetes Prediction using ML**")

    left, center, right = st.columns(3, gap='small', vertical_alignment='top', border=False)

    # all input fields
    with left:
        pregnancy_count = st.number_input(
            label='**Number of Pregnancies**',
            min_value=0,
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
        type='primary',
    )
    if(btn):
        st.progress(50, text=f'**{50}%**')
        st.success(f'''
            **Nice 👍🏻** \n
            pregnancy count:- {str(pregnancy_count).center(10,'-')}, glocose level:- {str(glucose_level).center(10,'-')}, blood pressure:- {str(blood_pressure).center(10,'-')},\n
            skin thickness:- {str(skin_thickness).center(10,'-')}, insulin level:- {str(insulin_level).center(10,'-')}, bmi value:- {str(bmi).center(10,'-')},\n
            diabetes predigree function value:- {str(diabetes_pedigree).center(10,'-')}, age:- {str(age).center(10,'-')}
        ''')
        st.balloons()
        st.toast('**Good job!**', icon='🤩')

def heart_disease_page():
    st.title('**Heart Disease Prediction using ML**')

def parkinsons_page():
    st.title('**Parkinsons Prediction using ML**')

if(st.session_state['page']=='diabetes'):
    diabetes_page()
elif(st.session_state['page']=='heart_disease'):
    heart_disease_page()
else:
    parkinsons_page()

with st.sidebar:
    with st.container(border=True):
        st.title('**:material/apartment: Prediction of Disease Outbreaks System**')

        btn1 = st.button(
            label='**Diabetes Prediction**',
            type='primary' if st.session_state['page']=='diabetes' else 'secondary',
            icon=':material/vital_signs:',
            use_container_width=True,
        )
        btn2 = st.button(
            label='**Heart Disease Prediction**',
            type='primary' if st.session_state['page']=='heart_disease' else 'secondary',
            icon=':material/favorite:',
            use_container_width=True,
        )
        btn3 = st.button(
            label='**Parkinsons Prediction**',
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