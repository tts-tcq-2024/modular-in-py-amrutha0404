from telecom_color_coder import TelecomColorCode

def calculate_major_index(pair_number):
    return (pair_number - 1) // len(TelecomColorCode.MINOR_COLORS)

def calculate_minor_index(pair_number):
    return (pair_number - 1) % len(TelecomColorCode.MINOR_COLORS)

def validate_major_index(major_index):
    if major_index >= len(TelecomColorCode.MAJOR_COLORS):
        raise IndexError('Major index out of range')

def validate_minor_index(minor_index):
    if minor_index >= len(TelecomColorCode.MINOR_COLORS):
        raise IndexError('Minor index out of range')

def get_color_from_pair_number(pair_number):
    """
    Returns the TelecomColorCode based on the given pair number.

    Args:
        pair_number (int): The pair number for which the color code needs to be determined.

    Returns:
        TelecomColorCode: The color code corresponding to the given pair number.

    Raises:
        ValueError: If the major or minor index is invalid.

    """
    major_index = calculate_major_index(pair_number)
    validate_major_index(major_index)
    minor_index = calculate_minor_index(pair_number)
    validate_minor_index(minor_index)
    return TelecomColorCode(major_index, minor_index)
