def corresponding_parenthesis(text):
    left_side = []
    right_side = []
    output = ''
    for item in text:
        if item == ')':
            right_side.append(')')
        else:
            left_side.append('(')
    if len(left_side) > len(right_side):
        for each in range(len(left_side) - len(right_side)):
            output += left_side[each]
    if len(right_side) > len(left_side):
        for each in range(len(right_side) - len(left_side)):
            output += right_side[each]
    return output

print(corresponding_parenthesis("()((()"))


def remove_more_than_two_repetitions(text):
    output = ''
    for index, item in enumerate(text):
        try:
            if item == text[index + 1] == text[index + 2]:
                continue
            else:
                output += item
        except:
            output += item
    return output


text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"

text = remove_more_than_two_repetitions(text)
print(text)
