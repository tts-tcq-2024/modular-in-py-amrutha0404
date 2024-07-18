from get_color_from_number import get_color_from_pair_number
from telecom_color_coder import TelecomColorCode

def generate_reference_manual():
    manual = "\n================== Color Coding Reference Manual =====================\n"
    total_pairs = len(TelecomColorCode.MAJOR_COLORS) * len(TelecomColorCode.MINOR_COLORS)
    for pair_number in range(1, total_pairs+1):
        # Get the color code for the current pair number
        color_code = get_color_from_pair_number(pair_number)
        
        # Append the pair number and color code to the manual string
        manual += f"{pair_number}: {color_code}\n"
    
    # Return the reference manual string
    return manual


def print_reference_manual():
    # Generate the reference manual
    manual = generate_reference_manual()
    # Print the reference manual
    print(manual)
