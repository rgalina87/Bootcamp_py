import requests

# ingredients = []
# api_key = '7f960416fe004948b003853e9fb5e3bb'
# url = 'https://api.spoonacular.com/recipes/complexSearch31'

def search_by_ingredient(ingredients):
    api_key = '7f960416fe004948b003853e9fb5e3bb'
    url = 'https://api.spoonacular.com/recipes/complexSearch31'
    params = {"apiKey": api_key,
              "query": ' '.join(ingredients)}
    response = requests.get(url, params)
    return response.json()

# def search_by_id(id):
#     api_key = '7f960416fe004948b003853e9fb5e3bb'
#     url = 'https://api.spoonacular.com/recipes/complexSearch31'
#     params = {"apiKey": api_key,
#               "query": ' '.join(id)
#               }
#     response = requests.get(url, params)
#     return response.json()