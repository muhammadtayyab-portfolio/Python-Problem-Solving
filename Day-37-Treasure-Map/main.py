
map_list1 = ["⬜","⬜","⬜"]
map_list2 = ["⬜","⬜","⬜"]
map_list3 = ["⬜","⬜","⬜"]
map_grid = [map_list1, map_list2, map_list3]
print(f"{map_list1}\n{map_list2}\n{map_list3}")

user = input("Please enter the cordinates to marke the possitio : ")

sel_row = int(user[0])
sel_col = int(user[1])
map_grid[sel_row-1][sel_col-1] = "❌"
print(f"{map_list1}\n{map_list2}\n{map_list3}")