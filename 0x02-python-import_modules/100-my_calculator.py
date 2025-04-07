#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul

    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = ['+', '-', '*', '/']
    func = [add, sub, mul, div]
    op = sys.argv[2]
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    for i in range(len(operator)):
        if op == operator[i]:
            print("{} {} {} = {}".format(num1, op, num2, func[i](num1, num2)))
