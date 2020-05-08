from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.elements = []
        self.max_elements = []

    def empty(self) -> bool:
        return len(self.elements) == 0

    def max(self) -> int:
        if len(self.max_elements) == 0:
            return None
        return self.max_elements[-1]

    def pop(self) -> int:
        if len(self.elements) == 0:
            return None
        top = self.elements.pop()
        if top == self.max_elements[-1]:
            self.max_elements.pop()
        return top


    def push(self, x: int) -> None:
        self.elements.append(x)
        if len(self.max_elements) == 0 or x >= self.max_elements[-1]:
            self.max_elements.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
