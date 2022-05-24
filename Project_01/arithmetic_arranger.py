# Project_01
# Aritmetic arranger

def arithmetic_arranger(equations, boolean=False):

    # No. of problems cannot exceed five
    if len(equations) > 5:
        return "Error: Too many problems."

    upper_half_list = []
    lower_half_list = []
    line_list = []
    result_list = []

    for equation in equations:
        content = equation.split()
        operator = content[1]

        # Each number in a problem cannot be more than four digits
        if len(content[0]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if len(content[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

# Numbers must be numbers!!!!
        try:
            number_1 = int(content[0])
            number_2 = int(content[2])

        except:
            return "Error: Numbers must only contain digits."

# Only addition and subtraction must be covered
        if operator != "+" and operator != "-":
            return "Error: Operator must be \'+\' or \'-\'."

# If boolean is True shows result
        if boolean == True:
            if operator == "+":
                result = str(number_1 + number_2)

            elif operator == "-":
                result = str(number_1 - number_2)
              
        elif boolean == False:
            result = ""

# When the upper number is of less length
        if len(str(number_1)) < len(str(number_2)):
            lower_half = operator + ' ' + str(number_2)
            upper_half = (len(lower_half) - len(str(number_1))) * ' ' + str(number_1)
            line = len(lower_half) * '-'
          
# When the lower number is of less length
        else:
            upper_half = '  ' + str(number_1)
            lower_half = operator + (len(upper_half) - len(str(number_2)) - 1) * ' ' + str(number_2)
            line = len(lower_half) * '-'

        result = (len(line) - len(result)) * ' ' + result

        upper_half_list.append(upper_half)
        lower_half_list.append(lower_half)
        line_list.append(line)
        result_list.append(result)

    distance = "    "

    top = distance.join(upper_half_list)
    top_middle = distance.join(lower_half_list)
    bottom_middle = distance.join(line_list)
    bottom = distance.join(result_list)

    if boolean == True:
      arranged_problems = top + '\n' + top_middle + '\n' + bottom_middle + '\n' + bottom
    else:
      arranged_problems = top + '\n' + top_middle + '\n' + bottom_middle

    return arranged_problems