import requestfunctions.getmethods as getmethods
import requests
from modules.nav import SideBarLinks
import streamlit as st
import logging
import json

logger = logging.getLogger(__name__)

st.set_page_config(layout="wide")

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

# create a 2 column layout
col1, col2 = st.columns(2)

# add one number input for variable 1 into column 1
with col1:
    st.title("New Note")

# add another number input for variable 2 into column 2
with col2:
    title = st.text_input("Enter Title")

content = st.text_area(label="Enter Description", value="", height=None, max_chars=None,
                       key=None, help=None, on_change=None, args=None, kwargs=None,
                       placeholder=None, disabled=False, label_visibility="visible")

col1, col2 = st.columns(2, vertical_alignment="bottom")
response = getmethods.getPoliticians(st.session_state["user_id"])

if response.ok:
    try:
        politicians = response.json()
    except json.decoder.JSONDecodeError:
        st.error("Error: Received empty or invalid JSON from server.")
        politicians = []
else:
    st.error(f"Error: {response.status_code} {response.reason}")
    politicians = []

with col1:
    selected_politician = st.selectbox(label="Select Politician:", options=politicians, index=0, format_func=lambda pol: pol["Name"])

with col2:
    if st.button("New Politician"):
        st.switch_page('pages/42_NewPolitician.py')


st.subheader('Policy Changes')
st.text('Monetary Policy:')
col1, col2, col3 = st.columns(3)
with col1:
    st.slider(label='Discount Rate')

with col2:
    st.slider(label='Treasury Securities')

with col3:
    st.slider(label='Feature #3')



if st.button("Save Note", type="primary", use_container_width=True):
    if selected_politician == None:
        st.write("Please select a Politician")
    else: 
        returnJson = {"politician_id": selected_politician["politician_id"],
              "content": content, "title": title, "user_id": st.session_state["user_id"]}
        getmethods.postNote(returnJson)
        st.switch_page("pages/43_Lobbyist2.py")

