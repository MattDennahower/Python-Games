from random import choice
import os
from art import logo, vs
from game_data import data

# Track score and game status
score = 0
game_continue = True


def get_random_acc():
  """Returns a random account from the data list"""
  return choice(data)
  
def format_data(account):
  """Formats the account data into a printable format"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks the user's guess against the follower counts and returns True if they got it right. Or False if they guess wrong"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  """Main game function"""
  global score
  global game_continue
# Display art
print(logo)
# Generate a random account from the game data and check to make sure they are not the same
account_a = get_random_acc()
account_b = get_random_acc()
while game_continue:
  account_a = account_b
  account_b = get_random_acc()
  while account_a == account_b:
    account_b = get_random_acc()
  # Format the account data into a printable format
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  
  # Ask the user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if the user is correct
  # Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen between rounds
  _ = os.system('clear')
  # Redisplay the logo after clearing the screen
  print(logo)
  # Give user feedback on their guess
  # Score keeping

  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    game_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")

game()
