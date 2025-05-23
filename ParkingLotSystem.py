from datetime import datetime
import math

# Initializing a car
class Car():
    def __init__(self, number_plate: str, car_type: int):
        self.number_plate = number_plate
        self.car_type = car_type
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"{self.number_plate} (Type {self.car_type}) @ {self.timestamp}"

# Initializing the Parking Lot
class ParkingLot():
    def __init__(self, Hatchbacks: int, Sedans: int, SUVs: int):
        self.capacity = {1: Hatchbacks, 2: Sedans, 3: SUVs}
        self.available = self.capacity.copy()
        self.lot = {}

    def add_car(self, number_plate:str, car_type: int) -> bool:
        if number_plate in self.lot:
            print(f"{number_plate} Already Parked.")
            return False
        elif self.available.get(car_type, 0) > 0:
            self.available[car_type] -= 1
            self.lot[number_plate] = Car(number_plate, car_type)
            print(f"{number_plate} Parked Successfully.")
            return True
        print("Parking Full.")
        return False
    
    def remove_car(self, number_plate: str) -> bool:
        if number_plate in self.lot:
            self.available[self.lot[number_plate].car_type] += 1
            amount = math.ceil(float((datetime.now() - self.lot[number_plate].timestamp).total_seconds())/3600) * 30
            self.lot[number_plate].timestamp
            self.lot.pop(number_plate, None)
            print(f"Total Amount - INR{amount}")
            return True
        print(f"{number_plate} Not Parked")
        return False

    def status(self):
        print(f"Available Parking Slots: Hatchbacks:{self.available[1]}/{self.capacity[1]}, Sedans:{self.available[2]}/{self.capacity[2]} SUVs:{self.available[3]}/{self.capacity[3]}")
        print("Cars Parked - ")
        for car in self.lot.values():
            print(f"\t{car}")

def main():
    print("=== PARKING LOT SYSTEM ===")
    parking = ParkingLot(Hatchbacks=1, Sedans=1, SUVs=1)
    while True:
        print("1. Park\n2. Remove\n3. Availability\n4. Exit\n")
        choice = input("Enter your choice - ").lower()
        if choice in ["1", "park"]:
            try:
                number_plate = input("Vehicle Number - ")
                car_type = int(input("Car Type - "))
                parking.add_car(number_plate = number_plate, car_type = car_type)
            except ValueError:
                print("Car type should be 1 for Hatchbacks, 2 for Sedans, 3 for SUVs")
        elif choice in ["2", "remove"]:
            number_plate = input("Vehicle Number - ")
            parking.remove_car(number_plate = number_plate)
        elif choice in ["3", "status", "availability"]:
            parking.status()
        elif choice in ["4", "exit", "bye"]:
            break
        else:
            print("Invalid Input, Retry")

if __name__=="__main__":
    main()
