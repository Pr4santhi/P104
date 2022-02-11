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
new_data.sort()

if n % 2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]
    print(n)

print("median is :"+str(median))