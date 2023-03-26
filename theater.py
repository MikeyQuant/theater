


movies={"John Wick Chapter 4":"https://www.youtube.com/watch?v=JqF6zlHRdL8","Dungeons & Dragons: Honor Among Thieves":"https://www.youtube.com/watch?v=ODYz0jkj-cQ"
        ,"Shazam! Fury of the Gods":"https://www.youtube.com/watch?v=AIc671o9yCI","Air":"https://www.youtube.com/watch?v=6VEoWb1b-L0","Creed 3":"https://www.youtube.com/watch?v=xTaIZo8OJYE"
        ,"65 Million Years":"https://m.youtube.com/watch?v=_mNmHJxfNwM","Cocaine Bear":"https://www.youtube.com/watch?v=DuWEEKeJLMI"}
import streamlit as st
for m in movies.keys():
    st.header(m)
    st.video(movies[m])

