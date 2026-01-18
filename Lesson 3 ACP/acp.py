import re
import random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    while True:
        print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
        preference = normalize_input(input(Fore.YELLOW + "You: "))

        if preference in destinations:
            suggestion = random.choice(destinations[preference])
            print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
            print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
            answer = normalize_input(input(Fore.YELLOW + "You: "))

            if answer == "yes":
                print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
                break
            elif answer == "no":
                print(Fore.RED + "TravelBot: Okay, let's try another.")
            else:
                print(Fore.RED + "TravelBot: I'll suggest again.")
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
            show_help()
            break

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommend')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Give weather info (say 'weather')")
    print(Fore.GREEN + "- Give news info (say 'news')")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to end.\n")

def weather():
    print(Fore.CYAN + "TravelBot: Hello! I can share weather info.")
    country = normalize_input(
        input(
            Fore.YELLOW +
            "Which country? [UAE, UK, USA, India] (type 'exit' or 'bye' to quit): "
        )
    )

    if country in ["exit", "bye"]:
        print(Fore.CYAN + "TravelBot: Thanks for chatting!")
    elif country == "uae":
        print(Fore.GREEN + "TravelBot: UAE is sunny and pleasant, around 20–25°C.")
    elif country == "uk":
        print(Fore.GREEN + "TravelBot: UK is cold and cloudy, 1–6°C with possible drizzle or snow.")
    elif country == "usa":
        print(Fore.GREEN + "TravelBot: USA weather varies—snowy east, stormy west, calmer central areas.")
    elif country == "india":
        print(Fore.GREEN + "TravelBot: India has cool north mornings and warm, sunny southern regions.")
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have weather data for that country.")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input:
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif "weather" in user_input:
            weather()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
