def bubblesort(list):
    k=len(list)-1
    for i in range(k,0,-1):
        for j in range (i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

def insertsort(list):
    for i in range(1,len(list)):
        j=i-1
        next=list[i]
        while list[j]>next and (j>=0):
            list[j+1]=list[j]
            j-=1
        list[j+1]=next
    return list
def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        left=list[:mid]
        right=list[mid:]
        mergesort(left)
        mergesort(right)
        a=0
        b=0
        c=0
        while a<len(left)and b<len(right):
            if left[a]<right[b]:
                list[c]=left[a]
                a=a+1
            else:
                list[c]=right[b]
                b=b+1
            c+=1
        while a<len(left):
            list[c]=left[a]
            a=a+1
            c=c+1
        while b<len(right):
            list[c]=right[b]
            b=b+1
            c=c+1
    return list
def shellsort(lst):
    distance = len(lst) // 2
    while distance > 0:
        for i in range(distance, len(lst)):
            temp = lst[i]
            j = i
            while j >=distance and lst[j - distance] > temp:
                lst[j] = lst[j - distance]
                j -= distance
            lst[j] = temp
        distance //= 2
    return lst

def selectsort(list):
    for slot in range(len(list)-1,0,-1):
        maxindex=0
        for locate in range(1,slot+1):
            if list[locate]>list[maxindex]:
                maxindex=locate
        list[slot],list[maxindex]=list[maxindex],list[slot]
    return list
#search
def linersearch(list,item):
    index=0
    found=False
    while index<len(list)and found is False:
        if list[index]==item:
            found=True
            print(found, index)
            return found, index
        index+=1
    print(found)
    return found,-1

def binarysearch(list,item):
    start=0
    last=len(list)-1
    found=False
    while start<=last and found is False:
        midpoint=(start+last)//2
        if item==list[midpoint]:
            found=True
            print(found,midpoint)
            return found,midpoint
        else:
            if item>list[midpoint]:
                start=midpoint+1
            else:
                last=midpoint-1
    print(found)
    return found,-1

def intpoolsearch(list,x):
    idx1=0
    idx2=len(list)-1
    found=False
    while idx1<idx2 and x>=list[idx1] and x<=list[idx2]:

        midpoint=idx1+int(((float(idx2-idx1)/(list[idx2]-list[idx1]))*(x-list[idx1])))
        if list[midpoint]==x:
            found=True
            print(found,midpoint)
            return found,midpoint
    if list[midpoint]<x:
        idx1+=1
    priint(found)
    return found

f=[15,6,54,45,32,77,1,48,99,75,66,79,87]
x=selectsort(f)
found,index=intpoolsearch(x,66)
