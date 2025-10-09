class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet," + str(self.inches) + " inches"
        return output
    
    def __sub__(self, other): 
        # converting both object's height into inches
        height_A_inches = self.feet * 12 + self.inches
        height_2_sub = other.feet * 12 + other.inches

        # subtracting them
        total_height_inches = height_A_inches - height_2_sub

        #getting the output in feet
        output_feet = total_height_inches // 12

        # getting the output in inches
        output_inches = total_height_inches - (output_feet * 12)

        #returning final output as new Height object
        return Height(output_feet,output_inches)

person_A_height = Height(5,10)
amount_2_sub = Height(3,9)
height_sub = person_A_height - amount_2_sub

print("New Height: ", height_sub)