from pandas import value_counts


def generate_power(base):
    def to_the_power_of(exponent):
        return base ** exponent

    return to_the_power_of


base2 = generate_power(2)
base2(2)  # 4
base2(4)  # 16
base3 = generate_power(3)
base3(2)  # 9
base2(3)  # 8


def mean():
    sample = []

    def inner_mean(number):
        sample.append(number)
        return sum(sample) / float(len(sample))

    return inner_mean


height = mean()
height(100)
height(105)
height(98)


def even_meaner():
    sample = []
    current = []

    def inner_mean(number):
        nonlocal current  # to know the value can be used in the enclsoing scope
        sample.append(number)
        current = sum(sample) / float(len(sample))
        return current

    # getter
    def value():
        nonlocal current
        return current

    # setter only to 0
    def reset():
        nonlocal sample, current
        current = 0
        sample = []

    inner_mean.value = value
    inner_mean.reset = reset


temps = even_meaner()
temps(25)
temps(28)
temps(33)
temps.value()
temps.reset()
temps.value()
