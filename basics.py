
num_list="0123456"
sliced_numlist = num_list[0:5]
print(sliced_numlist)

chai="lemon,masala,ginger"
# string to list
print(chai.split(","))
chai="masala chai"
# question asking or finding 
print("masala" in chai)

# lists
tea_varieties=["blacktea","greentea","oolong tea"]
print(tea_varieties)
print(tea_varieties[0])
# slicing dicing also works here 
tea_varieties[1]="coffe"
print(tea_varieties)
# replacing with slicing
tea_varieties[1:2]=["cold coffe"]
print(tea_varieties)

# .pop() deletes the last element 
tea_varieties.append("milk")
print(tea_varieties)

if "milk" in tea_varieties:
 print("i have milk")
 
# looping tea is a variable like i 
for tea in tea_varieties:
 print(tea)  
 print(tea,end="-")
 

 