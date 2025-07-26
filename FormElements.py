import streamlit as st
from datetime import datetime
st.title("User Information Form")

form_values = {
    "name": None,
    "age": None,
    "height": None,
    "gender": None,
    "dob": None
    #"location"  : None
}

min_date = datetime(1930,1,1)
max_date = datetime.now()
# key for unique identifier
# we use "with" so the form does not re run after every edit and tackle data loss
# Once we submit the form, the application re-runs
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your Name")
    form_values["age"] = st.number_input("Enter your Age")
    form_values["height"] = st.number_input("Enter your Height")
    form_values["gender"] = st.selectbox("Gender",["Male","Female"])
    form_values["dob"] = st.date_input("Enter your DoB",min_value=min_date,max_value=max_date)
    #form_values["location"] = st.number_input("Enter your Age")


    # On the first instance the submit button is false, the application re-runs and then makes submit_button to true and then we continue
    submit_button = st.form_submit_button(label="Submit")
    print("Initial submit")
    if submit_button:
        print("in loop after submit")
        if not all(form_values.values()):
            st.warning("Please fill in all the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key,value) in form_values.items():
                st.write(f"{key}: {value}")
