from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def matched(ch1, ch2):
        matched_dictionary = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        return matched_dictionary[ch1] == ch2


def balanced(str):
    stack = Stack()
    for char in str:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char == ']':
            if stack.size()==0:
                 return False
            if not matched(char,stack.pop()):
                 return False

    return stack.size()==0

if __name__ == '__main__':
    print(balanced("({a+b})"))
    print(balanced("((a+b))"))
    print(balanced("((a+g))"))
    print(balanced("))"))
    print(balanced("[a+b]*(x+2y)*{gg+kk}"))