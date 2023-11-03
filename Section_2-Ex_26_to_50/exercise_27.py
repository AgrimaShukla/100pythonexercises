# Acceleration Calculator

def acceleration(v1, v2, t1, t2):
    acc = (v2 - v1) / (t2 - t1)
    return acc

print(acceleration(0, 10, 0, 20))