def simpleAdd(n1, n2):
    answer = n1 + n2
    return(answer)

def simpleDiv(numerator, divisor):
    try:
        answer = numerator/float(divisor)
        print(answer)
        return(answer)
    except ZeroDivisionError:
        print("Cannot enter 0 as divisor")
        return(None)
    except TypeError:
        print("Only numerical values are accepted")
        return(None)

def sumDigits(s):
    try:
        answer = len(s)
        return(answer)
    except TypeError:
        print("requires string")
        return(None)

def findAnEven(l):
    for i in range(len(l)):
        try:
            if int(l[i]) % 2 == 0:
                return(l[i])
        except ValueError:
            print("No even number found in list")
            return(None)
        except TypeError:
            print("Input requires list of integers")
            return(None)