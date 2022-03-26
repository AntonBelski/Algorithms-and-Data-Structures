from collections import deque


class ShuntingYardAlgorithm:
    # also known as Reverse Polish notation (RPN)
    def tokenize(self, s):
        number_str = []
        for c in s:
            if c.isdigit():
                number_str.append(c)
            elif c != ' ':
                if number_str:
                    yield ''.join(number_str)
                    number_str = []
                yield c

        if number_str:
            yield ''.join(number_str)

    def rpn(self, s):
        stack = []
        priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        postfix = deque()
        last = '('

        for t in self.tokenize(s):
            if t.isdigit():
                postfix.append(t)
            elif t in '+-/*':
                if t == '-' and last == '(':
                    postfix.append('0')
                while stack and priority[stack[-1]] >= priority[t]:
                    postfix.append(stack.pop())
                stack.append(t)
            elif t == '(':
                stack.append(t)
            else:
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            last = t

        while stack:
            postfix.append(stack.pop())

        return postfix

    def calculate(self, s):
        tokens = self.rpn(s)
        result = []

        for t in tokens:
            if not t.isdigit():
                if t == '-':
                    result[-2] -= result[-1]
                elif t == '+':
                    result[-2] += result[-1]
                elif t == '*':
                    result[-2] *= result[-1]
                else:
                    result[-2] = int(result[-2] / result[-1])
                result.pop()
            else:
                result.append(int(t))

        return sum(result)


if __name__ == '__main__':
    shunting_yard_algorithm = ShuntingYardAlgorithm()
    s = "1+1"
    print(shunting_yard_algorithm.calculate(s))
    s = "-6 -4/ 2"
    print(shunting_yard_algorithm.calculate(s))
    s = "2*(5 +5*2) /3+(6/2+8 )"
    print(shunting_yard_algorithm.calculate(s))
