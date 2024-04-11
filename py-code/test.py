import random

def main():
    print("Welcome to Dragon Battleground!")
    
    games_played, games_won, games_lost, games_drawn, dragons_killed = 0, 0, 0, 0, 0
    
    while input("Would you like to play Dragon Battleground [y|n]? ").lower() == 'y':
        games_played += 1
        player_health, dragon_health = 100, 100
        round_number = 1

        rounds = int(input("Please enter number of battle rounds (1-5): "))
        while rounds < 1 or rounds > 5:
            print("Must be between 1-5 inclusive.")
            rounds = int(input("Please enter number of battle rounds (1-5): "))

        while round_number <= rounds and player_health > 0 and dragon_health > 0:
            print(f"\n-- Round: {round_number} --")
            player_roll, dragon_roll = roll_dice(), roll_dice()

            print("Player rolled:")
            display_dice(player_roll)
            print("Dragon rolled:")
            display_dice(dragon_roll)

            player_damage = calculate_damage(player_roll)
            dragon_damage = calculate_damage(dragon_roll)
            player_health, dragon_health = max(0, player_health - dragon_damage), max(0, dragon_health - player_damage)

            print(f"> Player - Damage taken: {dragon_damage} - Current health: {player_health}")
            print(f"> Dragon - Damage taken: {player_damage} - Current health: {dragon_health}")

            round_number += 1

        if player_health > dragon_health:
            print("* Player wins! *")
            games_won += 1
            if dragon_health <= 0: dragons_killed += 1
        elif dragon_health > player_health:
            print("* Dragon wins! *")
            games_lost += 1
        else:
            print("* Draw! *")
            games_drawn += 1

    print("\nGame Summary")
    print(f"You played {games_played} games")
    print(f"  |--> Games won:    {games_won}")
    print(f"  |--> Games lost:   {games_lost}")
    print(f"  |--> Games drawn:  {games_drawn}")
    print(f"  |--> Dragons killed:  {dragons_killed}")
    print("\nThanks for playing Dragon Battleground!")

def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

def calculate_damage(roll):
    damage = sum(roll)
    roll_counts = {i: roll.count(i) for i in set(roll)}
    crit_miss = {1, 3, 5}

    if any(count >= 3 for count in roll_counts.values()):
        for num, count in roll_counts.items():
            if count >= 3:
                if num in crit_miss:
                    print("-- Swing and miss - no damage inflicted!")
                    return 0
                else:
                    print("-- Critical hit - triple the damage!")
                    return damage * 3
    elif 2 in roll_counts.values():
        print("-- Hit - double the damage!")
        return damage * 2
    else:
        print("-- Standard damage.")
    return damage

def display_dice(dice_rolls):
    dice_representation = {
        1: ("     ", "  *  ", "     "),
        2: ("*    ", "     ", "    *"),
        3: ("*    ", "  *  ", "    *"),
        4: ("*   ", "     ", "   *"),
        5: ("*   ", "  *  ", "   *"),
        6: ("*   ", "   ", "   *"),
    }
    for row in zip(*(dice_representation[dice] for dice in dice_rolls)):
        print(" ".join(row))

#if __name__ == "main":
main()