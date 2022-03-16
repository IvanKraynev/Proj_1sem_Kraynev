# Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

from string import punctuation

string_new = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'
str = [i for i in string_new if i in punctuation]
print(str)