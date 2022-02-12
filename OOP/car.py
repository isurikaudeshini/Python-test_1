class Car:
    top_speed = 100.0

    def drive(self): #self is not a reserved keywoord , convention is to go with self. i.e. access variables within the class
        print('I am driving but certainly not faster than {}'.format(self.top_speed))

car1 = Car()  #Constructor, Construct a new instance of Car class
car1.drive() #method on that object
