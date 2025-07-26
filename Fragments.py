import streamlit as st


# Fragments are a way to rerun only certain portions of your
# user interface and better organize or separate out your code
# Better provisioning, organize and code seperation

st.title("My Awesome app")


# Only re-runs the following fragment
@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[0].text_area("Enter Text")
    # st.rerun(scope="app") --> this will re-run entire application
    # st.rerun(scope="fragment") --> By default property of fragment
    # return statement will not work in fragments

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload Image")
    new_cols[2].selectbox("Choose Option", ["Option 1","Option 2","Option 3"])
    new_cols[3].slider("Select Filter",0,100,50)
    new_cols[4].text_input("Enter Text")

toggle_and_text()
# Un fragmented parts of code will re-run entire application
# This will also run both of the above functions
cols = st.columns(2)
cols[0].selectbox("Select",[1,2,3],None)
cols[1].button("Update")
filter_and_file()