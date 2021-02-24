# 홀짝일때 규칙 나눠서 정리한건데 친구 도움을 좀 받음 ㅠㅠ

def solution(start, length):
    # Your code here
    
    a = b = start
    result = 0
    
    for i in range(length):
        a = b + i
        b = a + length - i - 1
        if a == b:
            result ^= a
        else:
            result ^= [
                [b, 1, b ^ 1, 0],
                [a, a ^ b, a-1, (a-1) ^ b]
            ][a % 2][(b-a) % 4]

    return result