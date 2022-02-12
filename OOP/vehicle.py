class Vehicle:
     def __init__(self,starting_top_speed=100):
        self.top_speed = starting_top_speed    #Instance attribute
        self.__warnings = []

     def __repr__(self):
        print('Printing..')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed,len(self.__warnings))

     def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text) #double underscore in front is used to tell private variable or private attribute
                                                 #can access only form inside the class
     def get_warnings(self):
        return self.__warnings

     def drive(self): #self is not a reserved keywoord , convention is to go with self. i.e. access variables within the class
        print('I am driving but certainly not faster than {}'.format(self.top_speed))