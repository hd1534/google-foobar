def solution(l):
    # Your code here

    return sorted(l, key=lambda x: list(map(int, x.split('.'))))
    