# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100.

import random
import textwrap
import sys
import time

INTRODUCTION = """

WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THE GOVERNMENT WANTS IT FOR THEIR GAIN.

WE CAN'T LET THAT HAPPEN.

ONE GOAL: SURVIVAL... and  THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU.

"""
WIN = """
You pressed the button to open the gate.
This isn't the first time you've done this,
so you know hot to time it exactly.
Just ast the doors close, you slide right into HQ.
You know you did the right thing, the government 
would have just torn the car apart.
They don't know its secrets...
that it holds the key to different worlds.
As you step out of the vehicle, Fido runs up to you.
"Thank you for saving me," he says.
As you take a couple of steps away from teh car,
it makes a strange sound.
It changes it shape.
You've seen it before, but only on TV.
"...Bumblebee???"


-----GAME OVER-----
"""

LOSE_HUNGER = """

Your stomach is empty.
Who knew that what the doctor said was true,
that human/robot hybrids would need tofu to sustain themselves.
Your robot systems start to shut down.
Your human eyes close.
The last thing that you hear are sirens.
They gotchu. They got the car.
We FAILED...

"""

LOSE_AGENTS = """

The agents have closed in on you.
There are at least 20 cars surrounding you.
The lead car bumps your passenger side.
You manage to correct your steering
to keep you from crashing.

You didn't see the agents car beside you.
The driver bumps your car.
And that's it.

You spin out of control.
The car flips over at least two times.
or more... you lost count.

Sirens.

"Are they alive?" someone asks.
"Doesn't matter. all we wanted was the car."
You see a dog walking out of the car.
"Was it in the car the whole time?" You
think to yourself.

The dog looks up at the officers.
"You will never stop the revolution."
"Did the dog just talk?" You think to yourself.

You drift off into unconsciousness
"""
LOSE_FUEL = """

You ran out of fuel.
Car stops.
Your bad.
"""
CHOICES = """
     -----
     A. Eat some tofu
     B. Drive at a moderate speed
     C. Speed ahead at full throttle.
     D. Stop for fuel at a refuelling station.
        (No food available)
     E. Status Check
     Q. QUIT
     -----
"""


def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)


def main():
    # Show introduction
    type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_TOFU_LEVEL = 3
    Max_DISTANCE_TRAVELED = 100
    TOFU_CHANCE = 0.03

    # variables
    done = False
    km_traveled: int = 0  # 100km traveled is the goal
    agents_distance = -20
    turns = 0  # amount of turns taken
    tofu = MAX_TOFU_LEVEL
    fuel = MAX_FUEL_LEVEL
    hunger =0  # hunger increases with number

    while not done:
        # Random events
        # Fido
        if tofu < 3:
            if random.random() < TOFU_CHANCE:
                # Fido pops up says something and refills tofu
                tofu = MAX_TOFU_LEVEL
                print("\n******** Your tofu is magically refilled!\n******** \"You're welcome!\" a voice "
                      "says.\n******** It's Fido.******** He's using his tofu cooking skills.")

        # Check if reached END GAME
        if km_traveled > Max_DISTANCE_TRAVELED:
            # Win
            # Print win scenario (typing way)
            type_text_output(WIN)
            # Break from while loop
            break
        elif hunger > 45:
            # LOSE - TOO HUNGRY
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            # Print losing hunger scenario
            break

        elif agents_distance >= 0:
            # LOSE - AGENTS REACHED YOU
            # print losing agents scenario
            time.sleep(2)
            type_text_output(LOSE_AGENTS)
            break
        elif fuel <= 0:
            # LOSE - Ran out of fuel
            # print losing fuel scenario
            time.sleep(2)
            type_text_output(LOSE_FUEL)



        # Showing hunger
        if hunger > 40:
            print("\n******** your stomach starts hurting. You need to eat something soon.")
        elif hunger > 20:
            print("\n-------- You stomach is rumbling")

        # Give the player their choices
        time.sleep(1)
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.,?")
        if users_choice == "a":
            # Eat
            if tofu > 0:
                tofu -= 1
                hunger = 0
                # feedback to player
                print("\n-------- Mmmmmmm. Soybean goodness.\n-------- Your hunger is sated.\n")
            else:
                print("\n-------- You have no tofu left.\n")
        elif users_choice == "b":
            # Moderate speed
            player_distance_now = random.randrange(7, 15)
            agents_distance_now = random.randrange(7, 15)
            # Burn fuel
            fuel -= random.randrange(4, 8)
            # Player distance traveled
            km_traveled += player_distance_now
            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)
            # Feedback to Player
            print(f"\n-------- You slowly drove {player_distance_now}kms.\n")
        elif users_choice == "c":
            # Drive Fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)
            # Burn fuel
            fuel -= random.randrange(5, 11)
            # Player distance traveled
            km_traveled += player_distance_now
            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)
            # Feedback to Player
            print(f"\n-------- You sped ahead {player_distance_now}kms!\n")
        elif users_choice == "d":
            # Refuel

            # Fill the fuel tank
            fuel = MAX_FUEL_LEVEL
            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)
            # Give the user feedback
            print("\n-------- You filled the fuel tank.\n-------- The agents got closer...")

        elif users_choice == "e":
            print(f"\t---Status---")
            print(f"km traveled: {km_traveled}")
            print(f"Fuel left: {fuel}")
            print(f"Agents are {abs(agents_distance)}km behind you")
            print(f"You have {tofu} tofu left.")
            print("\t------------")
        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)
            turns += 1
        # pause
        time.sleep(1)

    # Outroduction
    print("Thanks for playing! Please play again. :D")
    print(f"you got to the ending in {turns} turns.")


if __name__ == '__main__':
    main()
