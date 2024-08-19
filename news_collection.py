# import requests
# import pandas as pd
#
# API_KEY = '1127fb1c4d1e4848b027e1ffcfb836a0'  # Replace with your NewsAPI key
# QUERY = 'stocks'
# URL = f'https://newsapi.org/v2/everything?q={QUERY}&apiKey={'1127fb1c4d1e4848b027e1ffcfb836a0'}'
#
# response = requests.get(URL)
# articles = response.json().get('articles', [])
#
# # Create DataFrame
# news_data = pd.DataFrame(articles)
# news_data.to_csv('news_data.csv', index=False)
# print('News data saved to news_data.csv')
