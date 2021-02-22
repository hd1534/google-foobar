def solution(xs):
    # Your code here
    if len(xs) == 1:
        return str(xs[0])

    pos = [x for x in xs if x > 0]
    neg = [x for x in xs if x < 0]

    pos_cnt = len(pos)
    neg_cnt = len(neg)

    if (neg_cnt == 1 and pos_cnt == 0) or (neg_cnt == 0 and pos_cnt == 0):
        return '0'

    if neg_cnt % 2:
        neg.remove(max(neg))

    result = 1
    for n in pos:
        result *= n

    for n in neg:
        result *= n

    return str(result)


