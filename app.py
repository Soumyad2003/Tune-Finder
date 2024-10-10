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


def fetch_id(music_title):
    try:
        response = requests.get("https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query={}".format(music_title))
        data = response.json()
        if data['songs']['data']:
            return data['songs']['data'][0]['id']
        else:
            return "Wa2ECpqQ"
    except Exception:
        return "Wa2ECpqQ"


def fetch_poster(id):
    try:
        response = requests.get("https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids={}".format(id))
        data = response.json()
        if data['{}'.format(id)]:
            return data['{}'.format(id)]['image']
        else:
            return "https://c.saavncdn.com/580/Despacito-Latin-2017-150x150.jpg"
    except Exception:
        return "https://c.saavncdn.com/580/Despacito-Latin-2017-150x150.jpg"


def fetch_link(id):
    try:
        response = requests.get("https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids={}".format(id))
        data = response.json()
        if data['{}'.format(id)]:
            return data['{}'.format(id)]['perma_url']
        else:
            return "https://www.jiosaavn.com/song/despacito/JwlZdDdARmI"
    except Exception:
        return "https://www.jiosaavn.com/song/despacito/JwlZdDdARmI"


def recommend(musics):
    music_index = music[music['Song'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music = []
    recommended_music_poster = []
    recommended_music_link = []
    for i in music_list:
        music_title = music.iloc[i[0]].Song
        id = fetch_id(music_title)
        recommended_music.append(music.iloc[i[0]].Song)
        recommended_music_poster.append(fetch_poster(id))
        recommended_music_link.append(fetch_link(id))
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
        st.markdown(f"<p style='color: white;'>{names[0]}</p>", unsafe_allow_html=True)
        st.image(posters[0])
        st.markdown(f"[Listen on JioSaavn]({link[0]})")
    with col2:
        st.markdown(f"<p style='color: white;'>{names[1]}</p>", unsafe_allow_html=True)
        st.image(posters[1])
        st.markdown(f"[Listen on JioSaavn]({link[1]})")
    with col3:
        st.markdown(f"<p style='color: white;'>{names[2]}</p>", unsafe_allow_html=True)
        st.image(posters[2])
        st.markdown(f"[Listen on JioSaavn]({link[2]})")
    with col4:
        st.markdown(f"<p style='color: white;'>{names[3]}</p>", unsafe_allow_html=True)
        st.image(posters[3])
        st.markdown(f"[Listen on JioSaavn]({link[3]})")
    with col5:
        st.markdown(f"<p style='color: white;'>{names[4]}</p>", unsafe_allow_html=True)
        st.image(posters[4])
        st.markdown(f"[Listen on JioSaavn]({link[4]})")
