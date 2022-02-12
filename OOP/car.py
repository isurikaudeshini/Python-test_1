class Car:
    # top_speed = 100  #attribute
    # warnings = []
    def __init__(self,starting_top_speed=100):
        self.top_speed = starting_top_speed    #Instance attribute
        self.warnings = []

    def __repr__(self):
        print('Printing..')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed,len(self.warnings))

    def drive(self): #self is not a reserved keywoord , convention is to go with self. i.e. access variables within the class
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

car1 = Car()  #Constructor, Construct a new instance of Car class
car1.drive() #method on that object

car1.warnings.append('New warning')
#print(car1.__dict__)
print(car1)
#Car.top_speed = 200

car2 = Car(200)
car2.drive() #method on that object
print(car2.warnings)

car3 = Car(250)
car3.drive() #method on that object
print(car3.warnings)
