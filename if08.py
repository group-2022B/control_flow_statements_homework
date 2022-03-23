def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    return "two-digit odd number" if a % 2 == 1 and len(str(a)) == 2 else \
        "two-digit even number" if a % 2 == 0 and len(str(a)) == 2 else \
        "three-digit odd number" if a % 2 == 1 and len(str(a)) == 3 else \
        "three-digit even number" if a % 2 == 0 and len(str(a)) == 3 else \
        "not a number"
