#defining the function to find the student with second largest marks
def secondlargest(list):
    max= 0
    largest = 0
    for i in list:
        if i[-1]>=largest:
            largest = i[-1]
    for i in list:
        if i[-1]!=largest:
            if i[-1]>=max:
                max = i[-1]

    newlist=[]
    for i in list:
        if i[-1]==max:
            newlist.append(i[0])
    return sorted(newlist)

#input from the user
n = int(input("Enter the number of students :"))
list=[]
for i in range(n):
    print("For student ", i)
    name = input("Enter the name: ")
    marks = float(input("Enter marks: "))
    list1=[name,marks]
    list.append(list1)

#calling the function
print("The students having second highest marks are: ", secondlargest(list))
