
from flask import render_template
from .import main
from ..requests import get_news




@main.route('/')
def index():
    title = "Home - welcome to Hapa kule News updates"
    bbc_news = get_news()
    return render_template('index.html', title=title,bbc=bbc_news)
