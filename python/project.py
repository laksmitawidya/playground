def get_arithmetic_result(a, b, operator):
    if operator == "+":
        return int(a) + int(b)
    if operator == "-":
        return int(a)-int(b)



def arithmetic_arranger(problems):
    if len(problems) > 5:
        print("Error: Too many problems")
        return

    for problem in problems:
        arithmetic = problem.split()
        a = arithmetic[0]
    
        operator = arithmetic[1]
        b = arithmetic[2]
        if(operator != "+" and operator != "-"):
            print("Error: Operator must be '+' or '-'.")
            return

        result = get_arithmetic_result(a, b, operator)
        total_spaces = len(str(max(int(a),int(b)))) + 2

    

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 - 49"])