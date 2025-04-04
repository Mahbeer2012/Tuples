# creat a  tule with diffrent data types
tuplex =  ("tuple", False , 3.2 ,1)
print(tuplex)

#creat a tuple
tuplex = (4 , 6 , 2 , 8 , 3 , 1)
print(tuplex)
#tuples are immutable so you can not add new elements 
#using  merge of tuples with the + operator you can add an element and it will create a  new tuple
tuplex = tuplex + (9,)
print (tuplex)

# counts the numnber of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
 
# creat a tuple
tuple  = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple [start:stop] the start index is inclusive and the stop index
__slice = tuplex[3:5]
#is exclusive 
print(__slice)
#if the start index isn't defined, is taken from the bej inning of the tuple
__slice = tuplex[:6]
print(__slice)
