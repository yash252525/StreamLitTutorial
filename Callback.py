import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}


def go_to_step_2(name):
    # Callback runs before any other code on the next run
        st.session_state.info["name"] = name
        st.session_state.step = 2


def go_to_step_1():
    st.session_state.step = 1



if st.session_state.step == 1:
    st.header("Part 1: Info")

    name = st.text_input("Name",value=st.session_state.info.get("name",""))

    st.button("Next",on_click=go_to_step_2,args=(name,)) # you need to add "," after name so python understands that it is a tuple
        # st.session_state.info["name"] = name
        # st.session_state.step = 2
        # Now you will observe that when you cliock next you will have to click it twice
        # The reason is that when we click the button we will re-run the application first time and the step value will set to 2 and
        # then we will have to run it again to execute the value 2
        # To make this feasible we can change elif to if on line 22

# elif st.session_state.step ==2:
# Now after changing elif to if when we re-run the session state will already be 2 and we will enter the below loop
# Now removing this if comes with a challenge
# When we complete step 1 and press next we will see step 1 and 2 together
# to avoid this we will create a function using callback copying line 20,21 and changing line 19:  if st.button("Next"): to st.button
if st.session_state.step ==2:
    st.header("Part 2: Review")

    st.subheader("Please Review This...")
    st.write(f"**Name**: {st.session_state.info.get("name","")}")

    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}

    # Same is the case for back, so here we will create a call back function
    st.button("Back",on_click=go_to_step_1)
        # st.session_state.step = 1

