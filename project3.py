import array as arr

print("This is my array!")

#create an array
arraynum=arr.array("i", (1,2,3,4,5))
print("Original array: "+str(arraynum))

#count number of occurences
print("Number of occurences of 3 in said array: "+str(arraynum.count(3)))

#reverse the array

arraynum.reverse()
print("Reverse order of items in said array: ")
print(str(arraynum))
