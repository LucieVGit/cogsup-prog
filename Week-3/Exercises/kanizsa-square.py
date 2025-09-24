import expyriment

# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Initialize the experiment
exp = expyriment.design.Experiment(background_colour(c_grey))
control.initialize(exp)

width, height = exp.screen.size 

# Stimuli and design
s_size = int(width * 100 // 25) 
c_size = int(width * 100 // 5) 
square = stimuli.Rectangle(size=(size,size), colour=(225,0,0), position=(-width//2,height//2), line_width=5)
circle1 = stimuli.Circle(size=(size,size), colour=(225,0,0), position=(-width//2,height//2), line_width=5)
circle2 = stimuli.Circle(size=(size,size), colour=(225,0,0), position=(width//2,-height//2), line_width=5)
circle3 = stimuli.Circle(size=(size,size), colour=(225,0,0), position=(-width//2,-height//2), line_width=5)
circle4 = stimuli.Rectangle(size=(size,size), colour=(225,0,0), position=(width//2,height//2), line_width=5)

expyriment.control.start()

# Conduction of experiment

square1.present(clear=True, update=False)
square2.present(clear=False, update=False)
square3.present(clear=False, update=False)
square4.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

expyriment.control.end()

# voir sur git pour automatiser les positions