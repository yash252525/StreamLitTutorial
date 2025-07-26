import streamlit as st

st.sidebar.title("This is a sidebar")
st.sidebar.write("You can place elements like this")
sidebar_input = st.sidebar.text_input("Enter Something in the sidebar")


tab1,tab2,tab3 = st.tabs(['Tab 1','Tab 2','Tab 3'])

with tab1:
    st.write("You're in Tab 1")

with tab2:
    st.write("You're in Tab 2")

with tab3:
    st.write("You're in Tab 3")


st.divider()

# Column Layout
col1,col2,col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")
with col3:
    st.header("Column 3")
    st.write("Content for column 3")

st.divider()

# Container
with st.container(border=True):
    st.write("This is container content")



# Empty Placeholder
placehorder = st.empty()
placehorder.write("This is an empty placeholder, useful for dynamic content.")

if st.button("update Placeholder"):
    placehorder.write("The content of this placeholder has been updated")

if st.button("Reset"):
    placehorder.write("This is an empty placeholder, useful for dynamic content.")



# Expander
with st.expander("Expand for more details"):
    st.write("This is additional information that is defined by default.")

# Multiple lines
st.text("This is example\nMultiple lines writing\nAnother line")


# Popover (Hover)
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover on hover.")

if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")