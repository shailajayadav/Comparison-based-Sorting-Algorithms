import time

a= []
n = int(input("enter the size of input"))
#fvar=open(r'/Users/apple/Desktop/inputfile.txt','r')
#fvar=open(r'/Users/apple/Desktop/sortedfile.txt','r')
fvar=open(r'/Users/apple/Desktop/inverslysort.txt','r')
data=fvar.read()
a=data.split(',')
a= list(map(int, a[0:n]))
fvar.close()

start_time =time.time()
def merge_sort(a):
    if(len(a)>1):
        mid = len(a)//2
        lefth = a[:mid]
        righth = a[mid:]
        merge_sort(lefth)
        merge_sort(righth)
        i = j = k = 0
        while( i < len(lefth) and j < (len(righth))):
            if(lefth[i] < righth[j]):
                a[k] = lefth[i]
                i +=1
            else:
                a[k] = righth[j]
                j +=1
            k+=1
        while( i < len(lefth)):
            a[k] = lefth[i]
            i +=1
            k += 1
        while( j< len(righth)):
            a[k] = righth[j]
            j +=1
            k +=1

def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while(j>=0 and key < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key



start_time =time.time()            
merge_sort(a)
runtime = (time.time() - start_time)*1000
print(" runtime in ms =",runtime)     
        
           
    
    
