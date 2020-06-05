#Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for result in zip(keys, values):
    print(result)

#Exercise 2

store = {
    "name": "Zara",
    "creation_date": 1975,
    "creation_name": "Amancio Ortega Gaona ",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue",
                    "Spain": "red",
                    "US": ["pink", "green"],
                    }
}

#1
store["number_stores"] = 2
#2
print("Target audience of Zara is", store["type_of_clothes"])
#3
store["country_creation"] = "Spain"
#4
if "international_competitors" in store:
    store["international_competitors"] += ["Desigual"]
else:
	none
#5
del store["creation_date"]
#6
print(store["international_competitors"][-1])
#7
print("The major colors in the US is", store["major_color"]["US"])
#8
print(len(store))
#9
print(store.keys())
#10
more_on_store = {
    "creation_date": 1975,
    "number_stores": 10000,
}

store.update(more_on_store)
print(store)