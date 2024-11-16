class Car:
    # class attribute
    wheels = 4
    
    # constructor
    def __init__(self,make,model):
        # instance attributes
        self.make = make
        self.model = model
    # method
    def start_engine(self,name):
        print(f'The engine of {name} is now running.')

# object instances
car1 = Car("Toyota","Corolla")
car1.start_engine("corolla-1")