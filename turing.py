class Tape(object):
    blankTape = '_'

    def __init__(self, initString=''):
        self._tape = dict(enumerate(initString))

    def __str__(self):
        string = ''
        for i in range(
                min(self._tape.keys()),
                max(self._tape.keys()) + 1
        ):
            string += self._tape[i]
        return string

    def __setitem__(self, index, value):
        self._tape[index] = value

    def __getitem__(self, index):
        return self._tape[index] if index in self._tape else Tape.blankTape


class TuringMachine(object):
    def __init__(
        self,
        inputTape='',
        initState='',
        finalState=None,
        transFunc=None
    ):
        self._tape = Tape(inputTape)
        self._head = 0
        self._b = Tape.blankTape
        self._qc = initState
        self._tf = {} if transFunc == None else transFunc
        self._qf = set() if finalState == None else finalState

    def getTape(self):
        return str(self._tape)

    def nextMove(self):
        underHead = self._tape[self._head]
        x = (self._qc, underHead)

        if x in self._tf:
            y = self._tf[x]
            self._tape[self._head] = y[1]

            if y[2] == 'R':
                self._head += 1
            elif y[2] == 'L':
                self._head -= 1

            self._qc = y[0]
            print(self._tape)

    def isFinal(self):
        return True if self._qc in self._qf else False
