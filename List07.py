def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = list1
    i = 0
    while i < len(a):
        if a[i] == 0:
            a[i] = False
        i +=1
    return a