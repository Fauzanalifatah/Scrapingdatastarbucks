import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.starbucks.co.id/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("li")

data = []

for item in titles:
    data.append(item.get_text(strip=True))

df = pd.DataFrame(data, columns=["title"])
df.to_csv("starbucks.csv", index=False)