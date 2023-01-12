# Resolução do problema https://leetcode.com/problems/convert-the-temperature/description/
# Dificuldade: Fácil


def convertTemperature(celsius: float):
    return [f"{celsius + 273.15:.5f}", f"{celsius * 1.80 + 32.00:.5f}"]


print(convertTemperature(36.50))
print(convertTemperature(122.11))
