import requests 

api_key = "fcf651a2d8cf40ff8ff69f16b109bd31"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-16&sortBy=publishedAt&apiKey=fcf651a2d8cf40ff8ff69f16b109bd31"

request = requests.get(url)
content = request.json()
for article in content['articles']:
    print(article['title'])
    #print(article['description'])
    #print(article['author'])

