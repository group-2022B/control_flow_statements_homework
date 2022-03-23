def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    return "Freezing" if temp < 0 else "Very Cold" if temp < 10 else "Cold" if temp < 20 else "Normal" if temp < 30 else "Hot" if temp < 40 else "Very Hot"