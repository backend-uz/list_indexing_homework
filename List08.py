def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = list1
    i = 0
    while i < len(a):
        if a[i] == 1:
            a[i] = True
        else:
            a[i] = False
        i +=1
    return a