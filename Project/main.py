from SymbolTable import SymbolTable

st = SymbolTable()

st.add("a")
st.add("b")
st.add("c")
st.add("d")
st.add("e")
st.add("f")

print(st.get("a"))
print(st.get("1"))
print(st.get("b"))
print(st.get("c"))