#Exercise 1

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sampleJson_dic = json.loads(sampleJson)
print(sampleJson_dic['company']['employee']['payble']['salary'])

#Exercise 2

sampleJson = {"id": 1, "name": "value2", "age": 29}
sampleJson_sort = json.dumps(sampleJson, sort_keys=True)
with open('sampleJson_sort.txt', 'w') as outfile:
    json.dump(sampleJson_sort, outfile)
print(sampleJson_sort)

