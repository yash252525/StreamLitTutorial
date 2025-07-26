import streamlit as st




# Streamlit has hot re-run
# We re-run the entire python file (for refreshes)


# This function is used to add anything to a web app
# st.write("Hello world")
# st.write({"key": "value"})
# st.write(123)

# 3+4
#
#
# # change betn True and False
# "Hello World" if False else "bye"

#Understanding button
# pressed = st.button("Press me") # Current status before click is False, once we click the value becomes True
# print("First:", pressed)
# # if we refresh it becomes False


# Example for re-run
# Consider we have two buttons, both are false at the initial stage.
# 1. We click on button 1 , it will be True and button 2 will be False.
# 2. If we then click on button 2, it will change to True but button 1 value will become false which is because the file re runs
pressed = st.button("Press me") # Current status before click is False, once we click the value becomes True
print("First:", pressed)
# if we refresh it becomes False


pressed2 = st.button("Second Button")
print("Second:", pressed2)