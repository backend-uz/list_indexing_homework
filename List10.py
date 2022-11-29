def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    i = []
    if list_num[0] < list_num[-1]:
        i = list_num[-1]
    else:
        i = list_num[0]

    return i
l = [1,2,3]
print(main(l))