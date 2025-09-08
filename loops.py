
squared_num=[x**2 for x in range(10)]
print(squared_num)


# dictonaries consist everything in sequential order with key value pairs
# in dictonaries we give both key and values while in list keys are pre defined 0,1...


chai_types= {"Masala":"spicy","ginger":"zesty","green":"mild"}
print(chai_types["Masala"])
print(chai_types.get("green"))
chai_types["green"]="fresh"
print(chai_types)


# itertaion in dictonary 
for chai in chai_types:
 print(chai,chai_types[chai])

# since key values are being given we will have to grab one item at a time to iterate in key value pairs
 for key, value in chai_types.items():
  print(key,value)
#   we can ask questions to the keys 
#  adding new key value pairs4
chai_types["earl grey"]="citrius"
print(chai_types)
chai_types.pop("earl grey")
print(chai_types)
# .popitems() pops the last element without pasiinga nything 
# del chai_types["green "] deletes from the memory refrence
# {{},{}} allowed just like in list we give the dictonary inside a dictonary a key by which we canuse it
tea_shop={
 "chai":{"masala":"spicy","ginger":"zesty"},
 "tea":{"green":"fresh"}
}
# how to acces if we print teashop we get full dictonary 
# if we do this we get the whole chai dictonary
print(tea_shop["chai"])
# to even further key value do 
print(tea_shop["chai"]["masala"])
# .clear() claers memomory  