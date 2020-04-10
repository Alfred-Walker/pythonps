def solution(record):
    answer = []
    uid_name = {}
    in_and_out = []

    for r in record:
        text = r.split()
        command = text[0]
        uid = text[1]
        if len(text) == 3:
            name = text[2]
            uid_name[uid] = name

        if command == "Enter":
            in_and_out.append((1, uid))
        elif command == "Leave":
            in_and_out.append((0, uid))

    for io in in_and_out:
        if io[0] == 1:
            answer.append('"' + uid_name[io[1]] + '님이 들어왔습니다."')
        elif io[0] == 0:
            answer.append(uid_name[io[1]] + '"님이 나갔습니다."')

    return answer


test_record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(test_record))
