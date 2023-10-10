import math
class shape:
    def __init__(self,n,sideL):
        self.n = n
        self.sideL = sideL
        self.area = (self.n*self.sideL/(2*(math.tan(math.pi/self.n))/self.sideL))/2
    
    def __str__(self):
        return  f"n: {self.n}" \
                f"sideL: {self.sideL}"
    
    def save(self):
        in_file = "shapes.config"
        with open(in_file, "w") as file:
            file.write(self.__str__())

x = True
while x:
    try:

        shape_view = input("View previous shape? Y/N")
        if shape_view == "Y":
            in_file = "shapes.config"
            with open(in_file, "r") as file:
                print(file.read())

        elif shape_view == "N":
            break
        else:
            raise ValueErrorshape_view= int(input('input an interger value for the number of sides of your regular polygon '))
        sideL = float(input('input the side length of your shape '))
        shape1 = shape(n,sideL)
        print('your shape\'s area is ',shape1.area)

        save_confirm = input("Save this shape? Y/N:\n")
        if save_confirm == "Y":
            shape1.save()
        elif save_confirm == "N":
            break
        else:
            raise ValueError

        if bool(input('would you like to continue? (True/False) ')):
            break
    except:
        print('there was an error')