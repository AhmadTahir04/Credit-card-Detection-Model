def digits_of(n):
    """
    Convert a number into a list of its digits.
    
    :param n: int, number to be converted
    :return: list of int, digits of the number
    """
    return [int(d) for d in str(n)]

def luhn_algorithm(card_number):
    """
    Validate a credit card number using the Luhn algorithm.
    
    :param card_number: str, credit card number
    :return: bool, True if the card number is valid, False otherwise
    """
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

def validate_card_type(card_number):
    """
    Determine the type of credit card based on its number.
    
    :param card_number: str, credit card number
    :return: str, card type or 'Unknown card type'
    """
    if card_number.startswith('4') and len(card_number) in [13, 16, 19]:
        return 'Visa'
    elif card_number[:2] in ('51', '52', '53', '54', '55') and len(card_number) == 16:
        return 'MasterCard'
    elif card_number[:2] in ('34', '37') and len(card_number) == 15:
        return 'American Express'
    else:
        return 'Unknown card type'

def is_valid_card(card_number):
    """
    Check if a card number is valid and belongs to Visa, MasterCard, or American Express.
    
    :param card_number: str, credit card number
    :return: str, card type if valid, 'Invalid card number' otherwise
    """
    if not card_number.isdigit():
        return 'Invalid card number'

    if luhn_algorithm(card_number):
        return validate_card_type(card_number)
    else:
        return 'Invalid card number'

def main():
    card_number = input("Enter credit card number: ").strip()
    result = is_valid_card(card_number)
    print(result)

main()