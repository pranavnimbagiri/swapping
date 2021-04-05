def swapfiledata():
    file1=input("enter the file name to swap")
    file2=input("enter the file name to swap")
    file=open(file1,'r') 
    data_a = a.read()
    file=open(file2,'r') 
    data_b = b.read()
    file=open(file1,'w')
    a.write(data_b)
    file=open(file2,'w')
    b.write(data_a)

swapfiledata()    