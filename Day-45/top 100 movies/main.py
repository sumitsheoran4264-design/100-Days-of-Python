from bs4 import BeautifulSoup
import requests
import re

url ="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

with requests.get(url) as response:
    contant = response.text


soup = BeautifulSoup(contant, "html.parser")

all_movies_name_list = soup.find_all(name="h3" , class_="title")


movies_name = []

for movies in all_movies_name_list:
    movies_name.append(movies.get_text())

movies_name.reverse()


for moive in movies_name:
    name_of_movie = re.sub(r'[ ( ) ] E.T. â\x80\x93', '', moive)
    with open("Day-45/top 100 movies/movies_name.txt", mode="a") as moives_name_file:
        moives_name_file.write(f"{name_of_movie}\n")
        