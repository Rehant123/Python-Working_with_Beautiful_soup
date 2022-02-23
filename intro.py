from bs4 import BeautifulSoup

with open("website.html",encoding = "utf8") as file:
    contents  = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
all_anchor_tags = soup.findAll(name = "a")
print("\n")
paragraph_tag = soup.findAll(name = "p")

# print(paragraph_tag)

#print all anchor_tag


#--------------------getText
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())

#print all anchor

#---------------------get
for tag in all_anchor_tags:
    print(tag.get("href"))

#-------------------find
heading = soup.find(name = "h1",id = "name")
print(heading)

section_heading = soup.find(name = "h3",class_ = "heading")
print(section_heading.get("class"))


###-----------------select_one
company_url = soup.select_one(selector ="p a")
print(company_url) 

#using select with id
name = soup.select(selector = "#name")
print(name)

#using select with class
heading = soup.select(".heading")
print(heading)
