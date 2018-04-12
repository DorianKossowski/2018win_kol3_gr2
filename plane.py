
def sign(x): 
    return 1 if x >= 0 else -1

class Plane:
    def __init__(self):
        self.current_angle = 90
        self.set_angle = 90

    def correction(self):
        return 20 * sign(self.set_angle - self.current_angle)

    def is_crashed(self):
        return (self.current_angle > 180 or self.current_angle < 0)

