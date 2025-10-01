import expyriment

# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Initialize the experiment
exp = design.Experiment()
control.initialize(exp)

width, height = exp.screen.size 

# Stimuli and design
size = int(width // 20) # 5 // 100 = 20 donc ca revient a diviser par 20) 
square1 = stimuli.Rectangle(size=(size,size), colour=(225,0,0), position=(-width//2 + size //2, height//2 - size //2), line_width=5)
square2 = stimuli.Rectangle(size=(size,size), colour=(225,0,0), position=(width//2 - size //2,-height//2 + size //2), line_width=5)
square3 = stimuli.Rectangle(size=(size,size), colour=(225,0,0), position=(-width//2 + size //2,-height//2 + size //2), line_width=5)
square4 = stimuli.Rectangle(size=(size,size), colour=(225,0,0), position=(width//2 - size //2,height//2 - size //2), line_width=5)

control.start()

# Conduction of experiment

square1.present(clear=True, update=False)
square2.present(clear=False, update=False)
square3.present(clear=False, update=False)
square4.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

control.end()

# voir sur git pour automatiser les positions