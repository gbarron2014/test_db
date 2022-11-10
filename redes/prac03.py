import requests
main_api = 'https://fakestoreapi.com'
response = requests.get(f"{main_api}/products").json()

for item in response:    
    print('============================================================')
    print(f"{item['rating']['rate']}")

