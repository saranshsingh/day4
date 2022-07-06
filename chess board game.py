# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# First I split 2 numbers in List
# Stored in different variables acc. to values
column = [position[0]]
column[0] = "x"
row = [position[1]]
row[0] = "x"
# How to print only column ?
col1 = [row1[0] , row2[0] , row3[0] ] 
col2 = [row1[1] , row2[1] , row3[1] ] 
col3 = [row1[2] , row2[2] , row3[2] ] 
map_col = [col1 , col2 , col3]


# Now we have only columns 

# need to work on it I am 90 percent closer
a = map_col.append(column)
b = map.append(row)




  
  


# Now I will append them in output







#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")