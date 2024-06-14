# Define a  water_state function that:
# 1. gets a temperature argument
# 2. returns the string "Solid" if the temperature is less than or equal to 0
# 3. returns "Liquid" if the temperature is greater than 0, but less than 100.
# 4. returns "Gas" if the temperature is greater than or equal to 100.
from func_water_state import water_state
temperature = float(input("Enter temperature: "))

print(water_state(temperature))