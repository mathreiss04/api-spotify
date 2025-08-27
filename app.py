import os

import dotenv
import requests
import streamlit as st
from requests.auth import HTTPBasicAuth

dotenv.load_dotenv(dotenv.find_dotenv())


def authenticate():
    #Authenticate with Spotify API and return access token
    url = "https://accounts.spotify.com/api/token"
    body = {
        'grant_type': 'client_credentials',
    }
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    auth = HTTPBasicAuth(username=client_id, password=client_secret)

    response = requests.post(url=url, data=body, auth=auth)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"Authentication error: {e}")
        token = None
    else:
        token = response.json()['access_token']
        print('Access token obtained successfully!')
    return token


def search_artist(artist_name, headers):
    #Search for an artist by name
    url = "https://api.spotify.com/v1/search"
    params = {
        'q': artist_name,
        'type': 'artist',
    }
    response = requests.get(url=url, headers=headers, params=params)
    try:
        first_result = response.json()['artists']['items'][0]
    except IndexError:
        first_result = None
    return first_result


def get_top_tracks(artist_id, headers):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    response = requests.get(url=url, headers=headers)
    tracks = response.json()['tracks']
    return tracks


def main():
    #Header
    st.set_page_config(page_title='Spotify Artist Explorer', layout='wide')
    st.title('🎵 Spotify Artist Explorer')
    st.write("Explore artist info and top tracks with album covers! https://developer.spotify.com/documentation/web-api")

        # Custom CSS for nicer cards
    st.markdown("""
        <style>
        .card {
            background-color: #1e1e1e;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
        }
        .card img {
            border-radius: 8px;
            margin-right: 20px;
        }
        .card-content {
            flex: 1;
        }
        .track-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .track-info {
            font-size: 14px;
            color: #cccccc;
        }
        </style>
    """, unsafe_allow_html=True)
    
    artist_name = st.text_input('Search for an artist:')
    if not artist_name:
        st.stop()

    #Authenticate and get access token
    token = authenticate()
    if not token:
        st.stop()
    
    headers = {
        'Authorization': f'Bearer {token}'
    }

    #Search for the artist
    artist = search_artist(artist_name=artist_name, headers=headers)
    if not artist:  #Artist not found
        st.warning(f'Artist not found {artist_name}!')
        st.stop()

    #Artist info
    artist_id = artist['id']
    artist_name = artist['name']  #Update variable to ensure correct name
    artist_popularity = artist['popularity']
    artist_image = artist['images'][0]['url'] if artist['images'] else None

    #Display artist info
    col1, col2 = st.columns([1, 3])
    with col1:
        if artist_image:
            st.image(artist_image, width=200)
    with col2:
        st.subheader(f'Artist: {artist_name}')
        st.write(f'Popularity: {artist_popularity}')
    
    #Get top tracks
    st.subheader("Top Tracks 🎶")
    tracks = get_top_tracks(artist_id,headers)

    #Display each track as a card
    for track in tracks:
        track_name = track['name']
        track_popularity = track['popularity']
        album_name = track['album']['name']
        album_image = track['album']['images'][0]['url'] if track['album']['images'] else None
        track_url = track['external_urls']['spotify']

        st.markdown(f"""
            <div class="card">
                <img src="{album_image}" width="100">
                <div class="card-content">
                    <div class="track-title"><a href="{track_url}" target="_blank">{track_name}</a></div>
                    <div class="track-info">Album: {track['album']['name']}</div>
                    <div class="track-info">Popularity: {track_popularity}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
