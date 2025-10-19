#Q2
# (i) Tuple of 3 elements, attempt to change one element 

my_tuple = (10, 20, 30)
try:
    my_tuple[1] = 99
except TypeError as e:
    print("Error:", e)

# (ii) List of 3 elements, change one element

my_list = [10, 20, 30]

my_list[1] = 99
print(my_list)



# (iii) Dictionary with 2 key-value pairs, update one value
my_dict = {"name": "Ash", "age": 22}


my_dict["age"] = 23
print(my_dict)  


# (iv) Tuple with 2 sub-lists, modify inside a sub-list
my_tuple_with_lists = ([1, 2, 3], [4, 5, 6])


my_tuple_with_lists[0][1] = 99
print(my_tuple_with_lists)  


# Q3

def get_valid_name():
    name = input("Enter your name: ").strip()
    while not name:  
        print("Name cannot be empty. Please try again.")
        name = input("Enter your name: ").strip()
    return name


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 < age < 100:
                return age
            else:
                print("Age must be between 1 and 99. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if (
            "@" in email
            and "." in email
            and not email.startswith("@")
            and not email.endswith(".")
        ):
            return email
        else:
            print("Invalid email format. Try again.")


def get_valid_fav_number():
    while True:
        try:
            fav_number = int(input("Enter your favorite number (1-100): "))
            if 1 <= fav_number <= 100:
                return fav_number
            else:
                print("Favorite number must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# ---------------- MAIN PROGRAM ----------------
user_info = {
    "name": get_valid_name(),
    "age": get_valid_age(),
    "email": get_valid_email(),
    "favorite_number": get_valid_fav_number(),
}

# Display 
print(f"\nWelcome {user_info['name']}! Your account has been registered with email {user_info['email']}.")



# Q4

def calculate_ticket_price(age, is_student, is_weekend):
    # Validate age
    if age < 0 or age > 120:
        raise ValueError("Invalid age. Must be between 0 and 120.")

    # Base pricing
    if age < 12:
        price = 5
    elif 13 <= age <= 17:
        price = 8
    elif 18 <= age <= 59:
        price = 12
    else:  # Seniors (60+)
        price = 6

    # Apply student discount (20%) for age > 12
    if is_student and age > 12:
        price *= 0.8  # 20% discount

    # Weekend surcharge (+$2)
    if is_weekend:
        price += 2

    return round(price, 2)


# ---------------- MAIN PROGRAM ----------------
customers = []
total_revenue = 0

# Number of customers
num_customers = int(input("Enter number of customers: "))

for i in range(num_customers):
    print(f"\n--- Customer {i+1} ---")

    # Get age input
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0 or age > 120:
                raise ValueError
            break
        except ValueError:
            print("Invalid age. Please enter a number between 0 and 120.")

    # Student status
    student_input = input("Is the customer a student? (yes/no): ").strip().lower()
    is_student = (student_input == "yes")

    # Weekend status
    weekend_input = input("Is it a weekend show? (yes/no): ").strip().lower()
    is_weekend = (weekend_input == "yes")

    # Calculate ticket price
    price = calculate_ticket_price(age, is_student, is_weekend)
    total_revenue += price

    # Store customer info
    customers.append({
        "id": i + 1,
        "age": age,
        "student": is_student,
        "weekend": is_weekend,
        "ticket_price": price
    })

# ---------------- RESULTS ----------------
print("\n===== Ticket Summary =====")
for cust in customers:
    print(f"Customer {cust['id']}: Age={cust['age']}, Student={cust['student']}, Weekend={cust['weekend']}, Price=${cust['ticket_price']}")

# Highest and lowest paying customers
highest = max(customers, key=lambda x: x["ticket_price"])
lowest = min(customers, key=lambda x: x["ticket_price"])

print("\n===== Revenue Summary =====")
print(f"Total revenue (before group discount): ${round(total_revenue,2)}")
print(f"Highest-paying customer: Customer {highest['id']} (${highest['ticket_price']})")
print(f"Lowest-paying customer: Customer {lowest['id']} (${lowest['ticket_price']})")

# Apply group discount if 4+ customers
if num_customers >= 4:
    discount = total_revenue * 0.1
    total_revenue -= discount
    print(f"Group discount applied: -${round(discount,2)}")

print(f"Final Total Revenue: ${round(total_revenue,2)}")


# Q5

def weather_alert(temp_celsius, condition):
    # Convert temperature
    temp_f = (temp_celsius * 9/5) + 32
    temp_k = temp_celsius + 273.15

    if temp_celsius < 0 and condition.lower() == "snowy":
        alert = "Heavy snow alert! Stay indoors."
    elif temp_celsius > 35 and condition.lower() == "sunny":
        alert = "Heatwave warning! Stay hydrated."
    elif condition.lower() == "rainy" and temp_celsius < 15:
        alert = "Cold rain alert! Wear warm clothes."
    else:
        alert = "Normal weather conditions."

    
    return {
        "alert": alert,
        "celsius": temp_celsius,
        "fahrenheit": round(temp_f, 1),
        "kelvin": round(temp_k, 2)
    }


# ---------------- MAIN ----------------
weather_data = []

num_cities = int(input("Enter number of cities/customers to check weather: "))

for i in range(num_cities):
    print(f"\n--- City {i+1} ---")
    city_name = input("Enter city name: ")

 
    while True:
        try:
            temp_c = float(input("Enter temperature in Celsius: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


    condition = input("Enter weather condition (sunny/rainy/snowy/etc.): ")

    result = weather_alert(temp_c, condition)
    weather_data.append({
        "city": city_name,
        "condition": condition,
        **result
    })

# ---------------- RESULTS ----------------
print("\n===== Weather Report =====")
for data in weather_data:
    print(f"\nCity: {data['city']}")
    print(f"Condition: {data['condition'].capitalize()}")
    print(f"Temperature: {data['celsius']}°C | {data['fahrenheit']}°F | {data['kelvin']}K")
    print(f"Alert: {data['alert']}")


# Q6

def analyze_sales(sales_list):

    sorted_sales = sorted(sales_list)
    n = len(sorted_sales)

  
    max_sales = max(sorted_sales)
    min_sales = min(sorted_sales)

    
    if n % 2 == 1: 
        median_sales = sorted_sales[n // 2]
    else:  
        median_sales = (sorted_sales[n // 2 - 1] + sorted_sales[n // 2]) / 2

    return max_sales, min_sales, median_sales


# ---------------- MAIN ----------------
while True:
    try:
        
        raw_input = input("Enter at least 5 daily sales values (comma-separated): ")
        sales = [float(x.strip()) for x in raw_input.split(",") if x.strip()]

        if len(sales) < 5:
            print("Please enter at least 5 sales values.\n")
            continue
        break
    except ValueError:
        print("Invalid input. Enter only numbers separated by commas.\n")


max_sales, min_sales, median_sales = analyze_sales(sales)

print("\n===== Sales Analytics =====")
print(f"Highest sales day: {max_sales}")
print(f"Lowest sales day: {min_sales}")
print(f"Median sales: {median_sales}")

# Q7

def update_inventory(inventory_dict, item, quantity):
    if item not in inventory_dict:
        print(f" Item '{item}' not found in inventory.")
        return inventory_dict

    new_quantity = inventory_dict[item] + quantity
    if new_quantity < 0:
        print(f" Not enough stock for {item}. Available: {inventory_dict[item]}")
    else:
        inventory_dict[item] = new_quantity
    return inventory_dict


# ---------------- MAIN  ----------------
inventory = {
    "Laptop": 10,
    "Headphones": 15,
    "Mouse": 20,
    "Keyboard": 12,
    "Monitor": 8
}

print(" Initial Inventory:")
for k, v in inventory.items():
    print(f"{k}: {v}")

print("\n Shopping Cart Checkout")
for i in range(3):
    item = input(f"\nEnter item {i+1} to buy: ").strip()
    try:
        qty = int(input(f"Enter quantity for {item}: "))
    except ValueError:
        print(" Invalid quantity, skipping item.")
        continue

    inventory = update_inventory(inventory, item, -qty)

print("\n Updated Inventory:")
for k, v in inventory.items():
    print(f"{k}: {v}")

most_stocked = max(inventory.items(), key=lambda x: x[1])
least_stocked = min(inventory.items(), key=lambda x: x[1])

print("\n===== Inventory Summary =====")
print(f"Most stocked product: {most_stocked[0]} ({most_stocked[1]} units)")
print(f"Least stocked product: {least_stocked[0]} ({least_stocked[1]} units)")
