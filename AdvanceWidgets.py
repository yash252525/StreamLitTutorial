import streamlit as st


# You will see error: streamlit.errors.StreamlitDuplicateElementId
# streamlit.errors.StreamlitDuplicateElementId: There are multiple button elements with the same auto-generated ID. When this element is created, it is assigned an internal ID based on the element type and provided parameters. Multiple elements with the same type and parameters will cause this error.
# To fix this error, please pass a unique key argument to the button element.
# each text, input is given an ElementID (Auto generated ID)
# To fix this key conflict we need to manually pass a key to one of the button
st.button("OK")
st.button("OK",key= "btn2")

if "slider" not in st.session_state:
    st.session_state.slider = 25


min_value = st.slider("Set min value",0,50,25) # min,max,default
# If you change min_value it will change min_value for slider_value as well because the session is updated
# To avoid this we can use st.session_state
st.session_state.slider = st.slider("Slider",min_value,100,st.session_state.slider)

# Example 2
# When we check the text box and put user input and then untick
# We tick again and the user_input disappears, this is the case because when we do not render display the values are lost
# To avoid this
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show input Field", value=st.session_state.checkbox,on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input("Enter Something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input","")

st.write(f"User Input: {user_input}")

