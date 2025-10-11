from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_WHITE, C_BLACK, C_BLUE, C_YELLOW, C_RED
from drawing_functions import *

exp = design.Experiment(name = "Ternus illusion", background_colour = C_WHITE)

control.set_develop_mode()
control.initialize(exp)

display = 500

def run_trial(radius, ISI, color_tags):
    position = [(-300, 0), (-100, 0), (100, 0), (300, 0)]

    move1_circle, left_circle, right_circle, move2_circle = [
        stimuli.Circle(radius, colour = C_BLACK, position = pos)
        for pos in position
    ]

    yellow_tag1 = red_tag = blue_tag = yellow_tag2 = None  # default (got help from ChatGPT for that line)

    if color_tags:
        colour_tag = [C_YELLOW, C_RED, C_BLUE, C_YELLOW]
        radius_tag = radius / 5
        yellow_tag1, red_tag, blue_tag, yellow_tag2 = [
            stimuli.Circle(radius_tag, colour = col, position = pos)
            for col, pos in zip(colour_tag, position)
        ]

    return(ISI, move1_circle, left_circle, right_circle, move2_circle, yellow_tag1, red_tag, blue_tag, yellow_tag2)


ISI, move1_circle, left_circle, right_circle, move2_circle, yellow_tag1, red_tag, blue_tag, yellow_tag2 = run_trial(radius = 75, ISI = display, color_tags = True)
# got help from ChatGPT for the list concept because I first wanted to pop from a tuple but that is not possible

stim_list1 = [move1_circle, left_circle, right_circle, yellow_tag1, red_tag, blue_tag]
stim_list2 = [left_circle, right_circle, move2_circle, red_tag, blue_tag, yellow_tag2]

# DRAW

    exp.screen.clear()
    for stim in stim_list2:
        stim.present(False, False)
    exp.screen.update()

    exp.clock.wait(ISI)

    if exp.keyboard.check(K_SPACE): # inside the loop
        break


exp.keyboard.wait()
control.end()

