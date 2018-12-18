import time

a= []
n = int(input("enter the size of input"))
#fvar=open(r'/Users/apple/Desktop/inputfile.txt','r')
fvar=open(r'/Users/apple/Desktop/sortedfile.txt','r')
#fvar=open(r'/Users/apple/Desktop/inverslysort.txt','r')
data=fvar.read()
a=data.split(',')
#a=list(a[0:n])
a= list(map(int, a[0:n]))
fvar.close()


def quickSort(a,low,high):
    if(low < high):
        pi = partition(a,low,high)
        quickSort(a,low,pi-1)
        quickSort(a,pi+1,high)
        
def partition(a,low,high):
    i = low-1
    pivot = a[high]
    for j in range(low,high):
        if(a[j] <= pivot):
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[high] = a[high],a[i+1]
    return i+1

start_time =time.time()
quickSort(a,0,len(a)-1)
runtime=(time.time() - start_time)*1000

print("runtime in ms :",runtime)


