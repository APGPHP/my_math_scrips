R = int(input("Enter radius of a circle: "))
steps = int(input("Enter no. of divisions / no. of values of dr: "))

dr = round(R/steps, 1)
A = 3.14159 * R * R
a = 0
r = 0

while R > r:
    
    r += round(R/steps, 1)
    
    a += 2.0*3.14159*r * dr

print("Actual area =", A, "Experimental area =", a, "Closeness =", str((a/A)*100) + "%")
