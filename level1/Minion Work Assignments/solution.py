def solution(data, n): 
    # Your code here

    for i in set(data):
        
        if data.count(i) > n:
            while i in data: data.remove(i)

    return data

