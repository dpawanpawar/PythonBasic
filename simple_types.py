#simple integer string float
#dir(__builtins__) #to check the function
x= 10
y= "10"
z=10.1
sum1=x + x
sum2=y + y

print(sum1, sum2)
print(type(x),type(y),type(z))

## list types 
#list of students grade
student_grades=[9,8,8.2] #similar to matlab

## range 
mylist=list(range(1,10))
print(mylist)

## Attributes
mysum=sum(student_grades)
length=len(student_grades)
mean=mysum/length
print(mean)

##
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))

## to use different function
username = "Python3"
print(username.lower())

## dictionary types
students_grades={"marry":9.1,"larry":8.8, "sam":7.5}
#keys for dictionary
students_grades["marry"]

## tuple types %faster than list but cannot change
monday_temperature=(1,4,5)
print(monday_temperature)
color_codes=((1,2,3),(4,5,6),(7,8,9))
#dictionary with tuple
day_temperatures = {'morning': (1.1 , 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
monday_temperature[1:4] #upper limit is not icluded in list i.e 4 
# indexing negative index also works

## accesing character and slices in string
new_list=['hello',1,2,3]
new_list[0]
new_list[0][2]