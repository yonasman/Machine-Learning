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
# car1.start_engine("corolla-1")
# encapsulation
class Speaker:
    # private attributes
    def __init__(self, color, model):
        self._color = color
        self._model = model
    # getters and setters
    def get_color(self):
        return self._color
    def set_model(self, new_model):
        self._model = new_model
speaker1 = Speaker("red","toyota")
# print(speaker1._color)
# inheritance
class SmartSpeaker(Speaker):
    def __init__(self,color,model, voice_assistance):
        super().__init__(color, model)
        self.voice_assistant = voice_assistance
        
    def say_hello(self):
        print(f'Hello {self.get_color()}')
smartSpeaker1 = SmartSpeaker('yellow','toyota','eliza')
# smartSpeaker1.say_hello()