from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5


class StateMachine:
    state = State.A

    def shift(self):
        return self.update({
            State.A: [State.B, 0],
            State.D: [State.E, 6],
            State.E: [State.F, 7],
            State.F: [State.B, 8],
        })

    def file(self):
        return self.update({
            State.A: [State.C, 1],
            State.B: [State.B, 4],
            State.C: [State.D, 5],
        })

    def fetch(self):
        return self.update({
            State.A: [State.E, 2],
            State.B: [State.C, 3],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()
