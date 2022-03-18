import requests
import json

API_KEY= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
API_SECRET= 'xxxxxxxxxxxxxxx'


times_url='https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key='+API_KEY


def get_news():

    result_ny = requests.get(times_url)
    json_data = json.loads(result_ny.text)
    
    resultados = json_data['results']
    
    final=[]
    
    for resultado in resultados:
        title= resultado['title']
        text = resultado['abstract']
        url = resultado['url']
        juntar=[]
        juntar.append(title)
        juntar.append(text)
        juntar.append(url)
        final.append(juntar)
    return final





