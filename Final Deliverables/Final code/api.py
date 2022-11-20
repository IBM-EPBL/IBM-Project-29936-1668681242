import requests

key="d5162e46c64f46de8dc4f4d5d54a03a8"

def headlines():
       r="https://newsapi.org/v2/top-headlines?country=in&apiKey={}"
       s=r.format(key)
       d=requests.get(s)
       data=d.json()
       return data
       
def search(q):
       r="https://newsapi.org/v2/everything?q={}&apiKey={}"
       s=r.format(q,key)
       d=requests.get(s)
       data=d.json()
       return data

def category(cat):      
       r="https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category={}&apiKey={}"
       s=r.format(cat,key)
       d=requests.get(s)
       data=d.json()
       return data
