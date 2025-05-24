def check_email(email: str):
    li = email.split("@")
    if len(li) <= 1:
        return False
    else:
        if "." in li[-1]:
            return True
        else:
            return False