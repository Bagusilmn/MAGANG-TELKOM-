from bs4 import BeautifulSoup
import requests

# HTML From File
# with open("index.html", "r") as f:
# 	doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all("p")[0]

# print(tags.find_all("b"))

# # HTML From Website
# url = "https://www.newegg.ca/gigabyte-liquid-cooling-system-radiator-size-277-x-119-x-27mm/p/N82E16835128038?Item=N82E16835128038"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(text="$")
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)


# HTML From Website
url = "https://gis.dukcapil.kemendagri.go.id/arcgis/apps/experiencebuilder/experience/?id=7d1ab9b69ded40ca97e82fc9b2bdd50c"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

print(doc.prettify())