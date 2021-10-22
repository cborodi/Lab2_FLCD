from SymbolTable import SymbolTable
from PIF import ProgramInternalForm
from Scanner import generateTokens

if __name__ == '__main__':
    fileName = input("Scan file> ")

    file = open(fileName, 'r')
    for line in file:
        print(line)

    with open(fileName, 'r') as file:
        for line in file:
            generateTokens(line)


"""
from SymbolTable import SymbolTable

st = SymbolTable()

st.add("a")
st.add("ab")
st.add("ba")
st.add("b")
st.add("c")
st.add("d")
st.add("e")
st.add("f")

print(st.get("a"))
print(st.get("1"))
print(st.get("b"))
print(st.get("c"))
print(st.get("ab"))
print(st.get("ba"))
"""
