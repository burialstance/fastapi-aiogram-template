def declination(age: int) -> str:
    """сколько лет?"""
    if (age % 10 == 1) and (age != 11) and (age != 111):
        return 'год'
    elif (age % 10 > 1) and (age % 10 < 5) and (age not in [12, 13, 14]):
        return 'года'
    else:
        return 'лет'


if __name__ == '__main__':
    for i in range(80):
        print(i, declination(i))
