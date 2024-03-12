import requests
from bs4 import BeautifulSoup
import ssl
import nltk
import pyttsx3
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('vader_lexicon')
import nltk.sentiment.vader as vader

# Define URL with technology keyword
url = "https://news.google.com/search?q=technology&hl=en"

engine = pyttsx3.init()

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

    # Speak the headline (optional)
    engine.say(title.text.strip())
    engine.runAndWait()
    # tts.speak(title.text.strip())
else:
  print("Failed to retrieve news headlines.")
