def solution(genres, plays):
    answer = []

    genres_plays = dict()
    for i in range(0, len(plays)):
        if genres[i] not in genres_plays:
            genres_plays[genres[i]] = 0

        genres_plays[genres[i]] += plays[i]

    zipped = list(zip(range(len(plays)), zip(genres, plays)))
    zipped.sort(key=lambda x: (genres_plays[x[1][0]], x[1][1], -x[0]), reverse=True)

    last_genre = ""
    cnt = 0
    for z in zipped:
        if last_genre == z[1][0]:
            cnt += 1
        else:
            cnt = 1
            last_genre = z[1][0]

        if cnt <= 2:
            answer.append(z[0])

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)
