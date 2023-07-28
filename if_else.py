x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1 coordinate plane")
elif x > 0 and y < 0:
    print("4 coordinate plane")
elif x < 0 and y > 0:
    print("2 coordinate plate")
elif x < 0 and y < 0:
    print("3 coordinate plate")
elif x == 0 and y > 0:
    print("Y-axis - upper coordinate half-plane (1 or 2 coordinate plate)")
elif x == 0 and y < 0:
    print("Y-axis - lower coordinate half-plane (3 or 4 coordinate plate)")
elif x > 0 and y == 0:
    print("X-axis - right coordinate half-plane (1 or 4 coordinate plate)")
elif x < 0 and y == 0:
    print("X-axis - right coordinate half-plane (2 or 3 coordinate plate)")
elif x == 0 and y == 0:
    print("Origin of coordinates")
else:
    print("ERROR !")