class Bike():
    def __init__(self,bike_name,bike_colour,bike_milege):
        self.a=bike_name
        self.b=bike_colour
        self.c=bike_milege
    def Data(self):
        print("Bike_name:",self.a)
        print("Bike_colour:",self.b)
        print("Bike_milege:",self.c)

Bike_obj=Bike("KTM","BLACK","6000MAH")
Bike_obj.Data()




