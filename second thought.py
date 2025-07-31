import random

def get_user_info():
    questions = [
        ("What’s your favorite color? ", "favorite_color"),
        ("What’s your favorite food? ", "favorite_food"),
        ("Which city do you live in? ", "city"),
        ("Which SHS did you attend? ", "shs"),
        ("What’s your favorite soccer team? ", "soccer_team"),
        ("What’s your hobby? ", "hobby"),
        ("What’s your talent? ", "talent")
    ]
    random.shuffle(questions)
    
    name = input("Hey there! What's your full name? ")
    age = input("How old are you? ")

    answers = {'name': name, 'age': age}
    for q, key in questions[:4]:  # Ask 4 random questions
        answers[key] = input(q)

    return answers

def generate_summary(data):
    return f"""Hello, {data['name']}! 
    You're {data['age']} years old and here's a bit about you:
- "When it comes to your favourites, you shine with": {data.get('favorite_color', 'N/A')}
- never say no to {data.get('favorite_food', 'N/A')}
- You're based in {data.get('city', 'N/A')}
- Throwback to SHS at {data.get('shs', 'N/A')}
- cheering loud for {data.get('soccer_team', 'N/A')}
- You've got a flair for {data.get('hobby', 'N/A')}
- Your talent for {data.get('talent', 'N/A')} is truly one-of-a-kind
"""

def main():
    while True:
        user_data = get_user_info()
        summary = generate_summary(user_data)
        print("\nHere's your fun profile summary:\n")
        print(summary)

        save = input("Would you like to save this summary to a .txt file? (yes/no): ").lower()
        if save == 'yes':
            filename = f"{user_data['name'].replace(' ', '_')}.txt"
            with open(filename, 'w') as file:
                file.write(summary)

        rating = input("Rate this assistant from 1 to 5 stars: ")
        if save == 'yes':
            with open(filename, 'a') as file:
                file.write(f"\nRating: {rating} stars")

        restart = input("\nWould you like to restart and try new questions? (yes/no): ").lower()
        if restart != 'yes':
            print("Thanks for using the assistant. Goodbye!")
            break

main()

