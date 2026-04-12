import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_technology_fact():
    response = requests.get(url)

    if response.status_code == 200:
        
        fact_data = response.json()
    
        print(f"Did you know? {fact_data['text']}")
        
    else:
        print("Oops, try again!")

while True:
    
    user_input = input("Press enter to get a new technology fact or press 'q' to exit.")
    
    if user_input.lower() == 'q':
        break

    get_random_technology_fact()