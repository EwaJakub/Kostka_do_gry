from random import randint


def dice_type_check(code):
    """
    Gives information about dice type in code with a number of its sides as a range for throw value.
    :param code: str code to be checked
    :return: int if the value is correct, str if the value is incorrect
    """
    dice_types = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    chosen_dice_type = ''
    for dice_type in dice_types:
        if dice_type in code:
            chosen_dice_type = int(dice_type[1::])
    return chosen_dice_type


def dice_threws(code):
    """
    Checkes the number os throws on base of code information
    :param code: str code to be checked
    :return: int or str in case of incorrect data
    """
    code_letters = []
    for element in code:
        if not element.isdigit() and element != '+' and element != '-':
            code_letters.append(element)
    try:
        if len(code_letters) == 1:
            i = code.index('D')
            if i != 0:
                number_of_throws = int(code[:i])
            elif code[0] == 'D':
                number_of_throws = 1
            return number_of_throws
        else:
            return 'Incorrect data'
    except ValueError:
        return 'Incorrect data'


def dice_value_modifier(code):
    """
    Checkes if code have modifier value
    :param code: str code to be checked
    :return: int or str in case of incorrect data
    """
    try:
        if '-' in code:
            i = code.index('-')
            modifier = int(code[i::])
        elif '+' in code:
            i = code.index('+')
            modifier = int(code[i::])
        else:
            modifier = 0
        return modifier
    except ValueError:
        return 'Incorrect data'


def dice_code(code):
    """
    Checkes if all options of code values are correct. If one of the values is not int, returns error information.
    If all values are correct gives a simulation of dice throws and returns a value.
    :param code:
    :return: int or str in case of incorrect data
    """
    chosen_dice_type = dice_type_check(code)
    number_of_throws = dice_threws(code)
    modifier = dice_value_modifier(code)
    if isinstance(chosen_dice_type, str) or isinstance(number_of_throws, str) or isinstance(modifier, str):
        return 'Incorrect code value!'
    return sum([randint(0, chosen_dice_type) for _ in range(0, number_of_throws)]) + modifier


if __name__ == '__main__':
    print(dice_code("2D10+10"))
    print(dice_code("D6"))
    print(dice_code("2D3"))
    print(dice_code("12D12-1"))
    print(dice_code("DD34"))    
    print(dice_code("4-3D6"))