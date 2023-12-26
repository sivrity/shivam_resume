import streamlit as st
from streamlit_option_menu import option_menu


import navbar, component


selected =navbar.streamlit_menu()
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


if selected == "Intro":
    component.Intro()
    
    component.Summary("## Summary", 0, 24)
if selected == "Project":
    selected=navbar.horizontal_menu()
    if selected == "Python":
        component.Summary(selected, 1, 24)
        component.Project("## Python - Project List",12,13,14)
    if selected == "Php":
        component.Summary(selected, 2, 24)
        component.Project("## Php - Project List",15,16,17)
    if selected == "Java":
        component.Summary(selected, 3, 24)
        component.Project("## Java - Project List",18,19,20)
    if selected == "JavaScript":
        component.Summary(selected, 4, 24)
        component.Project("## JavaScript - Project List",21,22,23)

if selected == "Education":
    component.Education("## Education", 0, 1, 2)
if selected == "Experience":
    component.Education("## Experience", 3,4,5)
if selected == "Achievement":
    component.Education("## Achievement",6,7,8)

if selected == "Other":
    component.Education("## Other",9,10,11)
