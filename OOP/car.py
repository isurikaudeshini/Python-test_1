class Car:
    top_speed = 100  #attribute
    warnings = []

    def drive(self): #self is not a reserved keywoord , convention is to go with self. i.e. access variables within the class
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

car1 = Car()  #Constructor, Construct a new instance of Car class
car1.drive() #method on that object

car1.warnings.append('New warning')
#Car.top_speed = 200

car2 = Car()
car2.drive() #method on that object
print(car2.warnings)

car3 = Car()
car3.drive() #method on that object
print(car3.warnings)
