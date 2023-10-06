#init python:
    #import requests

    #url = 'https://crucialexperiment.su/api/steam/user-items.php'
    #params = {
        #'steamid': '76561198413976685'
    #}

    #response = requests.get(url, params=params)
    #data = response.json()

    #items = {}

    #for item in data:
        #item_data = {
            #'name': item['name_en'],
            #'name_ru': item['name_ru'],
            #'color': item['name_color'],
            #'type': item['type'],
            #'icon_url': item['icon_url'],
            #'description': item['description_en'],
            #'description_ru': item['description_ru'],
        #}
        #items[item['name_en']] = item_data