def calculate_car_wash_price(service_choice1, service_choice2):
    
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10  
    total = base_wash  
    selected_services = []  # List to store selected services
    
    if service_choice1 != '-':
        total += services.get(service_choice1, 0)
        selected_services.append((service_choice1, services.get(service_choice1, 0)))
        
    if service_choice2 != '-':
        total += services.get(service_choice2, 0)
        selected_services.append((service_choice2, services.get(service_choice2, 0)))
    
    print("ZyCar Wash")
    print(f"Base car wash - ${base_wash}")
    
    for service, cost in selected_services:
        print(f"{service} - ${cost}")
    
    print(f"Total price: ${total}")

if __name__ == '__main__':
    
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    
    calculate_car_wash_price(service_choice1, service_choice2)
