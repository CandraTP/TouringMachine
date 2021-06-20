from time import sleep
from turing import TuringMachine

def convert(input):
  num =''
  for x in range(input):
    num += '1'

  return num

speed = 0.01

def switch():
    pilihan = input("1. Addition 2. Substraction 3. Multiplication 4. Division 5. Factorial 6. Binary Log \n")
    if pilihan == '1':

        a = int(input('Input A:'))
        b = int(input('Input B:'))

        x = convert(a)
        y = convert(b)

        inputAddition = x+'+'+y

        initialStateAddition = 'q0'
        finalStateAddition = {'q3'}
        transitionFuncAddition = {
            ('q0', '0'): ('q0', '_', 'R'),
            ('q0', '1'): ('q0', '1', 'R'),
            ('q0', '+'): ('q1', '1', 'R'),
            ('q1', '0'): ('q2', '0', 'L'),
            ('q1', '1'): ('q1', '1', 'R'),
            ('q1', '_'): ('q2', '_', 'L'),
            ('q2', '0'): ('q2', '_', 'R'),
            ('q2', '1'): ('q2', '_', 'R'),
            ('q2', '_'): ('q3', '_', 'S'),
        }

        turingAddition = TuringMachine(
            inputAddition,
            initialStateAddition,
            finalStateAddition,
            transitionFuncAddition
        )

        print("\ninitial tape addition     : "
            + turingAddition.getTape())

        i = 0
        while not turingAddition.isFinal():
            i += 1
            print('Step', i, ': ', end="")
            turingAddition.nextMove()
            sleep(speed)

        print("final tape addition       : "
            + turingAddition.getTape())

    elif pilihan == '2':
        inputSubtraction = '11-111'
        initialStateSubtraction = 'q0'
        finalStateSubtraction = {'q5'}
        transitionFuncSubtraction = {
            ('q0', '1'): ('q1', '_', 'R'),
            ('q0', '-'): ('q4', '_', 'R'),
            ('q1', '1'): ('q1', '1', 'R'),
            ('q1', '-'): ('q2', '-', 'R'),
            ('q2', '1'): ('q3', '-', 'L'),
            ('q2', '-'): ('q2', '-', 'R'),
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

        print("\ninitial tape subtraction  : "
            + turingSubtraction.getTape())

        i = 0
        while not turingSubtraction.isFinal():
            i += 1
            print('Step', i, ': ', end="")
            turingSubtraction.nextMove()
            sleep(speed)

        print("final tape subtraction    : "
            + turingSubtraction.getTape())
    
    elif pilihan == '3':
        print("kol")
    elif pilihan == '4':
        print("kol")
    elif pilihan == '5':
        print("kol")
    elif pilihan == '6':
        print("kol")
    else:
        print("Pilihan anda SALAH !!")

switch()