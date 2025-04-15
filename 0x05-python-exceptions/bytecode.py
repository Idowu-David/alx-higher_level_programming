import dis
def magic(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c

print(dis.dis(magic))