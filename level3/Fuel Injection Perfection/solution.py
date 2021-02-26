def solution(n):
    # Your code here

    result = 0
    n = int(n)
    print(bin(n))

    while n != 1:
        result += 1

        if n == 0b11:
            return result + 1

        if n & 1 == 1:
            if n & 0b11 == 0b11:
                n += 1
            else:
                n -= 1
        else:
            n >>= 1

        print(" -> ", bin(n))
        
    return result


if __name__ == "__main__":
    print(solution(str(0b11)))