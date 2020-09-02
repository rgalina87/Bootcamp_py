import requests

ingredients = []

def search_by_ingredient(ingredients):
    api_key = '7f960416fe004948b003853e9fb5e3bb'
    # api_key = '16df366821304f2a9b6d992cbbd52431'
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {"apiKey": api_key,
              "query": ' '.join(ingredients)}
    response = requests.get(url, params)
    print(response.json())
    recipe_info_url = 'https://api.spoonacular.com/recipes/{}/information'
    results = response.json()['results']
    recipes = []
    for result in results:
        print(result)
        req = requests.get(recipe_info_url.format(result['id']), params={"apiKey": api_key})
        print(req.text)
        recipes.append(req.json())
    return recipes

def recipe_info(recipe_id):
    api_key = '7f960416fe004948b003853e9fb5e3bb'
    # api_key = '16df366821304f2a9b6d992cbbd52431'
    recipe_info_url = 'https://api.spoonacular.com/recipes/{}/information'
    req = requests.get(recipe_info_url.format(recipe_id), params={"apiKey": api_key})
    return req.json()