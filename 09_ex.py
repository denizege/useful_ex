# 9. Размер в байтах

# Этот пример возвращает длину строки в байтах, что удобно, когда вам нужно знать размер строковой переменной.

def ByteSize(string):
    return len(string.encode("utf8"))
ByteSize("Python") #6
ByteSize("Data") #4
