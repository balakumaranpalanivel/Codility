# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    
    path_list = list()
    for i in range(1,X+1):
       path_list.append(i)

    for i in range(0, len(A)):
        try:
            path_list.remove(A[i])
            if(len(path_list) == 0):
                return i
        except ValueError:
            pass

    return -1