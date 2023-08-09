def is_valid(num: str) -> bool:
    for element in num:
        if not element.isdigit():
            return False
    if 1 <= int(num) <= 100:
        return True
    else:
        return False