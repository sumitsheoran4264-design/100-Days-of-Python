from bs4 import BeautifulSoup 
import requests
from ytmusicapi import YTMusic, OAuthCredentials
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
oauth_file = Path(__file__).with_name("oauth.json")

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

ytmusic = YTMusic(
    str(oauth_file),
    oauth_credentials=OAuthCredentials(client_id=client_id,
                                       client_secret=client_secret)
)
# date = input("Which year do want to travel to? Type the date in this format YYYY-MM-DD: ")

youtube_music_url = "https://music.youtube.com/"
billboard_app_url = f"https://appbrewery.github.io/bakeboard-hot-100/2025-07-26/"  #available dates = "2025-04-12", "2025-07-05", "2025-07-26", "2025-09-27", "2026-02-07", "2026-02-14", "2026-02-21", "2026-02-28", "2026-03-07", "2026-03-14", "2026-03-21", "2026-03-28", "2026-04-04", "2026-04-11", "2026-04-18"


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(billboard_app_url, headers=header)
contant = response.text

soup = BeautifulSoup(contant, "html.parser")

all_songs = soup.find_all(name="h3", class_="chart-entry__title")

song_names = [song.get_text().strip() for song in all_songs]


print(song_names)

song_title_list = []
song_video_id_list = []
for song in song_names:
    print(song)
    search_result = ytmusic.search(song,filter="songs")
    song_name = search_result[0]['title']
    song_title_list.append(song_name)
    song_video_id = search_result[0]['videoId']
    song_video_id_list.append(song_video_id)

initial_videos = song_video_id_list[:10]
remaining_videos = song_video_id_list[10:]

playlist_id = ytmusic.create_playlist(
    title="My 100 Python Playlist",
    description="Created automatically using Python with 100 song IDs",
    privacy_status="PRIVATE",
    video_ids=initial_videos
)
batch_size = 50
for i in range(0, len(remaining_videos), batch_size):
    batch = remaining_videos[i:i + batch_size]
    ytmusic.add_playlist_items(playlist_id, batch)
    print(f"Added batch {i // batch_size + 1} of songs successfully!")

print(len(song_video_id_list))
 