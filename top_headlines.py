import requests
from bs4 import BeautifulSoup
# import nltk
# nltk.download('vader_lexicon')

import nltk.sentiment.vader as vader

# Define URL with technology keyword
url = "https://news.google.com/search?q=technology&hl=en"

# Send request and get response
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find all news titles
  titles = soup.find_all('a', attrs={'class': 'JtKRv'})

  # Create sentiment analyzer object
  sentiment_analyzer = vader.SentimentIntensityAnalyzer()

  # Print headlines with sentiment analysis
  for i, title in enumerate(titles[:5]):
    # Analyze sentiment
    sentiment = sentiment_analyzer.polarity_scores(title.text.strip())

    # Print title, sentiment score, and classification
    print(f"{i+1}. {title.text.strip()}")
    print(f"  * Sentiment Score: {sentiment['compound']}")
    print(f"  * Classification: {max(sentiment, key=sentiment.get)}")
else:
  print("Failed to retrieve news headlines.")
