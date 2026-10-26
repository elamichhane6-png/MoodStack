import streamlit as st
from datetime import date


# Initializing default values to session state variables 
# to persist data across reruns
if "counter" not in st.session_state:
    st.session_state.counter = 0
if "first_name" not in st.session_state:
    st.session_state.first_name = ""
if "last_name" not in st.session_state:
    st.session_state.last_name = ""
if "birthday" not in st.session_state:
    st.session_state.birthday = date.today()
if "show_balloons" not in st.session_state:
    st.session_state.show_balloons = True
if "entries" not in st.session_state:
    st.session_state.entries = {}


# Only show the setup form to users if the counter is 0
if st.session_state.counter == 0:

    st.title("Welcome to Mood Stack! ")
    st.write("Before we begin, please put in information our app will utilize for functionality purposes:")
    st.divider()
# Gets user information like first name, last name, and birthday
    with st.form(key="user_information_form"):

        st.subheader("General Information")
        first_name_input = st.text_input("Enter your first name")

        last_name_input = st.text_input("Enter your last name")

        st.subheader("User Birthday Information")
        min_date = date(1950, 1, 1)
        max_date = date.today()

        birthday_input = st.date_input(
            "Select your date of birth", 
            min_value = min_date, 
            max_value = max_date, 
            format = "MM-DD-YYYY"
        )

        submit_button = st.form_submit_button("Submit")

        # Input value holders only applied AFTER 
        # the user clicks Submit with all fields filled out
        if submit_button:
            # Check if text inputs are empty strings
            if not first_name_input.strip() or not last_name_input.strip():
                st.warning("Please fill in all of the fields")
            else:
                # Increment counter ONLY on a successful, completed submission
                st.session_state.counter += 1

                # Update our session state with the validated entries
                st.session_state.first_name = first_name_input.strip()
                st.session_state.last_name = last_name_input.strip()
                st.session_state.birthday = birthday_input

                st.rerun()
# Runs normal dashboard when the form has been done once via counter
else:
    # Different title message and balloons will be displayed
    # to user when they go to dashboard for the first time
    if st.session_state.show_balloons: 
        st.balloons()            
        st.session_state.show_balloons = False

    st.title(f"👋 Hello, {st.session_state.first_name} {st.session_state.last_name}!")
    today = date.today()
    st.write(f"Today is {today.strftime('%A, %B %d, %Y')}")

    # Shows user how many mood enteries they have made this month

    monthly_entries = 0

    for entry_date in st.session_state.entries:
        if entry_date.year == today.year and entry_date.month == today.month:
            monthly_entries += 1

    st.write(f"### You have made {monthly_entries} entry/entries this month!" )
    if (monthly_entries == 0):
        st.write("Start logging today's mood!")
    else:
        st.write("Keep up the work!")


    # All buttons that go to different parts of the app
    col1, col2 = st.columns([2, 1]) 
    with col1:
        mood_calendar_button = st.button("View my Mood Calendar", use_container_width=True)
    with col2:
        settings_button = st.button("Settings", use_container_width=True)
    
    journal_button = st.button("View my Mood Journal", use_container_width=True)


    # Switches user to different pages
    if (mood_calendar_button):
        st.switch_page("pages/1_Mood_Calendar.py")
    elif(journal_button):
        st.switch_page("pages/2_Mood_Journal.py")
    elif(settings_button):
        st.switch_page("pages/3_Settings.py")
