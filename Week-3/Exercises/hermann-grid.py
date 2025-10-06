# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

# start expyriment
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Hermann grid", background_colour = C_WHITE)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# CONSTANTS
colour = C_BLACK
max_width, max_height = exp.screen.size

def create_grid(n, size, space):
    W = n * size + (n - 1) * space
    H = n * size + (n - 1) * space

    # Check current configuration fits
    if W > max_width or H > max_height:
        raise ValueError("The target grid does not on fit the screen")

    squares = []

    for row in range(n):
        for col in range(n):
            ## Compute position and correct for offset from expy coords
            pos_x = col * (size + space) - (W - size) // 2 
            pos_y = row * (size + space) - (H - size) // 2 
            squares.append(
                stimuli.Rectangle(
                    size=(size, size), 
                    position=(pos_x, pos_y), 
                    colour=colour, 
                    corner_anti_aliasing=10)
                )
    return squares

def run_trial(squares):
    exp.screen.clear()
    for square in squares:
        square.present(False, False)
    exp.screen.update()

# Start running the experiment
control.start(subject_id=1)

# Present the shapes

# number of colums/rows , size , space
squares = create_grid(5, 90, 20)

run_trial(squares)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()
 
# End the current session and quit expyriment
control.end()