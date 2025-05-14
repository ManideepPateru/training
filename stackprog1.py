def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            
            stack.append(result)
    
    return stack[0]

def main():
    expression = input("expression")
    result = evaluate_postfix(expression)
    
    print("Result:", int(result))

if __name__ == "__main__":
    main()