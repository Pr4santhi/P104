import csv

#reading the csv file and storing it in a list
with open("height-weight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

#the first line will be taken out
file_data.pop(0)
#creating an empty list
new_data=[]
#sorting data to get the height of people
for i in range (len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

#length of list 
n=len(new_data)
total=0
for x in new_data:
    total+=x

mean=total/n
print("mean is :"+str(mean))    