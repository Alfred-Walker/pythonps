# 파이썬 url 사용
# https://velog.io/@city7310/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-URL-%EA%B0%80%EC%A7%80%EA%B3%A0-%EB%86%80%EA%B8%B0
from urllib.parse import ParseResult, urlparse, urlunparse


parsed = urlparse("https://google.com/pathA/pathB")
print(parsed)
print(parsed.scheme)
print(parsed.netloc)
print(parsed.path)
unparsed = urlunparse(parsed)
print(unparsed)




import re

# 파이썬 re regex 사용
def get_valid_url_regex(address_list):
    valid_address = []
    pattern_both = r"((https://|http://).*|)"
    pattern_http = r"(http://.*|)"
    pattern_https = r"(https://.*|)"

    address_regex = re.compile(pattern_https, re.IGNORECASE)      # 필요에 따라 제거

    for addr in address_list:
        match_object = address_regex.fullmatch(addr)

        if match_object:
            valid_address.append(re.split(r'https://|http://', match_object.group()))

    return valid_address


print(get_valid_url_regex(["http://naver.com", "https://naver.com", "https://naver.com/"]))
