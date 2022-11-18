#Tuple - kind of a list that only can be searched not mathamatical equ. 
#python prefers python for speed
import numpy
pricelist=(230,175,300,175,220,310,250,180) #if the values have parentasis its a tuple 
print("Maximum Price = ", max(pricelist))
print("Minimum Price = ", min(pricelist))
print("Sum of All Price = ", sum(pricelist))
print("Average of All Price = ", numpy.mean(pricelist))
print(type(pricelist))
