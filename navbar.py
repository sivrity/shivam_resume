import streamlit as st
from streamlit_option_menu import option_menu

def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title="Shivam resume",  # required
            options=["Intro", "Project", "Education", "Experience", "Achievement", "Other"],  # required
            # icons=["house", "browser-chrome", "book","degree","medal", "envolpe"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    return selected


def horizontal_menu():
    Hori_selected = option_menu(
        menu_title=None,  # required
        options=["Python", "Java", "Php", "JavaScript"],  # required
        # icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        # styles={
        #         "container": {"padding": "0!important", "background-color": "#fafafa"},
        #         "icon": {"color": "orange", "font-size": "25px"},
        #         "nav-link": {
        #             "font-size": "25px",
        #             "text-align": "left",
        #             "margin": "0px",
        #             "--hover-color": "#eee",
        #         },
        #         "nav-link-selected": {"background-color": "green"},
        #     },
        )
    return Hori_selected