class Vehicle(object):
    """ a demo class for vehicles
    superclass of cars and trucks """
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.owners = []
        self.hasOwners = False
        self.mpgExists = False
    
    def addMPG(self, miles, gallons):
        """ assumes two numeric values """
        try:
            self.mpg = round(miles/gallons,2)
            self.mpgExists = True
        except ZeroDivisionError:
            print "Cannot enter Zero as gallons."
        except TypeError:
            print "Requires two numerical values"

    def getMPG(self):
        return self.mpg[:]

    def addOwner(self, name):
        """ assumes character string """
        if(name not in self.owners):
            self.owners.append(name)
            self.hasOwners = True
        else:
            print name + "already in list of owners"
    
    def listOwners(self):
        return self.owners[:]

    def isTruck(self):
        return isinstance(self, Truck)

    def __str__(self):
        msg = self.make + " " + self.model 
        if self.hasOwners:
            msg = msg + " owned by" + " " + str(self.owners[-1])
        else:
            msg = "brand new " + msg
        if self.mpgExists:
            msg = msg + " " + "and has a mpg of" + " " + str(self.mpg)
        return msg

class Truck(Vehicle):
    def __init__(self, make, model, wheels, bed_size):
        Vehicle.__init__(self, make, model)
        self.wheels = wheels
        self.bed_size = bed_size
    
    def isTruck(self):
        return isinstance(self, Truck)

    def __str__(self):
        msg = " ".join(["Truck Specs:", self.make,  self.model, " with" , str(self.wheels), "wheels",
            "and a bed size of", str(self.bed_size), "square feet"]) 
        return(msg)

v1 = Vehicle("ford", "ranger")
v1.addMPG(100, 5)
print v1

v1.addOwner("jeff")
v1.addOwner("brian")
v1.listOwners()
print v1

v1.isTruck()

v2 = Vehicle("toyota", "prius")
v2.addMPG(10, 0)
v2.addOwner(v1.listOwners())
print v2

t1 = Truck("big", "truck", 16, 1000)
print(t1.isTruck())
print t1