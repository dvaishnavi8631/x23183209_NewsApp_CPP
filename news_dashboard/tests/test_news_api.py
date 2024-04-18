import unittest
from unittest.mock import patch
from news_dashboard.news_api import NewsAPI

class TestNewsAPI(unittest.TestCase):
    @patch('news_dashboard.news_api.requests.get')
    def test_get_top_headlines(self, mock_get):
        # Mocking the response from the News API
        mock_response = {
            'status': 'ok',
            'articles': [
                {'title': 'Article 1', 'description': 'Description 1'},
                {'title': 'Article 2', 'description': 'Description 2'}
            ]
        }
        mock_get.return_value.json.return_value = mock_response

        # Initialize NewsAPI object with a dummy API key
        news_api = NewsAPI(api_key='dummy_api_key')
        articles = news_api.get_top_headlines()

        # Asserting that the function returns the expected articles
        self.assertEqual(articles, mock_response['articles'])

if __name__ == '__main__':
    unittest.main()
