import requests
import random

# Function to get a random list of cats
def get_random_cats(n=3):
    # Get the list of all cat breeds from The Cat API
    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url, headers={
        'x-api-key': 'live_U2bm55iqL8kzi9Qf7E14kkhGgMUAz072ArB2Ib9eHzT64558BncktZ58uYUEOIoE'})

    # Check if the request was successful
    if response.status_code == 200:
        breeds = response.json()

        # Pick `n` random breeds from the list
        random_cats = random.sample(breeds, n)

        # Create a list of cat dictionaries with relevant information
        cats = [{
            'name': cat['name'],
            'life_span': cat.get('life_span', 'N/A'),
            'intelligence': cat.get('intelligence', 'N/A'),
            'affection_level': cat.get('affection_level', 'N/A'),
            'social_needs': cat.get('social_needs', 'N/A')
        } for cat in random_cats]

        return cats

# Function to display cats and let the user pick one
def choose_cat(cats):
    print("Please choose one of the following cats:\n")
    for i, cat in enumerate(cats):
        print(f"{i + 1}. {cat['name']} ")

    # Ask the user to pick a cat by number
    choice = input("\nEnter the number of the cat you want to choose (1, 2, or 3): ")

    # Ensure the choice is valid
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(cats):
            return cats[choice]
        else:
            print("Invalid choice! Please enter a valid number.")
            return choose_cat(cats)
    else:
        print("Invalid input! Please enter a number.")
        return choose_cat(cats)


# Function to run the game
def run():
    # Get 3 random cats to choose from
    cats = get_random_cats()

    if cats:
        # Let the user pick a cat
        my_cat = choose_cat(cats)
        print(f"\nYou chose {my_cat['name']}!\n")

        # Stat choice prompt with actual values
        stat_prompt = 'Which stat do you want to use?\n(life_span: {}, intelligence: {}, affection_level: {}, social_needs: {})\n'.format(
            my_cat['life_span'], my_cat['intelligence'], my_cat['affection_level'], my_cat['social_needs']
        )

        # Ask for stat choice
        stat_choice = input(stat_prompt)

        # Ensure the stat choice is valid
        if stat_choice not in my_cat:
            print(f"Invalid choice: {stat_choice}")
            return

        # Get a random opponent cat
        opponent_cat = random.choice(cats)  # You can get a fresh cat from get_random_cats() if desired
        print(f'The opponent chose {opponent_cat["name"]} and their {stat_choice} was {opponent_cat[stat_choice]}.')

        my_stat = my_cat[stat_choice]
        opponent_stat = opponent_cat[stat_choice]

        # Handle N/A stats or compare numeric values
        if my_stat == 'N/A' or opponent_stat == 'N/A':
            print("One of the chosen stats is not available.")
        else:
            # Compare the stats directly (they should be comparable, like intelligence)
            if my_stat > opponent_stat:
                print('You Win!')
            elif my_stat < opponent_stat:
                print('You Lose!')
            else:
                print('Draw!')
    else:
        print("Failed to get cats.")


# Run the game
run()



