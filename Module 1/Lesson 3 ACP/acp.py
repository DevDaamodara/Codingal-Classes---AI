import re
import random
from colorama import Fore, init

init(autoreset=True)

# Data structures
DESTINATIONS = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

JOKES = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

WEATHER_DATA = {
    "uae": "UAE is sunny and pleasant, around 20–25°C.",
    "uk": "UK is cold and cloudy, 1–6°C with possible drizzle or snow.",
    "usa": "USA weather varies—snowy east, stormy west, calmer central areas.",
    "india": "India has cool north mornings and warm, sunny southern regions."
}

PACKING_TIPS = [
    "Pack versatile clothes.",
    "Bring chargers/adapters.",
    "Check the weather forecast."
]

# Command mappings
COMMANDS = {
    "recommend": "Get travel destination suggestions",
    "pack": "Get packing tips",
    "joke": "Hear a travel joke",
    "weather": "Get weather information",
    "help": "Show available commands",
    "exit": "Exit the chat",
    "bye": "Exit the chat"
}

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    """Suggest travel destinations based on user preference."""
    valid_types = ", ".join(DESTINATIONS.keys())
    while True:
        print(Fore.CYAN + f"TravelBot: Choose from: {valid_types}")
        preference = normalize_input(input(Fore.YELLOW + "You: "))

        if preference in DESTINATIONS:
            suggestion = random.choice(DESTINATIONS[preference])
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
            print(Fore.RED + f"TravelBot: Sorry, I don't have that type. Try: {valid_types}")
            break

def packing_tips():
    """Provide packing tips for a trip."""
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    for tip in PACKING_TIPS:
        print(Fore.GREEN + f"- {tip}")

def tell_joke():
    """Tell a random travel joke."""
    print(Fore.YELLOW + f"TravelBot: {random.choice(JOKES)}")

def show_help():
    """Display available commands."""
    print(Fore.MAGENTA + "\nI can:")
    for command, description in COMMANDS.items():
        if command not in ["exit", "bye"]:
            print(Fore.GREEN + f"- {description} (say '{command}')")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to end.\n")

def weather():
    """Provide weather information for selected countries."""
    print(Fore.CYAN + "TravelBot: Which country?")
    valid_countries = ", ".join(WEATHER_DATA.keys()).upper()
    print(Fore.CYAN + f"Available: {valid_countries}")
    
    country = normalize_input(
        input(Fore.YELLOW + "You: ")
    )

    if country in ["exit", "bye"]:
        print(Fore.CYAN + "TravelBot: Thanks for chatting!")
    elif country in WEATHER_DATA:
        print(Fore.GREEN + f"TravelBot: {WEATHER_DATA[country]}")
    else:
        print(Fore.RED + f"TravelBot: Sorry, I don't have weather data for that country. Try: {valid_countries}")

def dispatch_command(user_input):
    """Route user input to appropriate command handler."""
    command_handlers = {
        ("recommend", "suggest"): recommend,
        ("pack", "packing"): packing_tips,
        ("joke",): tell_joke,
        ("weather",): weather,
        ("help",): show_help,
    }
    
    for keywords, handler in command_handlers.items():
        if any(keyword in user_input for keyword in keywords):
            handler()
            return True
    
    return False

def chat():
    """Main chat loop for TravelBot."""
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))

        if user_input in ["exit", "bye"]:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        elif not dispatch_command(user_input):
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
