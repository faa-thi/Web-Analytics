import requests
from bs4 import BeautifulSoup
import pandas as pd

# IMDb URL for the Top 250 movies
url = "https://www.imdb.com/chart/top/"

# Set headers to mimic a real browser request
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch the webpage
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract movie details
    movie_list = []

    rows = soup.select("li.ipc-metadata-list-summary-item")  # Updated IMDb selector

    for row in rows[:10]:  # Limiting to first 10 movies
        title = row.select_one("h3").text if row.select_one("h3") else "N/A"

        year = row.select_one("span.sc-b0691f29-8").text if row.select_one("span.sc-b0691f29-8") else "N/A"

        rating = row.select_one("span.sc-b0691f29-1").text if row.select_one("span.sc-b0691f29-1") else "N/A"

        movie_list.append([title, year, rating])
        print(f"Title: {title}, Year: {year}, Rating: {rating}")  # Debugging
   
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
