import streamlit as st

# session state is something that we can use to store values within th same user session
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")
    # for eg if you print counter value on line 6, you see the counter value 3 and for line counter value will be 4.
    # The reason for it is the streamlit flow, it re-runs the appln, keeps the value at line 6 and then increments value at line 8, updates at line 9
    # Due to this process make sure to print only once the changes are executed

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter value: {st.session_state.counter}")




# counter = 0
#
# st.write(f"Counter Value: {counter}")
#
# if st.button("Increment Counter"):
#     # But when we press button for increment it goes to 1 but not further because we re-run the program every time so the value stays same
#     counter += 1
#     st.write(f"Counter incremented to {counter}")
# else:
#     # initial start will print this as button is on false value
#     st.write(f"Counter stays at {counter}")
# # Hence we can use session state