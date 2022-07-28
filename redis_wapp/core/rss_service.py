import requests

def get_cnn_rss():
    response = requests.get("http://rss.cnn.com/rss/edition_europe.rss")
    #print(response.content)
