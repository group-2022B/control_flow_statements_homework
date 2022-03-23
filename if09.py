def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    if a < 10:
        return True
    else:
        a = str(a)
        a = a[1] + a[0]
        a = int(a)
        return main(a)
        