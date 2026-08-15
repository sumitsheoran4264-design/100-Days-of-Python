from bs4 import BeautifulSoup
import requests
url = "https://news.ycombinator.com"
response = requests.get(url)

yc_webpage = response.text



soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.a.get_text()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)


largest_num = max(article_upvote)
largest_index = article_upvote.index(largest_num)

print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_num)


#--------------------------------------------------------------------------------#
#=============================== Parctice from website html ======================
#_________________________________________________________________________________#


# with open(file="Day-45/website.html") as file:
#     contants = file.read()

# soup = BeautifulSoup(contants, "html.parser")
# all_unorderd_list = soup.find_all(name="li")
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading.string)
# section_heading = soup.find(name="h3", class_="heading")
# company_url = soup.select_one(selector="p a ")
# print(company_url)

# name = soup.select_one("#name")
# print(name.get_text())

# all_headings = soup.select_one(".heading")
# print(all_headings)