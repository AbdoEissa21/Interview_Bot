import streamlit as st
import json
import time
import random
import requests
import copy
import os

st.set_page_config(
    page_title='Interview Bot'
)
general_question_types = ["Multiple Choice", "Open Ended"]
question_types = general_question_types + ["System Design", "Take Home Assessment", "Data Structure and Algorithms", "Behavioral"]
with st.sidebar:
	st.markdown("## Enter Job Details")
	st.markdown("*Paste the basic info for the job you're applying to*")
	st.session_state.job_position = st.text_input("Job Position", placeholder="Paste your job position here (e.g. Junior Software Engineer)")

	st.session_state.job_description = st.text_area("Job Description", placeholder="Paste your job description text here")

	st.divider()

	st.markdown("## Options")

	st.session_state.question_count = st.slider("Amount of Questions You Want", min_value=1, max_value=25)
	st.session_state.question_types = st.multiselect(
		'What type of questions do you want to generate (randomized per question)',
		question_types,
		question_types[-2:])

	st.divider()
