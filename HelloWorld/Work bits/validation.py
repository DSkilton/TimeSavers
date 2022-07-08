agreed = ["yes", "y", "ok"]


def did_user_agree(str_input):
    if str_input.lower() in agreed:
        return True
