#tupples

tup1=(3,2,6,5,4,90)

print(tup1)

t1=tuple([1,2,3])
print(t1)
t=(43) #type int
t=(43,) #type tuple

#dictionary

sd={'name':"Ganesh",'age':21}
print(sd)
print(type(sd))

dic1=dict(name="ganesh",age=32)
print(dic1)


sd={'name':"Ganesh",'age':21}
print(sd['name'])
print(sd.keys())
print(sd.values())

sd['country']="india"
print(sd)

mark_det={"english":43,"math":54,"science":89}
sd.update(mark_det)
print(sd)