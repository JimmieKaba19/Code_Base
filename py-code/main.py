#python
import random
from dice import display_dice

# Function to roll a six-sided die
def roll_die():
    return random.randint(1, 6)

# Function to determine if a roll results in a hit, critical hit, or miss
def roll_result(roll):
    if len(set(roll)) == 1:  # Three of a kind
        if roll[0] in [1, 3, 5]:
            return "miss"
        else:
            return "critical hit"
    elif len(set(roll)) == 2:  # Pair
        return "hit"
    else:
        return "normal"

# Initialize player and dragon health
player_health = 100
dragon_health = 100

# Initialize battle statistics
total_battles = 0
player_wins = 0
dragon_wins = 0

# Main game loop
while True:
    # Prompt the player for the number of battle rounds
    num_rounds = int(input("Let's begin: \n Enter the number of battle rounds (1-5 inclusive): "))
    
    # Validate input
    if num_rounds < 1 or num_rounds > 5:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    # Initialize round counter
    round_num = 1
    
    # Individual battle loop
    while round_num <= num_rounds:
        print(f"\nRound {round_num} - Player vs Dragon")
        
        # Roll dice for player and dragon
        player_roll = [roll_die() for _ in range(5)]
        dragon_roll = [roll_die() for _ in range(5)]
        
        # Determine roll results
        player_result = roll_result(player_roll)
        dragon_result = roll_result(dragon_roll)
        
        # Calculate damage dealt
        player_damage = sum(player_roll) * (2 if player_result == "hit" else 3 if player_result == "critical hit" else 1)
        dragon_damage = sum(dragon_roll) * (2 if dragon_result == "hit" else 3 if dragon_result == "critical hit" else 1)
        
        # Display rolls and damage
        print("\nPlayer rolls:")
        display_dice(player_roll)
        print("Dragon rolls:")
        display_dice(dragon_roll)
        print(f"\nPlayer {player_result}: {player_damage} damage")
        print(f"Dragon {dragon_result}: {dragon_damage} damage")
        
        # Update health
        player_health -= dragon_damage
        dragon_health -= player_damage
        
        # Display health
        print(f"\nPlayer health: {player_health}")
        print(f"Dragon health: {dragon_health}")
        
        # Increment round counter
        round_num += 1
    
    # Update battle statistics
    total_battles += 1
    if player_health > dragon_health:
        player_wins += 1
    else:
        dragon_wins += 1
    
    # Ask if the player wants to continue playing
    play_again = input("\nDo you want to battle another dragon? (yes/no): ")
    if play_again.lower() != "yes":
        break

# Display game summary
print("\nGame Summary:")
print(f"Total battles: {total_battles}")
print(f"Player wins: {player_wins}")
print(f"Dragon wins: {dragon_wins}")