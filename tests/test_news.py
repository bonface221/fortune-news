import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News(
            'Ukraine',
            "https://ichef.bbci.co.uk/news/1024/branded_news/74A2/production/_124385892_gettyimages-1240390485.jpg",
            'Russia attacks again','12/04/2022',
            "http://www.bbc.co.uk/news/world-europe-61296851"
        )

    def test_instances(self):
        self.assertTrue(isinstance(self.new_news,News))