
import urllib.request,json
from .models import News

api_key = None
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    get_news_url = base_url.format('fortune',api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results= None

        if get_news_response['articles']:
            news_articles_list= get_news_response['articles']
            news_results = process_articles(news_articles_list)

    return news_results

def process_articles(news_list):

    processed_results = []
    for news_item in news_list:
        title = news_item.get('title')
        image = news_item.get('urlToImage')
        description = news_item.get('description')
        date = news_item.get('publishedAt')
        url = news_item.get('url')

        if image:
            news_object = News(title,image,description,date,url)
            processed_results.append(news_object)

    return processed_results


