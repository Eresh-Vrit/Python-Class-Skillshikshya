class Car:
    def __init__(self, model:str, year: int, color: str):
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print(f"{self.model} is driving.........")
    
    def stop(self):
        print(f"{self.model} stopped!!")

    def describe(self):
        print(f"This car model is {self.model}. Year: {self.year}. Color: {self.color}")




    


