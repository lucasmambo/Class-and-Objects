class Temperature:
    def __init__(self,celsius,fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def convertFahrenheit(self):
        return (self.celsius*9/5)+32

    def convertCelsius(self):
        return (self.fahrenheit-32)*5/9
t = Temperature(60,45)
print("60°C is",t.convertFahrenheit(),"in Fahrenheit")
print("45°F is",t.convertCelsius(),"in Celsius")