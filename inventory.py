import math


print ("Welcome to the container inventory program!")
print ("")

# Calculate the volume of the sphere
def calc_Vsphere(r):
    return (4.0/3.0) * math.pi * math.pow(r,3)
# Calculate the area of the sphere
def calc_Ssphere(r):
    return 4.0 * math.pi * math.pow(r,2)
# Calculate the volume of the rectangular
def calc_Vrect(l, w, h):
    return l * w * h
# Calculate the area of the rectangular
def calc_Srect(l, w, h):
    return 2 * (l * w + l * h + w * h)
# Calculate the volume of the cylinder
def calc_Vcylinder(r, h):
    return  math.pi * math.pow(r,2) * h
# Calculate the area of the cylinder
def calc_Scylinder(r, h):
    return 2.0 * math.pi * r * h + 2.0 * math.pi * math.pow(r,2)
# Calculate the volume of the cone
def calc_Vcone(r, h):
    return (1.0/3.0) * math.pi * math.pow(r,h) * h
# Calculate the area of the cone
def calc_Scone(r, h):
    return math.pi * r * (r + math.sqrt(pow(h,2) + pow(r,2)))

Vsphere = 0        # Define cumulative volume of sphere
Ssphere = 0        # Define cumulative area of sphere
Vrect = 0          # Define cumulative volume of rect
Srect = 0          # Define cumulative area of rect
Vcylinder = 0      # Define cumulative volume of cylinder
Scylinder = 0      # Define cumulative area of cylinder
Vcone = 0          # Define cumulative volume of cone
Scone = 0          # Define cumulative area of cone


indexSphere = 0    # Index of sphere
indexRect = 0      # Index of rectangular
indexCylinder = 0  # Index of cylinder
indexCone = 0      # Index of cone


quit = 0           # Define boolean condition false


while not quit:
    option = raw_input("What would you like to do? (add, printV, printSA, printNum, quit): ")

    if option == "add":
    
            shape = raw_input("What shape is the container? (sphere, rect, cone, cylinder): ")

            if shape == "sphere":
                indexSphere += 1
                r = float(raw_input("Radius (m): "))
                Vsphere += calc_Vsphere(r)
                Ssphere += calc_Ssphere(r)
               # print "Cumulative Volume of spheres: ", Vsphere
               # print "Cumulative Surface area of spheres: ", Ssphere
            elif shape == "rect":
                indexRect += 1
                l = float(raw_input("Length (m): "))
                w = float(raw_input("Width (m): "))
                h = float(raw_input("Height (m): "))
                Vrect += calc_Vrect(l, w, h)
                Srect += calc_Srect(l, w, h)
               # print "Cumulative Volume of rectangular prisms: ", Vrect
               # print "Cumulative Surface area of rectangular prisms: ", Srect
            elif shape == "cylinder":
                indexCylinder += 1
                r = float(raw_input("Radius (m): "))
                h = float(raw_input("Height (m): "))
                Vcylinder += calc_Vcylinder(r, h)
                Scylinder += calc_Scylinder(r, h)
               # print "Cumulative Volume of cylinder: ", Vcylinder
               # print "Cumulative Surface area of cylinder: ", Scylinder
            else:
                indexCone += 1
                r = float(raw_input("Radius (m): "))
                h = float(raw_input("Height (m): "))
                Vcone += calc_Vcone(r, h)
                Scone += calc_Scone(r, h)
               # print "Cumulative Volume of cone: ", Vcone
               # print "Cumulative Surface area of cone: ", Scone
    elif option == "printV":
         print "Total volumes (m^3):"
         print "Sphere: ", Vsphere
         print "Rectangular Prism: ", Vrect
         print "Cone: ", Vcone
         print "Cylinder: ", Vcylinder
    elif option == "printSA":
         print "Total surface area (m^2):"
         print "Sphere: ", Ssphere
         print "Rectangular Prism: ", Srect
         print "Cone: ", Scone
         print "Cylinder: ", Scylinder
    elif option == "printNum":
         print "Object counts:"
         print "Sphere: ", indexSphere
         print "Rectangular Prism:", indexRect
         print "Cone: ", indexCone
         print "Cylinder: ", indexCylinder
    else: 
         print "Goodbye!"
         exit(0)
