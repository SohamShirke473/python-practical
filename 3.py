def area_of_square(side):
    return side * side

def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_triangle(base, height):
    return 0.5 * base * height

try:
      
    print("1. Area of Square")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        side = float(input("Enter the side of the square: "))
        area = area_of_square(side)
        print(f"Area of Square: {area:.2f} square units")

    elif choice == "2":
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        area = area_of_rectangle(length, breadth)
        print(f"Area of Rectangle: {area:.2f} square units")

    elif choice == "3":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_of_triangle(base, height)
        print(f"Area of Triangle: {area:.2f} square units")

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

except ValueError:
    print("Invalid input! Please enter numeric values only.")


