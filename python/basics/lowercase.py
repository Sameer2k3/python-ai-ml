text = "HeLLo WoRLD"
result = ""

for ch in text:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)