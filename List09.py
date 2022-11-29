def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 0
    l = list1
    while i < len(l):
        if l[i] == l[i+1]:
            b = True
        else:
            b = False
    return b