import math

def paint_cal(h,w):
    volume = h*w
    volume_pr_square = math.ceil(volume/5)
    return volume_pr_square

wall_height = int(input("Please enter hight of the wall : "))
wall_width = int(input("Please enter weight of the wall : "))

number_of_cans = paint_cal(wall_height,wall_width)
print(f"You'll need {number_of_cans} cans of paint.")
