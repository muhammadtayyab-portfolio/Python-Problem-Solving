# Ek string input lo aur first non-repeating character print karo.

str = input("Please enter any string...")
count = 0
found = False

while count <= len(str)-1:
    if str.count(str[count])==1:
       print("First non-repeating character is:", str[count])
       found = True
       break 
    count +=1

if not found:
    print("No non-repeating character found")