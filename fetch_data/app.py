
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

#scraping the data(html)
def fetch_data(url):
    html=requests.get(url)
    soup=BeautifulSoup(html.content,'html.parser')

    # Ectract Needy data from the HTML
    news=[]
    for i in soup.find_all('div'):

        title = i.find('a', class_='open-section')
        if title is not None:
            title = title.text.strip()
        else:
            title = ''


        content=i.find('p')
        if content is not None:
            content = content.text.strip()
        else:
            content = ''

        date_time=i.find('span',class_='latestDate')
        if date_time is not None:
            date_time=date_time.text.strip()
        else:
            date_time=''

        news.append({
            'title':title,
            'content':content,
            'date':date_time
        })
    return news

@app.route('/')
def api():
    malik=fetch_data('https://www.thenews.com.pk/latest-stories')
    return jsonify(malik)

if __name__ == "__main__":
    app.run(debug=True)
