# Function to calculate hotel cost
def hotel_cost(num_nights):
    return num_nights * 100 # Assume hotel costs $100 per night

# Function to calculate plane cost
def plane_cost(city_flight):
    if city_flight == "New York":
        return 200 # Assume flight to New York costs $200
    elif city_flight == "London":
        return 500 # Assume flight to London costs $500
    elif city_flight == "Tokyo":
        return 800 # Assume flight to Tokyo costs $800
    else:
        return 0 # Return 0 if the city is not in the list

# Function to calculate car rental cost
def car_rental(rental_days):
    return rental_days * 50 # Assume rental costs $50 per day

# Function to calculate holiday cost
def holiday_cost(city_flight, num_nights, rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

# Get user inputs
city_flight = input("Enter the city you will be flying to (New York, London, Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days that you will be hiring a car for: "))

# Calculate holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Print out holiday details
print("Your holiday details:")
print("City of flight:", city_flight)
print("Number of nights at hotel:", num_nights)
print("Number of days for car rental:", rental_days)
print("Total holiday cost: $", total_cost)
#End of code