from time import sleep
from turing import TuringMachine
import keyboard

# # ADDITION
# inputAddition = '111+111'
# initialStateAddition = 'q0'
# finalStateAddition = {'q3'}
# transitionFuncAddition = {
#     ('q0', '0'): ('q0', '_', 'R'),
#     ('q0', '1'): ('q0', '1', 'R'),
#     ('q0', '+'): ('q1', '1', 'R'),
#     ('q1', '0'): ('q2', '0', 'L'),
#     ('q1', '1'): ('q1', '1', 'R'),
#     ('q1', '_'): ('q2', '_', 'L'),
#     ('q2', '0'): ('q2', '_', 'R'),
#     ('q2', '1'): ('q2', '_', 'R'),
#     ('q2', '_'): ('q3', '_', 'S'),
# }

# turingAddition = TuringMachine(
#     inputAddition,
#     initialStateAddition,
#     finalStateAddition,
#     transitionFuncAddition
# )

# print("\ninitial tape addition     : " + turingAddition.get_tape())

# while not turingAddition.final():
#     turingAddition.step()

# print("final tape addition       : " + turingAddition.get_tape())

# # SUBTRACTION
# inputSubtraction = '11-11111'
# initialStateSubtraction = 'q0'
# finalStateSubtraction = {'q5'}
# transitionFuncSubtraction = {
#     ('q0', '1'): ('q1', '_', 'R'),
#     ('q0', '-'): ('q4', '_', 'R'),
#     ('q1', '1'): ('q1', '1', 'R'),
#     ('q1', '-'): ('q2', '-', 'R'),
#     ('q2', '1'): ('q3', '-', 'L'),
#     ('q2', '-'): ('q2', '-', 'R'),
#     ('q3', '1'): ('q3', '1', 'L'),
#     ('q3', '-'): ('q3', '-', 'L'),
#     ('q3', '_'): ('q0', '_', 'R'),
#     ('q4', '1'): ('q5', '1', 'S'),
#     ('q4', '-'): ('q4', '_', 'R'),
#     ('q4', '_'): ('q5', '_', 'S'),
# }

# turingSubtraction = TuringMachine(
#     inputSubtraction,
#     initialStateSubtraction,
#     finalStateSubtraction,
#     transitionFuncSubtraction
# )

# print("\ninitial tape subtraction  : " + turingSubtraction.get_tape())

# while not turingSubtraction.final():
#     turingSubtraction.step()

# print("final tape subtraction    : " + turingSubtraction.get_tape())

# # MULTIPLICATION
# inputMultiplication = '111*11'
# initialStateMultiplication = 'q0'
# finalStateMultiplication = {'q9'}
# transitionFuncMultiplication = {
#     ('q0', '0'): ('q8', '_', 'R'),
#     ('q0', '1'): ('q1', '_', 'R'),
#     ('q1', '1'): ('q2', '_', 'R'),
#     ('q1', '*'): ('q7', '_', 'R'),
#     ('q2', '1'): ('q2', '1', 'R'),
#     ('q2', '*'): ('q3', '*', 'R'),
#     ('q3', '1'): ('q4', 'M', 'R'),
#     ('q3', 'N'): ('q6', 'N', 'L'),
#     ('q4', '1'): ('q4', '1', 'R'),
#     ('q4', 'N'): ('q4', 'N', 'R'),
#     ('q4', '_'): ('q5', 'N', 'L'),
#     ('q5', '1'): ('q5', '1', 'L'),
#     ('q5', 'M'): ('q3', '1', 'R'),
#     ('q5', 'N'): ('q5', 'N', 'L'),
#     ('q6', '1'): ('q6', '1', 'L'),
#     ('q6', '*'): ('q6', '*', 'L'),
#     ('q6', '_'): ('q1', '_', 'R'),
#     ('q7', '0'): ('q7', '_', 'R'),
#     ('q7', '1'): ('q7', '1', 'R'),
#     ('q7', 'N'): ('q7', '1', 'R'),
#     ('q7', '_'): ('q9', '_', 'S'),
#     ('q8', '0'): ('q8', '_', 'R'),
#     ('q8', '1'): ('q8', '_', 'R'),
#     ('q8', '*'): ('q8', '_', 'R'),
#     ('q8', '_'): ('q9', '_', 'S'),
# }

# turingMultiplication = TuringMachine(
#     inputMultiplication,
#     initialStateMultiplication,
#     finalStateMultiplication,
#     transitionFuncMultiplication
# )

# print("\ninitial tape mutiplication: " + turingMultiplication.get_tape())

# while not turingMultiplication.final():
#     turingMultiplication.step()

# print("final tape mutiplication  : " + turingMultiplication.get_tape())

# # DIVISION
# inputDivision = '110111111110'
# initialStateDivision = 'q0'
# finalStateDivision = {'q9'}
# transitionFuncDivision = {
#     ('q0', '1'): ('q1', '_', 'R'),
#     ('q1', '1'): ('q1', '1', 'R'),
#     ('q1', '0'): ('q2', '0', 'R'),
#     ('q2', 'X'): ('q2', 'X', 'R'),
#     ('q2', '1'): ('q3', 'X', 'L'),
#     ('q3', '0'): ('q3', '0', 'L'),
#     ('q3', '1'): ('q3', '1', 'L'),
#     ('q3', 'X'): ('q3', 'X', 'L'),
#     ('q3', '_'): ('q0', '1', 'R'),
#     ('q0', '0'): ('q4', '0', 'R'),
#     ('q4', '1'): ('q4', '1', 'R'),
#     ('q4', 'X'): ('q4', 'X', 'R'),
#     ('q4', '0'): ('q5', '0', 'R'),
#     ('q5', '1'): ('q5', '1', 'R'),
#     ('q5', '_'): ('q6', '1', 'L'),
#     ('q6', '1'): ('q6', '1', 'L'),
#     ('q6', '0'): ('q6', '0', 'L'),
#     ('q6', 'X'): ('q6', 'X', 'L'),
#     ('q6', '_'): ('q0', '_', 'R'),
#     ('q2', '0'): ('q7', '_', 'L'),
#     ('q7', '1'): ('q7', '_', 'L'),
#     ('q7', '0'): ('q7', '_', 'L'),
#     ('q7', 'X'): ('q7', '_', 'L'),
#     ('q7', '_'): ('q8', '_', 'R'),
#     ('q8', '_'): ('q8', '_', 'R'),
#     ('q8', '1'): ('q9', '1', 'R'),
# }

# turingDivision = TuringMachine(
#     inputDivision,
#     initialStateDivision,
#     finalStateDivision,
#     transitionFuncDivision
# )

# print("\ninitial tape division     : " + turingDivision.get_tape())

# while not turingDivision.final():
#     turingDivision.step()

# print("final tape division       : " + turingDivision.get_tape())

# FACTORIAL
inputFactorial = '111'
initialStateFactorial = 'q0'
finalStateFactorial = {'q24'}
transitionFuncFactorial = {
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '_'): ('q1', '0', 'S'),
    ('q1', '0'): ('q1', '0', 'L'),
    ('q1', '1'): ('q1', '1', 'L'),
    ('q1', '_'): ('q2', '_', 'R'),
    ('q2', '0'): ('q5', '0', 'R'),
    ('q2', '1'): ('q3', 'X', 'R'),
    ('q3', '0'): ('q3', '0', 'R'),
    ('q3', '1'): ('q3', '1', 'R'),
    ('q3', '_'): ('q4', '1', 'S'),
    ('q4', '0'): ('q4', '0', 'L'),
    ('q4', '1'): ('q4', '1', 'L'),
    ('q4', 'X'): ('q2', 'X', 'R'),
    ('q5', '1'): ('q5', '1', 'R'),
    ('q5', '_'): ('q7', '0', 'L'),
    ('q6', '0'): ('q6', '0', 'L'),
    ('q6', '1'): ('q6', '1', 'L'),
    ('q6', 'X'): ('q6', 'X', 'L'),
    ('q6', '_'): ('q16', '_', 'R'),
    ('q7', '0'): ('q7', '0', 'L'),
    ('q7', '1'): ('q7', '1', 'L'),
    ('q7', 'X'): ('q7', '1', 'L'),
    ('q7', '_'): ('q8', '_', 'R'),
    ('q8', '1'): ('q9', '_', 'R'),
    ('q9', '0'): ('q6', '0', 'L'),
    ('q9', '1'): ('q10', 'X', 'R'),
    ('q10', '0'): ('q11', '0', 'R'),
    ('q10', '1'): ('q10', '1', 'R'),
    ('q11', '0'): ('q14', '0', 'L'),
    ('q11', '1'): ('q12', 'X', 'R'),
    ('q12', '0'): ('q12', '0', 'R'),
    ('q12', '1'): ('q12', '1', 'R'),
    ('q12', '_'): ('q13', '1', 'S'),
    ('q13', '0'): ('q13', '0', 'L'),
    ('q13', '1'): ('q13', '1', 'L'),
    ('q13', 'X'): ('q11', 'X', 'R'),
    ('q14', '0'): ('q15', '0', 'L'),
    ('q14', 'X'): ('q14', '1', 'L'),
    ('q15', '0'): ('q15', '1', 'L'),
    ('q15', '1'): ('q15', '1', 'L'),
    ('q15', 'X'): ('q9', 'X', 'R'),
    ('q16', '0'): ('q25', '_', 'R'),
    ('q16', 'X'): ('q17', '_', 'R'),
    ('q17', '0'): ('q18', '_', 'R'),
    ('q17', '1'): ('q18', '_', 'R'),
    ('q17', 'X'): ('q19', 'X', 'R'),
    ('q18', '0'): ('q24', '_', 'S'),
    ('q18', '1'): ('q18', '_', 'R'),
    ('q18', 'X'): ('q22', 'X', 'R'),
    ('q19', '0'): ('q20', '0', 'R'),
    ('q19', '1'): ('q19', '1', 'R'),
    ('q19', 'X'): ('q19', 'X', 'R'),
    ('q20', '0'): ('q21', '0', 'L'),
    ('q20', '1'): ('q20', '1', 'R'),
    ('q20', 'X'): ('q20', 'X', 'R'),
    ('q21', '0'): ('q6', 'X', 'L'),
    ('q21', '1'): ('q6', 'X', 'L'),
    ('q21', 'X'): ('q21', 'X', 'L'),
    ('q22', '0'): ('q22', '0', 'R'),
    ('q22', '1'): ('q22', '1', 'R'),
    ('q22', 'X'): ('q22', 'X', 'R'),
    ('q22', '_'): ('q23', '0', 'L'),
    ('q23', '0'): ('q23', '0', 'L'),
    ('q23', '1'): ('q23', '1', 'L'),
    ('q23', 'X'): ('q23', '1', 'R'),
    ('q23', '_'): ('q9', '_', 'R'),
    ('q25', '0'): ('q25', '_', 'R'),
    ('q25', '1'): ('q25', '1', 'R'),
    ('q25', '_'): ('q24', '_', 'S'),
}

turingFactorial = TuringMachine(
    inputFactorial,
    initialStateFactorial,
    finalStateFactorial,
    transitionFuncFactorial
)

print("\ninitial tape factorial     : " + turingFactorial.get_tape())

speed = 0.5

if keyboard.KEY_UP:
    speed += 0.05

if keyboard.KEY_DOWN:
    speed -= 0.05
i=0
while not turingFactorial.final():
        # i=1
        # print("Step {0} : {1}" .format(i, turingFactorial.step()))
        # sleep(speed)
        # i+=1
    i +=1 
    print(f"Step {i} : {turingFactorial.step()}")
    sleep(speed)
        
    
print("final tape factorial      : " + turingFactorial.get_tape())
