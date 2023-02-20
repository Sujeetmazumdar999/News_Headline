
from flask import Flask, render_template
import requests

app=Flask(__name__)
#128848611a244b8983a019af303adf6f

@app.route('/')
def getNews():
    api_key= "128848611a244b8983a019af303adf6f"
    url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=" +api_key
    news= requests.get(url).json()

    articles = news["articles"]
    my_articles=[]
    my_news=""

    for article in articles:
        my_articles.append(article["title"])




    #context= {'my_news': my_news }
    return render_template('index.html',msg=my_articles)






if __name__=='__main__':
    app.run(debug=True)
