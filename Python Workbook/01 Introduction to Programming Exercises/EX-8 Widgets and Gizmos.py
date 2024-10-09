"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
"""
WEIGHT_OF_WIDGET = 75
WEIGHT_OF_GIZMO = 112
widget = int(input("Enter the no. of widget: "))
gizmo = int(input("Enter the no. of gizmo: "))
total_weight = widget * WEIGHT_OF_WIDGET + gizmo * WEIGHT_OF_GIZMO
print(f"The total weight of {widget} widgets and {gizmo} gizmos is {total_weight} grams.")
