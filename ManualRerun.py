import streamlit as st

st.title("Counter Example with Immediate Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    #previously we only had increment, which did not provide updated counter because after rerun the
    # counter value is 0 and then counter is incremented to 1
    # To avoid this we need to do a manual re-run
    #st.session_state.count += 1

    st.session_state.count += 1
    st.rerun()  ## This is example for manual re-run

st.write(f"Current Count: {st.session_state.count}")

if st.button("Increment and Update Immediately"):
    increment_and_rerun()