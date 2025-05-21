import string

def check_password(password: str) -> bool:
    if not (8 <= len(password) <= 20):
        return False

    has_letter = False
    has_digit = False
    has_punct = False

    for c in password:
        if c in string.ascii_letters:
            has_letter = True
        elif c in string.digits:
            has_digit = True
        elif c in string.punctuation:
            has_punct = True
        else:
            return False

    return has_letter and has_digit and has_punct