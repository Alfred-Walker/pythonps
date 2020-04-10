import re

# 파이썬 re regex 사용
def get_valid_mail(email_list):
    valid_mail = []
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    email_regex = re.compile(pattern, re.IGNORECASE)

    for email in email_list:
        match_object = email_regex.fullmatch(email)

        if match_object:
            valid_mail.append(re.split(r'@', match_object.group(0)))

    return valid_mail


print(get_valid_mail(["aaa@daum.net", "23479823498.com", "abch@hanmail.com"]))



# address = "studio.alfred.walker@gmail.com"
# email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# search: 문자열의 어느 위치에서나 패턴 매치
# match: 문자열의 시작 점에서 패턴 매치
# fullmatch : 문자열의 시작과 끝까지 일치 (권장)
# (위 regex는 ^와 $을 사용하여 모두 동일하게 동작?)
# if re.search(email_regex, address):
#     print("<{0}> is valid address. ( SEARCH )".format(address))

# if re.match(email_regex, address):
#     print("<{0}> is valid address. ( MATCH )".format(address))

# if re.fullmatch(email_regex, address):
#     print("<{0}> is valid address. ( FULL MATCH )".format(address))


address = "studio.alfred.walker@GMAIL.COM"
lower_upper_gmail_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@(gmail.com|GMAIL.COM)$)")

# if re.search(lower_upper_gmail_regex, address):
#     print("<{0}> is valid address. ( SEARCH )".format(address))

# if re.match(lower_upper_gmail_regex, address):
#     print("<{0}> is valid address. ( MATCH )".format(address))

# if re.fullmatch(lower_upper_gmail_regex, address):
#     print("<{0}> is valid address. ( FULL MATCH )".format(address))


# 파이썬 split 사용 (@ 만 split)
# address = "studio.alfred.walker@gmail.com"
# tmp_split = address.split('@')
# account = tmp_split[0]
# mail_server = tmp_split[1]




# 파이썬 email parser
from email.utils import parseaddr


# 일부 잘못된 주소를 valid 하게 처리하는 경우에 대한 예시
invalid_address = 'invalid@example,com'
invalid_address2 ='invalid-email'
result1 = parseaddr(invalid_address)
result2 = parseaddr(invalid_address2)
# print(result1)
# print(result2)
# >>> ('', 'invalid@example')
# ('', 'invalid-email'


# 일반적인 주소 획득
address = "studio.alfred.walker@gmail.com"
parseaddr(address)
# >>> ('', studio.alfred.walker@gmail.com)

address2 = "Alfred Walker <studio.alfred.walker@gmail.com>"
parseaddr(address)
# >>> ('Alfred Walker', 'studio.alfred.walker@gmail.com')

address2 = '"Alfred Walker <studio.alfred.walker@naver.com>" <studio.alfred.walker@gmail.com>'
parseaddr(address)

# >>> ('Alfred Walker <studio.alfred.walker@naver.com>', 'studio.alfred.walker@gmail.com')

invalid_address = "[invalid!email]"
parseaddr(invalid_address)
# >>> ('', '')