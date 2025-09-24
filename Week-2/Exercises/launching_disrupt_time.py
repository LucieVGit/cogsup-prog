# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

square_left = stimuli.Rectangle(size=(50,50), colour = (225,0,0), position = (-200, 0))
square_right = stimuli.Rectangle(size=(50,50), colour = (0,225,0), position = (0, 0)) 

# Start running the experiment
control.start(subject_id=1)

# Present the squares
square_left.present(clear=True, update=False)
square_right.present(clear=False, update=True)

x = -50
n = -10 # I feel that x pixels is the threshold at which it does not disrupt my impression of causality
t = x + n

while square_left.position[0] < t :  
    square_left.move((5, 0))        # move 5 pixels to the right
    square_left.present(clear=True, update=False)
    square_right.present(clear=False, update=True)
    exp.clock.wait(15) 

while square_right.position[0] < 400 :
    square_right.move((5, 0))        # move 5 pixels to the right
    square_right.present(clear=True, update=False)
    square_left.present(clear=False, update=True)
    exp.clock.wait(15) 

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()