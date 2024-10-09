from bs4 import BeautifulSoup
# import lxml # for XML content use this to pass the file to soup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.li.getText)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_tags:
#     print(tag.getText)
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
company_url = soup.select_one(selector="p a")
# print(company_url)

headings = soup.select(".heading")
# print(headings)


