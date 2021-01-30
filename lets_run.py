# importing general models
import os
import sys

# importing desired packages for python
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from math import floor

# global settings
CWD = os.path.abspath('.')
image = Image.open('amateur_logo.jpg')
# current_workouts = pd.read_parquet('amateur_runners/participants.parquet')
#
# current_workouts = pd.DataFrame(columns=[
#                                             'name',
#                                             'easy_mins',
#                                             'easy_seconds',
#                                             'hard_mins',
#                                             'hard_seconds',
#                                             'long_km'
#                                             ])
#
# current_workouts.to_parquet('participants.parquet')

# Streamlit Layout
st.set_page_config(layout="wide")
col1, col2 = st.beta_columns(2)
#st.markdown('<font style="font-family: Helvetica; font-size:23pt"> :tv: **Explorative Spot Analysis** </font>', unsafe_allow_html=True)
col2.image(image, width=150)
col1.header('**Willkommen bei den amateur runners und Woche 2 der Challenges**')
col1.subheader('Diese Woche bekommst du drei auf dich individuell angepasste Workouts')
col1.subheader('Klingt gut?')



st.markdown(':rocket: Auf gehts! :rocket:')
start_check = st.checkbox('Konfigurator starten')
st.markdown('---')



def new_member():
    name_input = st.text_input('Verrat uns deinen Namen')
    st.markdown('Was ist deine aktuelle pace für einen entspannten Lauf?')

    easy_mins = st.number_input('Minuten', min_value=3, max_value=7, value=5, step=1, key ='easy_mins')
    easy_seconds = st.number_input('Sekunden', min_value=0, max_value=50, value=20, step=10, key ='easy_seconds')

    st.markdown('Was ist deine aktuelle pace für einen harten Lauf?')
    st.markdown('*Du solltest die Pace mindestens 2km halten können*')
    hard_mins = st.number_input('Minuten', min_value=3, max_value=6, value=4, step=1, key ='hard_mins')
    hard_seconds = st.number_input('Sekunden', min_value=0, max_value=50, value=20, step=10, key ='hard_seconds')

    st.markdown('Ein Longrun für mich bedeuted mindestens ...km?')
    long_km = st.number_input('km', min_value=8, max_value=20, value=12, step=1, key ='long_km')
    return easy_mins, easy_seconds, hard_mins, hard_seconds, long_km, name_input


def make_text_layout(name_input, easy_mins, easy_seconds, hard_mins, hard_seconds, long_km):

    if name_input != '':
        placeholder_0.markdown('Amateur Runner: **{}**'.format(name_input))
    else:
        placeholder_0.markdown('***Vergiss nicht deinen Namen einzugeben***')


    if easy_seconds == 0:
        text_easy = 'Easy pace: {}:0{}'.format(easy_mins,easy_seconds)
    else:
        text_easy = 'Easy pace: {}:{}'.format(easy_mins,easy_seconds)
    placeholder_1.markdown(text_easy)

    if hard_seconds == 0:
        text_hard = 'Hard pace: {}:0{}'.format(hard_mins,hard_seconds)
    else:
        text_hard = 'Hard pace: {}:{}'.format(hard_mins,hard_seconds)
    placeholder_2.markdown(text_hard)
    text_long = 'Longrun: mindestens {}km'.format(long_km)
    placeholder_3.markdown(text_long)
    placeholder_4.markdown('*Pace = Minuten:Sekunden pro km*')


def workout_1_mix(easy_mins, easy_seconds, hard_mins, hard_seconds):

    warm_up = easy_mins * 60 + easy_seconds + 10
    warm_up_mins = floor(warm_up / 60)
    warm_up_seconds = warm_up - (warm_up_mins *60)
    warm_up_text = '**1)** 10 Minuten Warm-Up mit ~{}:{}'.format(warm_up_mins, warm_up_seconds)

    workout_hard = hard_mins * 60 + hard_seconds - 20
    workout_hard_mins = floor(workout_hard / 60)
    workout_hard_seconds = workout_hard - (workout_hard_mins *60)

    workout_easy = easy_mins * 60 + easy_seconds + 20
    workout_easy_mins = floor(workout_easy / 60)
    workout_easy_seconds = workout_easy - (workout_easy_mins *60)

    workout_text_part1 = '**2)** *insgesamt 5 Wiederholungen*'
    workout_text_part2 = '--> 2 Minuten ballern mit ~{}:{}'.format(workout_hard_mins, workout_hard_seconds)
    workout_text_part3 = '--> 3 Minuten chillen mit ~{}:{}'.format(workout_easy_mins, workout_easy_seconds)

    cool_down_text = '**3)** 10 Minuten Cool-down mit ~{}:{}'.format(warm_up_mins, warm_up_seconds)
    return warm_up_text, workout_text_part1, workout_text_part2, workout_text_part3, cool_down_text


def workout_2_mix(easy_mins, easy_seconds, hard_mins, hard_seconds, long_km):

    km = floor(long_km * 0.75)
    easy_in_seconds = easy_mins * 60 + easy_seconds + 10
    start_pace_seconds = easy_in_seconds

    start_mins = floor(start_pace_seconds / 60)
    start_seconds = start_pace_seconds - (start_mins *60)

    hard_in_seconds = hard_mins * 60 + hard_seconds + 10
    end_pace = hard_in_seconds
    end_mins = floor(end_pace / 60)
    end_seconds = end_pace - (end_mins *60)

    cool_in_seconds = easy_mins * 60 + easy_seconds + 20
    cool_mins = floor(cool_in_seconds / 60)
    cool_seconds = cool_in_seconds - (cool_mins *60)


    seconds_to_kill = easy_in_seconds - hard_in_seconds
    km_to_kill = km - 1
    seconds_every_km = round(seconds_to_kill / km_to_kill)

    workout_text_part1 = '**insgesamt {} km**'.format(km)
    workout_text_part2 = 'Pace für den 1ten km -> {}:{}'.format(start_mins, start_seconds)
    workout_text_part3 = 'Die nächsten {}km jeweils ca. {}s schneller als der vorherige'.format(km_to_kill-1, seconds_every_km)
    workout_text_part4 = 'Der {}te km ist der schnellste mit ca. {}:{}'.format(km_to_kill, end_mins, end_seconds)
    cool_down = '1km Cool down mit ~{}:{}'.format(cool_mins, cool_seconds)
    return workout_text_part1, workout_text_part2, workout_text_part3, workout_text_part4, cool_down



if start_check:
    easy_mins, easy_seconds, hard_mins, hard_seconds, long_km, name_input = new_member()
    st.markdown('---')
    placeholder_0 = st.empty()
    placeholder_1 = st.empty()
    placeholder_2 = st.empty()
    placeholder_3 = st.empty()
    placeholder_4 = st.empty()
    st.markdown('---')

    make_text_layout(name_input, easy_mins, easy_seconds, hard_mins, hard_seconds, long_km)

    workout1_title, workout1_steps = st.beta_columns(2)
    workout1_title.markdown(
                                "**Workout 1**  \n"
                                "Fahrtenspiel  \n"
                            )
    warm_up_text, workout_text_part1, workout_text_part2, workout_text_part3, cool_down_text = workout_1_mix(easy_mins, easy_seconds, hard_mins, hard_seconds)
    workout1_steps.markdown(warm_up_text)
    workout1_steps.markdown(workout_text_part1)
    workout1_steps.markdown(workout_text_part2)
    workout1_steps.markdown(workout_text_part3)
    workout1_steps.markdown(cool_down_text)

    workout2_title, workout2_steps = st.beta_columns(2)
    workout2_title.markdown(
                                "**Workout 2**  \n"
                                "Steigerungslauf  \n"
                            )
    workout_text_part1, workout_text_part2, workout_text_part3, workout_text_part4, cool_down = workout_2_mix(easy_mins, easy_seconds, hard_mins, hard_seconds, long_km)
    workout2_steps.markdown(workout_text_part1)
    workout2_steps.markdown(workout_text_part2)
    workout2_steps.markdown(workout_text_part3)
    workout2_steps.markdown(workout_text_part4)
    workout2_steps.markdown(cool_down)

    workout3_title, workout3_steps = st.beta_columns(2)
    workout3_title.markdown(
                                "**Workout 3**  \n"
                                "Longrun  \n"
                            )
    workout3_steps.markdown('Nothing Fancy here')
    workout3_steps.markdown('Einfach {}km in {}:{}'.format(long_km+1, easy_mins, easy_seconds))
    st.markdown('---')
    button_anmeldung = st.button('Klicken um für die Challenge anzumelden')
    anmelde_feedback = st.empty()
    anmelde_nummer = st.empty()
    st.header('Screenshot von deinen 3 Workouts nicht vergessen :wink:')
    st.subheader('Teile deine Fortschritte auf instagram und verlinke @weareamateurs')

    if button_anmeldung:
        current_workouts = pd.read_parquet('participants.parquet')
        current_member = pd.DataFrame({
                                        'name': [name_input],
                                        'easy_mins': [easy_mins],
                                        'easy_seconds': [easy_seconds],
                                        'hard_mins': [hard_mins],
                                        'hard_seconds': [hard_seconds],
                                        'long_km': [long_km]
                                        })
        current_workouts = current_workouts.append(current_member)
        current_workouts = current_workouts.drop_duplicates(subset=['name'], keep='last')
        st.write(current_workouts)
        current_workouts.to_parquet('participants.parquet')
        anmelde_feedback.markdown('Du bist jetzt für die Challenge angemeldet')
        anmelde_nummer.markdown('Amateure die mitmachen: *{}*'.format(len(current_workouts['name'])))
        st.balloons()
