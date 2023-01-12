# Resolução do problema https://leetcode.com/problems/defanging-an-ip-address/
# Dificuldade: Fácil


def defangIPaddr(address: str) -> str:
    return address.replace(".", "[.]")


print(defangIPaddr(address = "1.1.1.1"))
print(defangIPaddr(address = "255.100.50.0"))