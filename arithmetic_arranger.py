def arithmetic_arranger(problems, resolve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    up = ''
    down = ''
    dashs = ''
    results = ''

    for expression in problems:
        result = expression_arrange(expression)

        if type(result) == str:
            return 'Error: ' + result
        else:
            up = up + result[0] + "    "
            down = down + result[1] + "    "
            dashs = dashs + result[2] + "    "
            results = results + result[3] + "    "

    arranged = up.rstrip() + "\n" + down.rstrip() + "\n" + dashs.rstrip()
    if resolve:
        arranged = arranged + "\n" + results.rstrip()

    return arranged


def expression_arrange(expression):
    exp = expresion_parse(expression)

    if type(exp) == str:
        return exp

    opA = exp[0]
    opB = exp[1]
    opr = exp[2]
    pad = exp[3]
    res = exp[4]

    up = str(opA).rjust(pad + 2, ' ')
    down = '{} '.format(opr) + str(opB).rjust(pad, ' ')
    dashs = ''.rjust(pad + 2, '-')
    result = str(res).rjust(pad + 2, ' ')

    return (up, down, dashs, result)


def expresion_parse(expression):
    elements = expression.split()

    if len(elements[0]) > 4 or len(elements[2]) > 4:
        return 'Numbers cannot be more than four digits.'

    try:
        opA = int(elements[0])
        opB = int(elements[2])
    except:
        return 'Numbers must only contain digits.'

    pad = get_padding(elements[0], elements[2])
    opr = elements[1]

    if opr == '+':
        result = opA + opB
    elif opr == '-':
        result = opA - opB
    else:
        return "Operator must be '+' or '-'."

    return (opA, opB, opr, pad, result)


def get_padding(opA, opB):
    pad = len(opA)
    padb = len(opB)
    if padb > pad:
        pad = padb
    return pad
