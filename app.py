import streamlit as st
import pickle
import pandas as pd

import requests
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});

        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local(r'C:\Users\pomys\Desktop\music-recommendation-system\background_image.jpg')


def fetch_poster(music_title):
    response = requests.get("https://saavn.dev/api/search/songs?query={}".format(music_title))
    data = response.json()
    return data['data']['results'][0]['image'][2]['url']


def fetch_link(music_title):
    response = requests.get("https://saavn.dev/api/search/songs?query={}".format(music_title))
    data = response.json()
    return data['data']['results'][0]['url']


def recommend(musics):
    music_index = music[music['Song'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music = []
    recommended_music_poster = []
    recommended_music_link = []
    for i in music_list:
        music_title = music.iloc[i[0]].Song
        recommended_music.append(music.iloc[i[0]].Song)
        recommended_music_poster.append(fetch_poster(music_title))
        recommended_music_link.append(fetch_link(music_title))
    return recommended_music, recommended_music_poster, recommended_music_link


music_dict = pickle.load(open(r'C:\Users\pomys\Desktop\music-recommendation-system\music_rec.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open(r'C:\Users\pomys\Desktop\music-recommendation-system\similarities.pkl', 'rb'))
st.title('Song Recommendation System')

selected_music_name = st.selectbox('Select a song you like', music['Song'].values)

if st.button('Recommend'):
    names, posters, link = recommend(selected_music_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.markdown(f"[Listen on JioSaavn]({link[0]})")
    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.markdown(f"[Listen on JioSaavn]({link[1]})")
    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.markdown(f"[Listen on JioSaavn]({link[2]})")
    with col4:
        st.text(names[3])
        st.image(posters[3])
        st.markdown(f"[Listen on JioSaavn]({link[3]})")
    with col5:
        st.text(names[4])
        st.image(posters[4])
        st.markdown(f"[Listen on JioSaavn]({link[4]})")
