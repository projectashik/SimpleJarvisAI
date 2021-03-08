import operator


def get_operator(op):
    return {
        '+': operator.add,
        'plus': operator.add,
        '-': operator.sub,
        'minus': operator.sub,
        'x': operator.mul,
        'multiply': operator.mul,
        'into': operator.mul,
        'times': operator.mul,
        'divided': operator.__truediv__,
        'slash': operator.__truediv__,
        '/': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,
        '^': operator.xor,
        'xor': operator.xor
    }[op]


def eval_binary_expression(op1, oper, op2):
    op1, op2 = float(op1), float(op2)
    return get_operator(oper)(op1, op2)


def calculate(query):
    queries = query.split()
    try:
        result = eval_binary_expression(*queries)
        return query + " = " + str(result)
    except:
        return "Unable to calculate"
