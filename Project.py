print ("===================================")
print ("     RIDE-HAILING FARE CALCULATOR")
print ("===================================")

# Display ride options
print ("\nChoose your ride type:")
print ("1.Economy")
print ("2.Premium")

# Get user's ride type
ride_type = input("Enter your choice (1 or 2):")

# Get distance
distance = float(input("Enter distance travelled(km):"))

peak_hour = input("Is it peak hour? (y/n):").lower()
raining = input("Is it raining? (y/n):").lower()
student = input("Are you a student? (y/n):").lower()

if ride_type == "1":
    ride_name = "Economy"
    base_fare = 5.00
    rate_per_km = 1.20

elif ride_type == "2":
    ride_name = "Premium"
    base_fare = 8.00
    rate_per_km = 2.00

else:
    print("\nInvalid ride type.")
    exit()

distance_fare = distance * rate_per_km
subtotal = base_fare + distance_fare

surcharge = 0
if peak_hour == "y":
    surcharge = surcharge + (subtotal * 0.20)
if raining == "y":
    surcharge = surcharge + (subtotal * 0.10) 

discount = 0
if student == "y":
    discount = discount + (subtotal * 0.15)     # student -15%
if distance > 20:
    discount = discount + (subtotal * 0.05) 
