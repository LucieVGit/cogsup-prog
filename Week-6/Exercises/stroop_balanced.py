from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import itertools, random


""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ["match", "mismatch"]
COLORS = ["red", "blue", "green", "orange"]

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do, F if they don't.\n
Press SPACE to continue.
"""
INSTR_MID = "You have finished a block of the experiment, they are 8 of them. Take a break then press SPACE to move on to the second half."
INSTR_END = "Well done!\nPress SPACE to quit the experiment."

FEEDBACK_CORRECT = "Good answer !"
FEEDBACK_INCORRECT = "Wrong answer !"

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)

    correct = key == K_j if trial_type == "match" else key == K_f

    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

def derangements(lst):
    ders = []
    for perm in itertools.permutations(lst):
        if all(original != perm[idx] for idx, original in enumerate(lst)):
            ders.append(perm)
    return ders

PERMS = derangements(COLORS)

control.start()

subject_id = exp.subject
order = (subject_id - 1) % len(PERMS)
perm = PERMS[order]

base = (
    [{"trial_type" : "match", "word": c, "color": c} for c in COLORS] +
    [{"trial_type" : "mismatch", "word": w, "color": c} for w,c in zip(COLORS, perm)]
)

block_repetitions = N_TRIALS_IN_BLOCK // len(base)
blocks = []

for b in range(1, N_BLOCKS + 1):
    b_trials = base * block_repetitions
    random.shuffle(b_trials) ####################################### NO
    trials = [{"block_id": b, "trial_id":i, **t} for i, t in enumerate(b_trials, 1)]
    blocks.append(trials) 

present_instructions(INSTR_START)
for block_id, block in enumerate(blocks, 1):
    for trial in block:
        run_trial(**trial)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)
 
control.end()