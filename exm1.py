def arithmetic(num_1, num_2, operation):
    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "/":
        result = num_1 / num_2
    elif operation == "*":
        result = num_1 * num_2
    else:
        result = "Неверная операция"
    return result

result = int()
num_1, num_2, operator = int(input()), int(input()), input()


result = arithmetic(num_1, num_2, operator)

print(result)