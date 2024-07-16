from telecom_color_coder import TelecomColorCode
from get_color_from_number import validate_major_index,validate_minor_index
def get_pair_number_from_color(major_color, minor_color):
    major_index = get_major_index(major_color)
    minor_index = get_minor_index(minor_color)
    return calculate_pair_number(major_index, minor_index)

def get_major_index(major_color):
    try:
        # Find the index of the major color in the TelecomColorCode.MAJOR_COLORS list
        major_index = TelecomColorCode.MAJOR_COLORS.index(major_color)
    except ValueError:
        raise ValueError('Major color not found')
    
    return major_index

def get_minor_index(minor_color):
    try:
        # Find the index of the minor color in the TelecomColorCode.MINOR_COLORS list
        minor_index = TelecomColorCode.MINOR_COLORS.index(minor_color)
    except ValueError:
        raise ValueError('Minor color not found')
    
    return minor_index

def calculate_pair_number(major_index, minor_index):
    validate_major_index(major_index)
    validate_minor_index(minor_index)
    # Calculate the pair number using the formula
    return major_index * len(TelecomColorCode.MINOR_COLORS) + minor_index + 1
