units = {
    "length": {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "mile": 1609.34,
    },
    "mass": {
        "g": 0.001,
        "kg": 1,
        "t": 1000,
    },
    "time": {
        "sec": 1,
        "min": 60,
        "hour": 3600,
    },
}

print("Available types: length, mass, time")
print("Length: mm, cm, m, km, mile")
print("Mass: g, kg, t")
print("Time: sec, min, hour")

type_name = input("Enter measurement type: ")
from_unit = input("Enter source unit: ")
to_unit = input("Enter target unit: ")
value = float(input("Enter value: "))

result = value * units[type_name][from_unit] / units[type_name][to_unit]

print(f"{value} {from_unit} = {result:.4f} {to_unit}"