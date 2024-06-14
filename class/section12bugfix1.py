def get_maximum():
    celsius_local = [14, 15.1, 12.3]
    maximum_local = max(celsius_local)
    return maximum_local


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)