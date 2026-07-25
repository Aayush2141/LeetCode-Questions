# Last updated: 26/07/2026, 03:36:32
1class Solution:
2    def convertTemperature(self, celsius: float) -> List[float]:
3        kelvin = celsius + 273.15
4        fahrenheit = celsius * 1.80 + 32.00
5
6        return [kelvin, fahrenheit]