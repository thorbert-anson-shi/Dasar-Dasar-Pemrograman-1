class Park():
    def __init__(self) -> None:
        self.capacity = 10
        self.contents = []

    def add_car(self, id:str):
        if len(self.contents) < self.capacity:
            self.contents.append(id)
        else:
            print("Parking lot is full!")
    
    def remove_car(self):
        print("Which car would you like to remove?")
        [print(id) for id in self.contents]
        car_id = input("ID of car: ") 
        duration = input("How long did the car stay? (in seconds): ")
        self.contents.remove(car_id)
        print(f"Car {car_id} has been removed with a parking fee of {duration * 100}")

parking_lot = Park()
parking_lot.add_car("12345")
print(parking_lot.contents)