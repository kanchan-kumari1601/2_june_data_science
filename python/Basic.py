# print("hello")
# print("world")


# a=2
# b=3
# print(a)
# print(b)

# name="kanchan "
# age=20
# print(name)
# print(age)

# name="kanchan   "
# print(name)
# print(type(name))

# lastname= "kumari"
# print(name+ lastname)


# name="kanchan"
# #indexing
# print(name[0])
# print(name[2])


# #slicing
# print(name[0:3])

# city="Jamshedpur"
# print("Hello I am from " +city)


# company_name="upflairs"
# print("length of company name:-",len(company_name))




# #>>>>>>>>>tuple>>>>>>>>>>>>>>>>>>>>>>>>>
#  ## ordered and unchangeable
#  #heterogenous
#  ##allow duplicate values
 
# tpl=(1,2,3,4,"hello","world",2.5)
# print(tpl)
# print("length of tpl:-",len(tpl))

# ##slicing
# print(tpl[0:5])

# print(2 in tpl)



# #max
# #min
# #sum
# # tpl(1,2,3,4,5)
# # print(max(tpl))


# ##tuple unpacking
# # kapil=1,2,3
# # print(kapil)
# # a,b,c=kapil
# # print("a-",a)
# # print("b-",b)
# # print("c-",c)


# t1=(1,2)
# t2=(3,4,2)
# print(t1+t2)

# t2=(3,4,2)
# print(t2*3)

# t2=(3,4,2,(1,2))
# print(len(t2))

# print(t2[3][0])

# t=(1,2,3,4,5,6,7,8,9)
# print(t.index(8))
# print(t.count(5))



####>>>>>>>>>>>dict>>>>>>>>>>>>

##A dictionary (or dict) in Python is a collection of key-value pairs. It is unordered, mutable, and indexed by keys (not positions like lists or tuples).

# my_dict = {
#     "name": "kanchan",
#     "age": 20,
#     "city": "jamshedpur"
# }
# print(my_dict)

# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["city"])

# ##adding new key valu pair
# my_dict['country']="India"
# print(my_dict)

##task 1::: Access the element 7 from a tuple 
 #(1,2,3,4,5,5,[45,7,8,8]) 
tpl = (1, 2, 3, 4, 5, 5, [45, 7, 8, 8])
print(tpl[6][1])


# ##task 2 updating vlues of dict
my_dict = {
    "name": "kanchan",
    "age": 20,
    "city": "jamshedpur"
}

##updating values
my_dict["age"] = 21       
my_dict["gender"] = "Female" 

##task3 operators 
a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)   
print("a - b =", a - b)   
print("a * b =", a * b)   
print("a / b =", a / b)   
print("a // b =", a // b) 
print("a % b =", a % b)   
print("a ** b =", a ** b) 

print("\nComparison Operators:")
print("a == b:", a == b)  
print("a != b:", a != b)   
print("a > b:", a > b)      
print("a < b:", a < b)      
print("a >= b:", a >= b)    
print("a <= b:", a <= b) 

print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)  
print("x or y:", x or y)    
print("not x:", not x) 



# ##removing key value pair from dict
# # del my_dict['country']
# # print(my_dict)

# my_dict.pop("country")
# print(my_dict)

# ##dict methods

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# ##checking for a key
# print("name" in my_dict)
# print("hello" in my_dict)


# ###>>>>>>>>>>>>set>>>>>>>>>>>>
# ##heterogenous
# #no duplicate value

# my_set={1,2,3,4,5,}
# print(my_set)

# my_set={1,2,3,4,5,5}
# print(my_set)


# my_set=set()

# my_set={1,2,3,4,5}
# my_set.add(6)
# print(my_set)
# my_set.remove(6)
# print(my_set)


##type casting
# name=[1,2,3,4,5]
# print(name)
# print(type(name))
# #convert into set
# name=set(name)
# print(name)
# print(type(name))