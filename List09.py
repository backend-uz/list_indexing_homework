def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 1
    a = 0
    while i < len(list1):
        if list1[0] == list1[i]:
           a = True
        else:
            a = False
    i +=1
    return a
print(main([1,1,1,1]))