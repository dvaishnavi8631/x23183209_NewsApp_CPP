from newsapi_client.client import NewsApiClient

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual News API key
    news_api = NewsApiClient(api_key='b52eb77ce6764314a4d14eeee7f0255b')
    articles = news_api.get_top_headlines()

    for article in articles:
        print(article['title'])
