import time

a= []
n = int(input("enter the size of input"))
#fvar=open(r'/Users/apple/Desktop/inputfile.txt','r')
#fvar=open(r'/Users/apple/Desktop/sortedfile.txt','r')
fvar=open(r'/Users/apple/Desktop/inverslysort.txt','r')
data=fvar.read()
a=data.split(',')
#a=list(a[0:n])
a= list(map(int, a[0:n]))
fvar.close()


def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while(j>=0 and key < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

start_time =time.time()
insertion_sort(a)
runtime = (time.time() - start_time)*1000
print("runtime in ms := ",runtime)
            
