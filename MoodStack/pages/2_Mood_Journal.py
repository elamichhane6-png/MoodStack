import streamlit as st


# Ensures users who do not complete the user information form 
# will be sent back to complete the form
if st.session_state.get("counter", 0) == 0:
    st.switch_page("Home_Page.py")

# Will be used to determine if there at least one entry in a month
count = 0

st.title("Mood Journal")


# Showcases journal entries user has created based
# on the selected month that filters the entries
date_col1, date_col2 = st.columns([1, 1])
with date_col1:
    selected_month = st.date_input("Select a month")

st.subheader(selected_month.strftime("%B %Y"))

# Displays user entries based on the month selected
# First iterates through all entries in reverse sorted order and filters
# based on the month provided

for entry_date, entry in sorted(st.session_state.entries.items(), reverse=True):
    if entry_date.month == selected_month.month and entry_date.year == selected_month.year:
        with st.container(border=True):
            st.write(f"**{entry_date.strftime('%B %d, %Y')}**")
            st.write(f"Mood Level: {entry['mood_level']}")
            st.write(f"Mood Type: {entry['mood_type']}")
            st.write("Journal Entry:")
            st.write(entry["journal"])
        count = count + 1 # Count increases when a entry is found

# Checks if any entries were found, if not prints call to action to user
if count == 0:
    st.write("Start a daily entry by going to your Mood Calendar!")

    
# When pressed, returns user to home page
if st.button("⬅️", key = "third_go_back"):
    st.switch_page("Home_Page.py")
  
