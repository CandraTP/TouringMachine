class Tape(object):
    blank = '_'

    def __init__(self, tape_string=''):
        self._tape = dict(enumerate(tape_string))

    def __str__(self):
        s = ""
        min_i = min(self._tape.keys())
        max_i = max(self._tape.keys())

        for i in range(min_i, max_i+1):
            s += self._tape[i]
        return s

    def __getitem__(self, index):
        if index in self._tape:
            return self._tape[index]
        else:
            return Tape.blank

    def __setitem__(self, index, value):
        self._tape[index] = value


class TuringMachine(object):
    def __init__(
        self,
        inputTape='',
        initialState='',
        finalState=None,
        transitionFunc=None
    ):
        self._tape = Tape(inputTape)
        self._headPosition = 0
        self._blank = Tape.blank
        self._currentState = initialState

        if transitionFunc == None:
            self._transitionFunc = {}
        else:
            self._transitionFunc = transitionFunc

        if finalState == None:
            self._finalState = set()
        else:
            self._finalState = finalState

    def get_tape(self):
        return str(self._tape)

    def step(self):
        underHead = self._tape[self._headPosition]
        x = (self._currentState, underHead)

        if x in self._transitionFunc:
            y = self._transitionFunc[x]
            self._tape[self._headPosition] = y[1]

            if y[2] == 'R':
                self._headPosition += 1
            elif y[2] == 'L':
                self._headPosition -= 1
            self._currentState = y[0]

            return(self._tape)

    def final(self):
        if self._currentState in self._finalState:
            return True
        else:
            return False
