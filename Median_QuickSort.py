import time

def qsHelper(a,low,high):
   if(low + 10 <= high): 
      if low<high:
          piv = partition(a,low,high)
          qsHelper(a,low,piv-1)
          qsHelper(a,piv+1,high)
   else:
      insertion_sort(a,low,high)


def insertion_sort(a,low,high):
    for i in range(low+1,high+1):
        key = a[i]
        j = i-1
        while(j>=0 and key < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        
     
def quickSort(a):
   qsHelper(a,0,len(a)-1)   



def partition(a,low,high):
   pindex = median(a, low, high, (low + high) // 2)
   a[low], a[pindex] = a[pindex], a[low]
   pivot = a[low]
   
   lptr = low
   rptr = high
   
   flag = False
   while not flag:

       while lptr <= rptr and a[lptr] <= pivot:
           lptr = lptr + 1

       while a[rptr] >= pivot and rptr >= lptr:
           rptr = rptr -1

       if rptr < lptr:
           flag = True
       else:
           a[lptr],a[rptr] =a[rptr],a[lptr]


   temp = pivot
   a[a.index(pivot)] = a[rptr]
   a[rptr] = temp
  


   return rptr

def median(a, low, high, median):
  if a[low] < a[high]:
     
    return high if a[high] < a[median] else median
  else:
    return low if a[low] < a[median] else median


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
start_time =time.time()
a.sort()
quickSort(a)
runtime = (time.time() - start_time)*1000
print("runtime in ms := ",runtime)

   


