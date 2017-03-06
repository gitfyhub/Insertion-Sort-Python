def sort(list):
    # type: (object) -> object
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
            list[i + 1] = list[i]
            list[i] = value
            i = i - 1


def caller():
    a = [-1, 13333, 2, 3, 42, 2676547135678567879896896, 45454, -9,2342342424234234]
    sort(a)
    print(a)


# - - python console call - - -
# from insertion_sort import *
# caller()
