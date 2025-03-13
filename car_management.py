class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, _make, _model, _year, _mileage, _services, _id=total_cars+1):
        self._make = _make
        self._model = _model
        self._year = _year
        self._mileage = _mileage
        self._services = _services


        CarManager.total_cars += 1
        self._id = CarManager.total_cars

        CarManager.all_cars.append(self)

    def __str__(self):
        return f"{self._id} || {self._make} ||{self._model} || {self._year} || {self._mileage} || {self._services}"

    @property
    def get_id(self):
        return self._id

    @classmethod
    def get_all_cars(cls):
        return cls.all_cars

    def get_car_details(self, id):
        pass


##################################################################
def run_terminal():
    while True:
        terminal_msg = """\n----  WELCOME  ----
    1. Add a car
    2. View all cars
    3. View total number of cars
    4. See a car's details
    5. Service a car
    6. Update mileage
    7. Quit\n"""

        print(terminal_msg)
        user_input = input("Please type a number option: ")

        clean_input = validate_input(user_input)

        if clean_input == 7:
            print("Thank you for visiting, comeback soon!!!")
            break

        option_selected(clean_input)


def validate_input(u_input):
    try:
        input_to_int = int(u_input)

        if int(input_to_int) > 0 and int(input_to_int) < 8:
            return input_to_int
        else:
            print("\n*** Numbers between 1-7 ONLY! ***\n")
    except:
        print("\n*** Only numbers are allowed! ***\n")


def option_selected(option):
    if option == 1:
        add_a_car(option)
    elif option == 2:
        view_all_cars()
    elif option == 3:
        print(f"\nCurrently we have {CarManager.total_cars} {'car' if CarManager.total_cars == 1 else 'cars' } in our inventory")
    elif option == 4:
        # car_id = input("Please type the car's ID: ")
        see_car_detail()
    elif option == 5:
        service_a_car("existing_customer")
    elif option == 6:
        update_mileage()
    else:
        return option


def add_a_car(option):
    make = input("Type car make: ")
    capitalized_make = make.capitalize()
    make_validated = validate_car_options(make, "make")
    while not make_validated:
        make = input("Type car make: ")
        make_validated = validate_car_options(make, "make")

    model = input("Type car model: ")
    model_validated = validate_car_options(model, "model")
    while not model_validated:
        model = input("Type car model: ")
        model_validated = validate_car_options(model, "model")

    year = input("Type car's year: ")
    year_validated = validate_car_options(year, "year")
    while not year_validated:
        year = input("Type car's year: ")
        year_validated = validate_car_options(year, "year")

    mileage = input("Type car's current mileage: ")
    mileage_validated = validate_car_options(mileage, "mileage")
    while not mileage_validated:
        mileage = input("Type car's current mileage: ")
        mileage_validated = validate_car_options(mileage, "mileage")

    service = service_a_car("new_customer")
    car = CarManager(make, model, year, mileage, [service])
    # services = service_a_car("new_car")
    # services = input("Type the service performed to the car: ")
    # car = CarManager(f"{make}", f"{model}", f"{year}", f"{mileage}", f"{services}")

    # car_one = CarManager('Ford', "express", 1990, 12345, "oil change")
    # car_two = CarManager('Chevrolet', "Sylverado", 2017, 250123, "Air filter changed")
    pass


def view_all_cars():
    print("\n    *** CARS' INVENTORY ***\n")
    for car in CarManager.get_all_cars():
        print(f"{car._id}) {car._make} || {car._model} || {car._year} || {car._mileage} || {car._services}")


def validate_car_options(u_input, option):
    car_makes = [
        "Acura", "Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti",
        "Buick", "Cadillac", "Chevrolet", "Chrysler", "Citroën", "Dodge", "Ferrari",
        "Fiat", "Ford", "Genesis", "GMC", "Honda", "Hyundai", "Infiniti", "Jaguar",
        "Jeep", "Kia", "Lamborghini", "Land Rover", "Lexus", "Lincoln", "Maserati",
        "Mazda", "McLaren", "Mercedes-Benz", "Mini", "Mitsubishi", "Nissan", "Peugeot",
        "Porsche", "Ram", "Renault", "Rolls-Royce", "Saab", "Subaru", "Suzuki",
        "Tesla", "Toyota", "Volkswagen", "Volvo"
    ]

    if option == 'make':
        if not u_input.isalpha():
            print("No numbers or special characters allowed!!!")
            return False
        elif u_input.capitalize() not in car_makes:
            print(f"{u_input} is NOT a correct make, try again!")
            return False
        elif u_input.capitalize() in car_makes:
            return True
    elif option == "model":
        if u_input.isalnum():
            return True
        else:
            print(f"NO special characters allowed. Try again!")
            return False
    elif option == "year":
        if u_input.isnumeric():
            if len(u_input) > 4 or len(u_input) < 4:
                print("Year must be in YYYY format")
                return False
            else:
                return True
        else:
            print("Only numbers are allowd. Try again!")
            return False
    elif option == "mileage":
        if u_input.isnumeric():
            return True
        else:
            print("Only numbers are allowd. Try again!")
            return False
    return True


def see_car_detail():
    total_cars = CarManager.total_cars
    cars_db = CarManager.all_cars
    print(f"\nCar's ID should not be greater than {total_cars}")

    while True:
        car_id = input("Please type the car's ID: ")
        int_car_id = int(car_id)

        if car_id.isnumeric():
            if int_car_id > total_cars:
                print(f"Car's ID should not be greater than {total_cars}")
            else:
                print(cars_db[int_car_id - 1])
                break


def service_a_car(type_customer):
    basic_car_services = [
    "Oil Change",
    "Tire Rotation",
    "Brake Inspection & Replacement",
    "Air Filter Replacement",
    "Fuel System Cleaning",
    "Computer Diagnostics",
    "Emission Test & Inspection"
    ]
    
    print("*** Basic Car Services ***\n ")
    
    if type_customer == "existing_customer":
        total_cars = CarManager.total_cars
        cars_db = CarManager.all_cars

        print(f"\nCar's ID should not be greater than {total_cars}")
        car_id = input("Please type car's ID: ")
        
        service = services()
        cars_db[int(car_id) - 1]._services.append(service)
    else:
        return services()


def services():
    basic_car_services = [
        "Oil Change",
        "Tire Rotation",
        "Brake Inspection & Replacement",
        "Air Filter Replacement",
        "Fuel System Cleaning",
        "Computer Diagnostics",
        "Emission Test & Inspection"
    ]
        
    for index, service in enumerate(basic_car_services):
        print(f"{index + 1}) {service}")

    service_num = input("\nType the service number performed to the car: ")
    while True:
        if int(service_num) > len(basic_car_services):
            print(f"Number should be smaller than {len(basic_car_services) + 1}")
        else:
            print(f"{basic_car_services[int(service_num) - 1]} has been added!")
            break
    return basic_car_services[int(service_num) - 1]


def update_mileage():
    total_cars = CarManager.total_cars
    cars_db = CarManager.all_cars

    print(f"\nCar's ID should not be greater than {total_cars}")
    car_id = input("Please type car's ID: ")
    new_mileage = input("Please type new mileage: ")
    cars_db[int(car_id) - 1]._mileage = new_mileage
    # print(">>>>ID", car_id)
run_terminal()
