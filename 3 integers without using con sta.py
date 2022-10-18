x=int(input("Enter first number ...."))
y=int(input("Ente second number..."))
z=int(input("Enter third number...."))
a1=min(x,y,z)
a3=max(x,y,z)
a2=(x+y+z)-a1-a3
print("Numbers in sorted order",a1,a2,a3)