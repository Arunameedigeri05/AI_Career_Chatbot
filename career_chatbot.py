import streamlit as st

st.title("🎓 AI Career Guidance Chatbot")

name = st.text_input("Enter your name:")
interest = st.text_input("What subjects or topics do you enjoy? (e.g., math, biology, art)")

career_map = {
    "math": ["Data Scientist", "Software Engineer", "Statistician"],
    "biology": ["Doctor", "Biotechnologist", "Pharmacist"],
    "art": ["Graphic Designer", "Animator", "Interior Designer"],
    "business": ["Entrepreneur", "Marketing Manager", "Accountant"],
    "physics": ["Mechanical Engineer", "Astronomer", "Robotics Engineer"],
    "literature": ["Content Writer", "Editor", "Professor"]
}

resources = {
    "Data Scientist": "https://www.coursera.org/specializations/data-science-python",
    "Doctor": "https://www.medicalnewstoday.com/articles/how-to-become-a-doctor",
    "Graphic Designer": "https://www.coursera.org/specializations/graphic-design",
    "Entrepreneur": "https://www.udemy.com/course/entrepreneurship-course/",
    "Mechanical Engineer": "https://nptel.ac.in/courses/112/105/112105125/",
    "Content Writer": "https://www.udemy.com/course/writing-with-confidence/"
}

if st.button("Suggest Career"):
    found = False
    for key in career_map:
        if key in interest.lower():
            found = True
            st.success(f"Hi {name}, based on your interest in {key}, you can explore:")
            for career in career_map[key]:
                st.markdown(f"- *{career}* – [Learn More]({resources.get(career, '#')})")
            break
    if not found:
        st.warning("Sorry! I couldn't understand your interest. Try using keywords like math, biology, art, etc.")