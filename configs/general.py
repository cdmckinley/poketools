# General macros used in any scenario

GO_BACK_TO_GAME_AFTER_SYNC = """
2s
A 0.1s
1s
B 0.1s
1s
DPAD_UP 0.1s
0.5s
DPAD_LEFT 1s
A 0.1s
1s
"""


##########################
# MACROS FOR SHINY RESET #
##########################

SELECT_USER = """
LOOP {}
    DPAD_RIGHT 0.1s
    0.2s
A 0.1s
"""

SLEEP_MODE = """
HOME 2s
A 0.1s
"""

BUSY_WAIT = """
LOOP {}
    A 0.1s
    0.1s
"""

BUSY_WAIT_B = """
LOOP {}
    B 0.1s
    0.1s
"""


#########################################
# MACROS FOR CAPTURING SCREENSHOT/VIDEO #
#########################################

SCREENSHOT = """
CAPTURE 0.1s
"""

VIDEO = """
CAPTURE 1.0s
"""


#######################
# MACROS FOR EXP FARM #
#######################

STEPS_CIRCLE = """
PLUS 0.1s
DPAD_RIGHT 0.1s
LOOP {}
    L_STICK@+100+000 0.13s
    L_STICK@+000+100 0.13s
    L_STICK@-100+000 0.13s
    L_STICK@+000-100 0.13s
L_STICK@+000+000 0.1s
"""

BATTLE = """

"""