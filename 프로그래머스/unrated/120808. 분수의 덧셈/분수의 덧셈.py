def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)


def solution(numer1, denom1, numer2, denom2):
    denom = denom1*denom2
    numer = numer1*denom2 + numer2*denom1
    if gcd(numer, denom) == 1:
        answer = [numer, denom] 
    else:
        gcd1 = gcd(numer, denom)
        answer = [numer/gcd1, denom/gcd1]
    return answer