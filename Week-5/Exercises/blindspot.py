from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """


r = 75

def run_trial():
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()

    radius = r
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)

    if exp.keyboard.wait(K_DOWN)
        fixation = [
            stimuli.FixCross(position=[x, y - 20])
        ]
    elif exp.keyboard.wait(K_UP)
        fixation = [
            stimuli.FixCross(position=[x, y + 20])
        ]
    elif exp.keyboard.wait(K_LEFT)
        fixation = [
            stimuli.FixCross(position=[x - 20, y])
        ]
    elif exp.keyboard.wait(K_RIGHT)
        fixation = [
            stimuli.FixCross(position=[x + 20, y])
        ]
    elif exp.keyboard.wait(49)
        fixation = [
            stimuli.FixCross(size=(a + 10, z + 10))
        ]
    elif exp.keyboard.wait(50)
        fixation = [
            stimuli.FixCross(size=(a - 10, z - 10))
        ]
    else:
        #"Please press an arrow, 1 or 2 to move or change the size of the circle")


control.start(subject_id=1)

run_trial()
    
control.end()