from sys import argv

script, user_name, likable_thing = argv
prompt = '?: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like {likable_thing} {user_name}?")
likes = input(prompt)

print(f"Where you you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
  Alright, so you have said {likes} about liking {likable_thing}.
  You live in {lives}. Not sure where that is.
  And you have a {computer} computer. Nice.
  """)