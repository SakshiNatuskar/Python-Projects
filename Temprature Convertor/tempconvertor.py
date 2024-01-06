print("Temperature Converter")

choice = input("Choose conversion type (1 for Fahrenheit to Celsius, 2 for Celsius to Fahrenheit): ")

if choice == "1":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
else:
    print("Invalid choice. Please enter either 1 or 2.")
