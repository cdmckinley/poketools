"""
Automates egg hatching for shiny hunting with Masuda method.
"""

import sys
import argparse
from math import ceil
from utils.controller import Controller
from configs import general


#############
# CONSTANTS #
#############

STEPS_CYCLE = 257


######################
# SCRIPT ENTRY POINT #
######################

if __name__ == "__main__":

    # Command line arguments
    parser = argparse.ArgumentParser()
    # Number of steps from the daycare desk to the right of the grandpa
    help = "Number of steps from the daycare desk to the right of the grandpa"
    parser.add_argument("steps_to_grandpa", type=int, help=help)
    # Egg cycles
    help = "Number of egg cycles before hatching for this specific Pokémon species."
    parser.add_argument("-e", "--egg-cycles", type=int, help=help)
    # Hatching steps
    help = "Number of steps before hatching for this specific Pokémon species."
    parser.add_argument("-s", "--egg-steps", type=int, help=help)
    # Number of steps
    # Presence of ability dividing the number of steps by two
    help = "Use this flag if a Pokémon in your party knows an ability dividing by 2 the number of steps to hatching."
    parser.add_argument("-a", "--ability", action="store_true", help=help)
    # Capture screenshot or video when shiny is found
    help = "Capture a video or screenshot once a shiny is found."
    parser.add_argument("-c", "--capture", help=help, choices=["video", "screenshot"])
    args = parser.parse_args()

    # Check if one and only one of the options -e and -s have been specified
    if (args.egg_cycles is None and args.egg_steps is None or
        args.egg_cycles is not None and args.egg_steps is not None):
        sys.stderr.write("Please specify one and only one of `-e` and `-s`.\n")
        exit(-1)

    # Initialize and connect virtual game controller, then go back to game
    controller = Controller()
    #controller.sync_and_go_back()
    controller.reconnect()

    # Main loop
    cycles = args.egg_steps / STEPS_CYCLE if args.egg_steps else args.egg_cycles
    cycles = ceil(cycles / 2) if args.ability else int(cycles)
    steps = cycles * STEPS_CYCLE - args.steps_to_grandpa
    is_shiny = False
    while not is_shiny:
        controller.macro(general.GET_ON_BIKE)
        controller.run_in_circles(steps)
        steps = cycles * STEPS_CYCLE
        # Shiny detection !
