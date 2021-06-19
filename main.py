from turing import TuringMachine

inputSubtraction = '11-11111'
initialStateSubtraction = 'q0'
finalStateSubtraction = {'q9'}
transitionFuncSubtraction = {
    ('q0', '1'): ('q1', '_', 'R'),
    ('q0', '-'): ('q4', '_', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', '-'): ('q2', '-', 'R'),
    ('q2', '1'): ('q3', '-', 'L'),
    ('q2', '-'): ('q3', '-', 'R'),
    ('q3', '1'): ('q3', '1', 'L'),
    ('q3', '-'): ('q3', '-', 'L'),
    ('q3', '_'): ('q0', '_', 'R'),
    ('q4', '1'): ('q5', '1', 'S'),
    ('q4', '-'): ('q4', '_', 'R'),
    ('q4', '_'): ('q5', '_', 'S'),
}

turingSubtraction = TuringMachine(
    inputSubtraction,
    initialStateSubtraction,
    finalStateSubtraction,
    transitionFuncSubtraction
)

print("initial tape: " + turingSubtraction.get_tape())

while not turingSubtraction.final():
    turingSubtraction.step()

print("final tape: " + turingSubtraction.get_tape())


inputDivision = '110111111110'
initialStateDivision = 'q0'
finalStateDivision = {'q9'}
transitionFuncDivision = {
    ('q0', '1'): ('q1', '_', 'R'),
    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', '0'): ('q2', '0', 'R'),
    ('q2', 'X'): ('q2', 'X', 'R'),
    ('q2', '1'): ('q3', 'X', 'L'),
    ('q3', '0'): ('q3', '0', 'L'),
    ('q3', '1'): ('q3', '1', 'L'),
    ('q3', 'X'): ('q3', 'X', 'L'),
    ('q3', '_'): ('q0', '1', 'R'),
    ('q0', '0'): ('q4', '0', 'R'),
    ('q4', '1'): ('q4', '1', 'R'),
    ('q4', 'X'): ('q4', 'X', 'R'),
    ('q4', '0'): ('q5', '0', 'R'),
    ('q5', '1'): ('q5', '1', 'R'),
    ('q5', '_'): ('q6', '1', 'L'),
    ('q6', '1'): ('q6', '1', 'L'),
    ('q6', '0'): ('q6', '0', 'L'),
    ('q6', 'X'): ('q6', 'X', 'L'),
    ('q6', '_'): ('q0', '_', 'R'),
    ('q2', '0'): ('q7', '_', 'L'),
    ('q7', '1'): ('q7', '_', 'L'),
    ('q7', '0'): ('q7', '_', 'L'),
    ('q7', 'X'): ('q7', '_', 'L'),
    ('q7', '_'): ('q8', '_', 'R'),
    ('q8', '_'): ('q8', '_', 'R'),
    ('q8', '1'): ('q9', '1', 'R'),
}

turingDivision = TuringMachine(
    inputDivision,
    initialStateDivision,
    finalStateDivision,
    transitionFuncDivision
)

print("initial tape: " + turingDivision.get_tape())

while not turingDivision.final():
    turingDivision.step()

print("final tape: " + turingDivision.get_tape())
