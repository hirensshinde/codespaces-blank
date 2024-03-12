import requests
from bs4 import BeautifulSoup

# Define the URL with technology keyword
url = "https://news.google.com/search?q=technology&hl=en"

# Send request and get response
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find all news titles
  titles = soup.find_all('a', attrs={'class': 'JtKRv'})

  # Print only the top 5 headlines
  for i, title in enumerate(titles[:5]):
    print(f"{i+1}. {title.text.strip()}")
else:
  print("Failed to retrieve news headlines.")
