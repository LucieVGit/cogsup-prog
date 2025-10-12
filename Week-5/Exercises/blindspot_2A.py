from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.initialize(exp)

r = 75 #radius start
L = 1
R = 2
started_sides = {L: False, R: False}

""" Stimuli """
def make_circle(r, pos):
    c = stimuli.Circle(radius = r, position= pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side):
    global r, pos
    
    if side == L:
        a = -600
        eye = "left eye"
        # closed_side = "right"
    elif side == R:
        a = 600
        eye = "right eye"
        # closed_side = "left"
    else:
        raise ValueError("side must be L or R")
    
    if not started_sides.get(side, False):
        pos = (a * -1, 0)  # circle opposite to fixation
        started_sides[side] = True

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=(a, 0))
    fixation.preload()

    circle = make_circle(r, pos) 

    x, y = circle.position

    fixation.present(True, False)
    circle.present(False, True)

    key, _ = exp.keyboard.wait() # got help from chatGPT for this line

    if key == K_DOWN:
        pos = (x, y - 20)
    elif key == K_UP:
        pos = (x, y + 20)
    elif key == K_LEFT:
        pos = (x - 20, y)
    elif key == K_RIGHT:
        pos = (x + 20, y)
    elif key == 49: 
        r += 10
    elif key == 50:
        r -= 10
    elif key == K_SPACE:
        return "quit", pos, r, eye # got help from chatGPT for this line
    else:
        text_error = stimuli.TextScreen('Error', 'Please press an arrow, 1 or 2 to move \nor change the size of the circle', heading_size = 100, heading_colour=(225,0,0), text_size= 30, text_colour= C_BLACK)
        text_error.present(clear=True, update=True)
        exp.keyboard.wait()

    return "continue", pos, r, eye

control.start(subject_id=1)

text_start = stimuli.TextScreen("Find your blind spot", "Welcome in this expyriment ! \n_ \nToday you are going to find your blind spot, you will have in front of you a fixation cross and a circle that you will be able to move and change its size. " \
"To find your blind spot, please close your eye on the same side as the circle while facing the screen and look at the cross. \nThen, press an arrow to move the circle up, down, left or right. Press 1 to make the circle bigger and 2 to make it smaller." \
"\nWhen the circle disappears completely, you have found your blind spot, congratulations !! \_(^v^)_\ \nYou can then press space to test your other eye. \n_ \n_ \n_ \nPress space to start. :)", heading_size = 60, heading_colour=(0,0,128), text_size= 30, text_colour=(128,0,128))
text_start.present(clear=True, update=True)
exp.keyboard.wait()
# I put a f string here that changed automatically {closed_eye} but because it it defined after it doesn't work anymore

results = []

while True :
    status, pos, r, eye = run_trial(L)
    if status == "quit": 
        results.append((eye, r, pos))
        break

while True :
    status, pos, r, eye = run_trial(R)
    if status == "quit":
        results.append((eye, r, pos))
        break

exp.add_data_variable_names(["Eye", "Radius", "Coordinates"])

for entry in results:
    exp.data.add(entry)


# End the current session and quit expyriment
control.end()