import requests
import random
import json
import time
import utilstool

url=utilstool.url_get
user_agents=utilstool.user_agents




def client_html():
    headers = {'User-Agent': random.choice(user_agents)}
    newurl = random.choice(url)
    try:      
        response = requests.get(newurl, headers=headers)
    except Exception as e:
        print(e.args)
    else:
        result = response.json()
        print(result)




if __name__ == "__main__":
    while True:
        segundos = random.choice([1,2,3,4,5])
        time.sleep(segundos)
        client_html()