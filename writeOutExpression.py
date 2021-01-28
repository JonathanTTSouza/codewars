def expression_out(exp):
    numbers = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven',
                      '8':'Eight','9':'Nine', '10':'Ten', ' ':' '}
    words = exp.split(' ')
    try:
        output = numbers.get(words[0]) + ' ' + OPERATORS.get(words[1]) + numbers.get(words[2])
        return output
    except:
        return "That's not an operator!"
