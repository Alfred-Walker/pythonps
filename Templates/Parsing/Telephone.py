import re

# 파이썬 re regex 사용
def get_valid_phone(number_list):
    valid_number = []
    pattern = r"(\d{3,4})-\d{3,5}-\d{4}"
    pattern = r"[0-9]{3,5}-[0-9]{3,5}-[0-9]{3,5}"
    phone_regex = re.compile(pattern, re.IGNORECASE)

    for num in number_list:
        match_object = phone_regex.fullmatch(num)

        if match_object:
            valid_number.append(re.split(r'-', match_object.group()))

    return valid_number


print(get_valid_phone(["010-3333-4444", "010-33533-4444", "010-34333-4444"]))
