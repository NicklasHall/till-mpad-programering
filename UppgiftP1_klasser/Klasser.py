import os 
# class Car:   #en Klass har alltid stor bokstav
#     def __init__(self, name):
#         self.name = name 


    
# car = Car("Volvo")
        
# print(car.name)


# class Car:   #en Klass har alltid stor bokstav
#      def __init__(self):
#          self.car_details = {}

#      def add_car(self, make, model):
#         self.car_details[make] = make
#         self.car_details[model] = model

#      def list_cars(self):
#          for i in self.car_details:
#              print(i) 

# car = Car()
# car.add_car("Volvo", "940")
# car.list_cars()




# class Car:
#     def __init__(self):
#         self.car_details = {}

#     def add_car(self, make, model):
#         if make in self.car_details:
#             self.car_details[make].append(model) 
#         else:
#             self.car_details[make] = [model]  

#     def list_cars(self):
#         list_number = 1
#         for make, models in self.car_details.items():
#             for model in models:
#                 print(f"{list_number}) {make} - {model}")
#                 list_number += 1



# car = Car()

# while True:
#     make = input("Skriv in ett bil märke, eller skriv klar: ")
#     if make.lower() == 'Klar':
#         break
#     model = input(f"Skriv en model för bil märket {make}: ")
#     car.add_car(make, model)

# print("\nCars in the list:")
# car.list_cars()

    

class Car: 
    def __init__(self, make, model, color):
        self.make = make    
        self.model = model
        self.color = color 

    def view_car(self):
        return f"{self.make} - {self.model} ({self.color})"    
    
    

def list_cars():
    for index,  car in enumerate(cars, 1):
        print(f"{index} {car.view_car()}") 

 
os.system("cls")


cars = []

while True:
    make = input("make: ")
    model = input("model: ")
    color = input("color: ")

    cars.append(Car(make, model, color))

    list_cars()



# cars.append(Car("Lada", "Kalina", "Yellow"))
# cars.append(Car("Volvo", "940", "Silver"))
# cars.append(Car("Lada", "Kalina", "Yellow"))
# cars.append(Car("Lada", "Kalina", "Yellow"))

# for car in cars: 
#     print(car.view_car())