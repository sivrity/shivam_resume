import streamlit as st
from streamlit_player import st_player, _SUPPORTED_EVENTS
import database_config
from PIL import Image

database_url = "https://docs.google.com/spreadsheets/d/1Xf9xu9mIPywKDiMphXsjnf7DG0VQ3Tmk9-tvCKq5MTM/edit?usp=sharing"
Database = database_config.SaeeAM_query(f'SELECT * FROM "{database_url}"')





def datafetch(a, b, c):
  col1, col2 = st.columns([6,3])
  with col1:
    st.markdown(a)
    st.markdown(c)
  with col2:
    st.markdown(b)

def Project_show(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(f'{b}')
  with col3:
    st_player(c, height=200, key=b)
    

def Project(title, row_no1=10, row_no2=11, row_no3=12):
    st.markdown(title)
    for doing in Database:
        with st.container():    
            if doing[row_no1] != None:
                Project_show(doing[row_no1],doing[row_no2],doing[row_no3])
                st.markdown("***")

def Education(title, row_no1=1, row_no2=2, row_no3=3):
    st.markdown(title)
    for edu in Database:
    
        if edu[row_no1] != None:
            datafetch(edu[row_no1],edu[row_no3], edu[row_no2])               
    

def Summary(title,row_no, col_no):
    st.markdown(title, unsafe_allow_html=True)
    if Database[row_no][col_no] !=None:
      st.info(Database[row_no][col_no])


def Intro():
    image = Image.open('dp1.jpg')
    st.image(image, width=150)

    st.write('''
  # Shivam kumar singh resume.
  ''')