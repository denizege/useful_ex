# 10. Занятая память

# Пример позволяет получить объём памяти, используемой любой переменной в Python.


import sys
var1="Python"
var2=100
var3=True
print(sys.getsizeof(var1)) #55
print(sys.getsizeof(var2)) #28
print(sys.getsizeof(var3)) #28
