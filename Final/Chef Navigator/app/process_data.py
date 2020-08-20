import requests


api_key = '7f960416fe004948b003853e9fb5e3bb'

def search_by_ingrediant(ing_name):
  ing_name = ing_name.replace(' ', '%20')
  response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={ing_name}&apiKey={api_key}",
  headers={
      'Content-Type': 'application/json'
    },
  )
  return response.json()

def search_by_id(id):
    response = requests.get(f'https://api.spoonacular.com/recipes/{id}/information?apiKey={api_key}',
    headers = {
        'Content-Type': 'application/json'
              },
    )
    return response.json()