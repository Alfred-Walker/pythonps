import re


text = "테스트트트xm테스트"
target = "테스"
regex = re.compile(target)
result = regex.search(text)
print(result.group())

result = regex.findall(text)
print(result)


text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
result = matchobj.group()
print(result)

text = "시작테스트끝"
target = r"^시작.*"       # ['시작 테스트']

regex = re.compile(target)
result = regex.findall(text)
print(result)

text = "끝끝 시작테스트끝"
target = r".*끝$"       # ['시작 테스트']

regex = re.compile(target)
result = regex.findall(text)
print(result)

text = "010-12312-1111"
target = r"(\d{3})-(\d{3,5}-\d{4})"    # 가운데가 3개이상 4개 이하        d{3, 4} 로 입력하면 안됨
target = r"(\d{3})-([1-3]{3,5}-\d{4})"    # 가운데가 1이상 3 이하의 숫자이며, 3개이상 4개 이하        [('010', '12312-1111')]
target = r"(\d{3})-([1-3]{3,5})-(\d{4})"    # 괄호 처리가 되어 각 그룹이 tuple로 담김        [('010', '12312', '1111')]
target = r"(\d{3})-[1-3]{3,5}-\d{4}"    # 괄호(그룹) 처리가 앞부분만 되어 010만 추가됨       ['010']
target = r"\d{3}-[1-3]{3,5}-\d{4}"    # 전부 괄호(그룹) 처리가 안되어 전부 추가됨       ['010-12312-1111']
regex = re.compile(target)
result = regex.findall(text)
print(target)
print(result)


text = "문의사항이split1있으면split2032-232split33245 으로 연락주시기 바랍니다."
pattern = r'split[1-3]'
result = re.split(pattern, text)

print(result)       # ['문의사항이', '있으면', '032-232', '3245 으로 연락주시기 바랍니다.']



print('\n') # Prints a newline character
print(r'\n') # Escape sequence is not processed
print('\b') # Prints a backspace character
print(r'\b') # Escape sequence is not processed
