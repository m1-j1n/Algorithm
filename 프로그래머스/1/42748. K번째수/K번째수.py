def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        tmp = []
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer