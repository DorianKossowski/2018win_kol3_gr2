import random
from plane import Plane, sign

class Environment:
    def __init__(self):
        self.plane = Plane()

    def turbulence(self):
        self.plane.current_angle += (random.random() -0.5) * 90
        return self.plane.current_angle

    def flight(self):
        while True:
            self.turbulence()
            m_string = "Current angle: {}  Correction: {}".format(self.plane.current_angle, self.plane.correction())
            yield m_string
            self.plane.current_angle + self.plane.correction()

    def run(self,user_input):
        self.plane.current_angle = 90
        new_flight = self.flight()
        
        while user_input in ['y', 'yes']:
            if self.plane.is_crashed():
                print("Sorry, Your plane crashed!")
                break
            
            print(next(new_flight))
            user_input = input("Do You want to continue flynig?\n\r")
        else:
            print("We are landing")
