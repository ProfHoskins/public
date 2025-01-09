import streamlit as st

st.title("OrgSync Hub Prototype")

st.sidebar.header("Navigation")
options = st.sidebar.radio("Go to:", ["Dashboard", "Task Management", "Budget Tracker", "Event Planner", "Attendance", "Communication"])

if options == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to OrgSync Hub! Here's an overview of your organization:")
    st.metric("Total Members", 25)
    st.metric("Upcoming Events", 3)
    st.metric("Pending Tasks", 8)

elif options == "Task Management":
    st.header("Task Management")
    st.write("Assign, track, and manage tasks:")
    tasks = [{"Task": "Finalize Budget Proposal", "Deadline": "2025-01-15", "Status": "In Progress"},
             {"Task": "Organize Welcome Event", "Deadline": "2025-01-20", "Status": "Not Started"}]
    for task in tasks:
        st.write(f"**{task['Task']}** - Deadline: {task['Deadline']} - Status: {task['Status']}")
    st.text_input("New Task:")
    st.date_input("Deadline:")
    st.button("Add Task")

elif options == "Budget Tracker":
    st.header("Budget Tracker")
    st.write("Track your organization’s budget:")
    st.metric("Total Budget", "$5,000")
    st.metric("Spent", "$1,200")
    st.metric("Remaining", "$3,800")

elif options == "Event Planner":
    st.header("Event Planner")
    st.write("Manage your events here:")
    events = [{"Event": "General Meeting", "Date": "2025-01-10", "RSVPs": 15},
              {"Event": "Community Service", "Date": "2025-01-25", "RSVPs": 10}]
    for event in events:
        st.write(f"**{event['Event']}** - Date: {event['Date']} - RSVPs: {event['RSVPs']}")
    st.text_input("New Event:")
    st.date_input("Event Date:")
    st.button("Add Event")

elif options == "Attendance":
    st.header("Attendance Check-In")
    st.write("Track attendance for your meetings or events.")
    st.button("Generate QR Code")

elif options == "Communication":
    st.header("Communication")
    st.write("Send announcements or chat with members.")
    st.text_area("Write an announcement:")
    st.button("Send Announcement")

st.sidebar.write("---")
st.sidebar.write("Prototype v1.0")
