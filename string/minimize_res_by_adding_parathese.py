'''
You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.

Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.

Eg.
Input: expression = "247+38"
Output: "2(47+38)"
Explanation: The expression evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the '+'.
It can be shown that 170 is the smallest possible value.
'''
# 思路：找到哪里可以divide（加括号），evaluate
class Solution:

    def minimizeResult(self, expression: str) -> str:

        a, b = expression.split('+')
        res = (int(a) * int(b), f'({expression})')

        for i in range(len(a)):
            # i is where we divide a. op1: [0, i-1], op2(a): [i:] 24(7
            op1 = int(a[:i]) if i > 0 else 1
            a1 = int(a[i:])

            # j is where we divde b. op2(b): [:j], op3: [j+1:]
            for j in reversed(range(len(b))):
                op3 = int(b[j + 1:]) if j != len(b) - 1 else 1
                b1 = int(b[:j + 1])
                op2 = a1 + b1
                # print(f"op1: {op1} | a1: {a1} b1: {b1} | op3: {op3}")
                t = op1 * op2 * op3
                if t < res[0]:
                    res = (t, f'{op1 if i != 0 else ""}({a1}+{b1}){op3 if j != len(b) - 1 else ""}')
        return res[1]

