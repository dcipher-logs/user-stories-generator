from logos import logo, logo2

EXAMPLE = "As a user, I want to turn on a light, so that I can see my surroundings."

print(logo)
print("Welcome to the User Story Generator!\n")
print("Here is an example user story ⬇️")
print(EXAMPLE)

print("\n" * 3)
print("Now let's create your own!")

go_again = True
user_stories = []

while go_again:
    as_a = input("As a ___ (type your target audience): ").lower()
    i_want_to = input(f"As a {as_a}, I want to ___ (type the action your target audience wants to perform): ").lower()
    so_that = input(f"As a {as_a}, I want to {i_want_to} so that ___ (type reasoning for desired action):  ")

    print("\n" * 3)
    user_story = f"As a {as_a}, I want to {i_want_to} so that {so_that}."
    user_stories.append(user_story)

    print(logo2)
    print(user_story)
    print("\n" * 3)

    prompt = input("Would you like to make another user story? Type 'y' or 'n': ").lower()
    print("\n")

    if prompt == 'n':
        print("Below are the user stories you created! ⬇️\n")
        for story in user_stories:
            print(story)
            with open('user_stories.txt', mode='a') as user_stories:
                user_stories.write(f"\n{story}")
        go_again = False
    elif prompt != 'y':
        print("Please type the correct input")
        print(prompt)



