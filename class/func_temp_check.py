def temp_check(temperature):
    if temperature < 15:
        return "Cold"
    elif 15 <= temperature <= 25:
        return "Warm"
    else:
        return "Hot"
