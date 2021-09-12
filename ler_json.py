import json

def ler_json():
    with open('config.json', 'r', encoding='utf8') as f:
        return json.load(f)
   
print(ler_json())
input()