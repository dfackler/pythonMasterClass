def simpleAdd(n1, n2):
    answer = n1 + n2
    return(answer)

def simpleDiv(numerator, divisor):
    try:
        answer = numerator/float(divisor)
        print answer
        return(answer)
    except ZeroDivisionError:
        print "Cannot enter 0 as divisor"
        return(None)
    except TypeError:
        print "Only numerical values are accepted"
        return(None)

def sumDigits(s):
    try:
        answer = len(s)
        return(answer)
    except TypeError:
        print "requires string"
        return(None)