# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Launching function")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Start running the experiment
control.start(subject_id=1)

def launch(time, space, step, pause_after):
    square_left = stimuli.Rectangle(size=(50,50), colour = (225,0,0), position = (-500, 0))
    square_right = stimuli.Rectangle(size=(50,50), colour = (0,225,0), position = (0, 0)) 
    # Present the squares
    square_left.present(clear=True, update=False)
    square_right.present(clear=False, update=True)
    n = -50 + space
    while square_left.position[0] < n :
        square_left.move((5, 0))        # move 5 pixels to the right
        square_left.present(clear=True, update=False)
        square_right.present(clear=False, update=True)
        exp.clock.wait(15) 

    exp.clock.wait(time) 

    while square_right.position[0] < 500 :
        square_right.move((step, 0))        # move 5 pixels to the right
        square_right.present(clear=True, update=False)
        square_left.present(clear=False, update=True)
        exp.clock.wait(15) 

    if pause_after:
        exp.keyboard.wait()  # Leave it on-screen until a key is pressed
    

# function(time, space, speed)
launch(0, 0, 5, False) # Michottean launching
launch(100, 0, 5, False) # launching with a temporal gap
launch(0, -20, 5, False) # launching with a spatial gap
launch(0, 0, 15, True) # triggering (speed)

# End the current session and quit expyriment
control.end()