import streamlit as st
from datetime import date
from streamlit_calendar import calendar

# Ensures users who do not complete the user information form 
# will be sent back to complete the form
if st.session_state.get("counter", 0) == 0:
    st.switch_page("Home_Page.py")

# Initializing default values to session state variables
# to persist data across reruns
if "entries" not in st.session_state:
    st.session_state.entries = {}
if "mood_level" not in st.session_state:
    st.session_state.mood_level = ""
if "mood_type" not in st.session_state:
    st.session_state.mood_type = None
if "mood_type_color" not in st.session_state:
    st.session_state.mood_type_color = None
if "journal_text" not in st.session_state:
    st.session_state.journal_text = None
if "selected_date" not in st.session_state:
    st.session_state.selected_date = None


# Displays emotion level (emoji) along with text shown in form
# Emotion level also shown in calendar
moods_level = [
    ("😢", "Very bad"),
    ("😕", "Bad"),
    ("😐", "Okay"),
    ("🙂", "Good"),
    ("😄", "Great")
]
# list to store mood type
mood_type = ["Happy", "Sad", "Anxious", "Angry", "Calm", "Other"]

st.title("Mood Calendar")

# The pop-up shown to users when they choose to log their day
# Allows users to input values, mood level and type that will show on calendar
# Journal entries also inputted through here
@st.dialog("Log your day!")
def show_mood_log_dialog():
    st.subheader(f"Hi {st.session_state.first_name}, how are you?")

    st.session_state.mood_level, text = moods_level[2]
    level = st.select_slider("Select mood level", options=[1, 2, 3, 4, 5])
    st.session_state.mood_level, text = moods_level[level - 1]

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col3:
        st.write(f"{st.session_state.mood_level} {text}")

    with st.form(key="logging_user_mood"):
        st.subheader("Why do you feel this way?")
        st.session_state.journal_text = st.text_area("Type here")

        st.session_state.mood_type = st.radio(
            "Select your mood type", 
            options=mood_type
        )
        # Finds the color value that matches each mood type
        if st.session_state.mood_type == "Happy":
            st.session_state.mood_type_color = (255, 209, 106)
        elif st.session_state.mood_type == "Sad":
            st.session_state.mood_type_color = (0, 104, 201)
        elif st.session_state.mood_type == "Anxious":
            st.session_state.mood_type_color = (109, 63, 192)
        elif st.session_state.mood_type == "Angry":
            st.session_state.mood_type_color = (255, 43, 43)
        elif st.session_state.mood_type == "Calm":
            st.session_state.mood_type_color = (41, 176, 157)
        elif st.session_state.mood_type == "Other":
            st.session_state.mood_type_color = (211, 211, 211)

        st.divider()
        st.session_state.selected_date = st.date_input(
            "Select the date pertaining to this information", 
            max_value=date.today()
        )

        submit = st.form_submit_button("Submit")
        if submit:
            st.session_state.entries[st.session_state.selected_date] = {
                "mood_level": st.session_state.mood_level,
                "mood_type": st.session_state.mood_type,
                "mood_type_color": st.session_state.mood_type_color,
                "journal": st.session_state.journal_text
            }
    if st.button("Close"):
        st.rerun()


# Adjusted Calendar from GitHub
# Displays user inputed mood types and levels
# onto calendar

calendar_options = {
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": ""
    },
    "initialView": "dayGridMonth"
}

calendar_events = []

# Get the mood entries and turn them into calendar events
for entry_date, entry in st.session_state.entries.items():
    if entry_date is not None:
        color = entry["mood_type_color"]

        # Convert RGB color to a format the calendar understands
        color = "#{:02x}{:02x}{:02x}".format(
            color[0], color[1], color[2]
        )

        calendar_events.append({
            "title": entry["mood_level"] + " " + entry["mood_type"],
            "start": str(entry_date),
            "allDay": True,
            "backgroundColor": color,
            "borderColor": color
        })

# creates an event for user birthday for the next 10 years
birthday = st.session_state.birthday

for year in range(birthday.year, date.today().year + 11):
    birthday_date = birthday.replace(year=year)

    calendar_events.append({
        "title": "🎂 Birthday!",
        "start": str(birthday_date),
        "allDay": True,
        "backgroundColor": "#E2B6FF",
        "borderColor": "#E2B6FF" 
    })

calendar_result = calendar(
    events=calendar_events,
    options=calendar_options,
    key="mood_calendar"
)


col1, col2, col3, col4 = st.columns([1, 1, 1.65, 1]) # adjusting button locations
with col1:
    back_to_home_button = st.button("⬅️", key="first_go_back")
with col3:
    log_mood_button = st.button("Log Mood")

if back_to_home_button:
    # When pressed, returns user to home page
    st.switch_page("Home_Page.py")
elif log_mood_button:
    # When pressed, shows user place to log their daily entries
    show_mood_log_dialog()