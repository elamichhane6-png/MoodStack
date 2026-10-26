import streamlit as st
from datetime import date

# Ensures users who do not complete the user information form will be sent back
if st.session_state.get("counter", 0) == 0:
    st.switch_page("Home_Page.py")

# Page title
st.title("⚙️ Settings")
st.write("Handle your personal information.")
st.divider()

# Allows user to change data by hitting submit
with st.form(key="settings_form"):

    st.subheader("General Information")

# Gets new user first name and last name inputs
    first_name_input = st.text_input(
        "Enter your first name",
        value=st.session_state.get("first_name", "")
    )

    last_name_input = st.text_input(
        "Enter your last name",
        value=st.session_state.get("last_name", "")
    )

    st.subheader("User Birthday Information")
# Gets new birthday input from user
    min_date = date(1950, 1, 1)
    max_date = date.today()

    birthday_input = st.date_input(
        "Select your date of birth",
        value=st.session_state.get("birthday", date.today()),
        min_value=min_date,
        max_value=max_date,
        format="MM-DD-YYYY"
    )

    st.divider()

    submit_button = st.form_submit_button("Save Changes")
# Sends warning to user if fields are blank
    if submit_button:
        if not first_name_input.strip() or not last_name_input.strip():
            st.warning("Please fill in all of the fields.")
        else: 
            # Updates user information when submit button is pressed 
            st.session_state.first_name = first_name_input.strip()
            st.session_state.last_name = last_name_input.strip()
            st.session_state.birthday = birthday_input

            st.rerun()

st.divider()

# When pressed, returns user to home page
if st.button("⬅️", key="second_go_back"):
    st.switch_page("Home_Page.py")