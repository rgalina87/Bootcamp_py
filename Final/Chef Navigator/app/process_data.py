import requests


# api_key = '7f960416fe004948b003853e9fb5e3bb'
# url = 'https://api.spoonacular.com/recipes/complexSearch31'

ingredients = []

def search_by_ingredient(ingredients):
    api_key = '7f960416fe004948b003853e9fb5e3bb'
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {"apiKey": api_key,
              "query": ' '.join(ingredients)}
    response = requests.get(url, params)
    print("ingredients:", ingredients)
    print("RESPONSE:", response.json())
    return response.json()