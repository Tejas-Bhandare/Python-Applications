# Q6. Celsius to Fahrenheit Converter
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:
# F = (C × 9/5) + 32

# Expected Input:
# Enter temperature in Celsius: 25

# Expected Output:
# Temperature in Fahrenheit: 77.0°F

class Weather:
    def __init__(self, temp):
        self.temperature = temp

    def convTempCelsiusTofarenheit(self):
        fTemp = 0
        fTemp = (self.temperature * (9 / 5)) + 32
        return fTemp

def main():
    print("Enter Temperature in celsius :")
    value = int(input())

    wobj = Weather(value)
    result = wobj.convTempCelsiusTofarenheit()

    print("Temperature in Fahrenheit:", result,"F")

if __name__ == "__main__":
    main()