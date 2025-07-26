import os.path

import streamlit as st
import time
from datetime import datetime

from streamlit import session_state


# As we re-run each time caching becomes a important parameter to set for our application
# When we need to reach out to an API it will take a lot of time
# So to avoid these inconvenience we can implement cache within Streamlit

@st.cache_data(ttl=60)
def fetch_data():

    time.sleep(3)
    now = datetime.now()
    return{f"data":"This is cached data! {now}"}


st.write("Fetching data...")
data = fetch_data()
st.write(data)

# Cache resource example
file_path = "example.txt"
@st.cache_resource
def get_file_handler():
    file = open(file_path, "a+")
    return file

file_handler = get_file_handler()

if "counter" not in st.session_state:
   st.session_state.counter = 0

if st.button("Write to File"):
    st.session_state.counter += 1
    file_handler.write(f"New line of text {st.session_state.counter}\n")
    file_handler.flush()
    st.success("Wrote a new line to the file")

if st.button("Read File"):
    if os.path.exists(file_path):
        file_handler.seek(0)
        content = file_handler.read()
        st.text(content)
    else:
        st.warning("File does not exists !")

st.button("Close File", on_click=file_handler.close)


def delete_file():
    try:
        file_handler.close()
    except:
        pass
    if os.path.exists(file_path):
        os.remove(file_path)
        st.success("File Deleted")
    else:
        st.warning("File does not exists !")

st.button("Delete File",on_click=delete_file)


