#Numeric Lists
import numpy
pricelist=[230,175,300,175,220,310,250,180] #you can not apply max or min when the list is mixed with numbers and letters
print("Maximum Price = ", max(pricelist))
print("Minimum Price = ", min(pricelist))
print("Sum of All Price = ", sum(pricelist))
#finding the average with numpy
print("Average of All Price = ", numpy.mean(pricelist))

