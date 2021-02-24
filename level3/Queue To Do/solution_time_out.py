# time out ?

def solution(start, length):
    # Your code here
    result = 0

    for i in range(length, 0, -1):
        for j in range(i):
            result ^= start + j + ( length - i ) * length
            print(start + j + ( length - i ) * length, end=" ")
        print()

    return result
