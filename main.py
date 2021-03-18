def intercalate(a,b,c,m,n):
    i=0
    k=0
    ia=0
    ib=0
    flag=0
    
    while flag<=m+n-1:
        if ib>=n and ia>=m:
            break
        elif ib>=n:
            c[k]=a[ia]
            ia+=1
            k+=1
            flag+=1
        elif ia>=m:
            c[k]=b[ib]
            ib+=1
            k+=1
            flag+=1
        elif a[ia]<b[ib]:
            c[k]=a[ia]
            ia+=1
            k+=1
            flag+=1
        elif b[ib]<a[ia]:
            c[k]=b[ib]
            ib+=1
            k+=1
            flag+=1
        else:
            c[k]=b[ib]
            ib+=1
            ia+=1
            k+=1
            flag+=2
            
    print("\n\nVector C orderly: ",end=' ')
    
    for i in range(k):
        print(c[i],end=' ')
    print("\n")
    return k

def ordenate(vector,size):
    for i in range (size-1):
        for j in range (i+1,size):
            if vector[i]>vector[j]:
                aux=vector[j]
                vector[j]=vector[i]
                vector[i]=aux

def main():
    m=int(input("\nEnter the number of elements of vector A : "))
    a=[0]*m

    for i in range(m):
        a[i]=int(input("Enter the element %d of vector A: " %(i+1)))
        
    print("\nVector A not orderly: ",end=' ')
    for i in a:
        print(i,end=' ')
        
    ordenate(a,m)
    print("\nVector A orderly: ",end=' ')
    for i in a:
        print(i,end=' ')
        
    n=int(input("\n\nEnter the number of elements of vector B: "))
    b=[0]*n

    for i in range(n):
        b[i]=int(input("Enter the element %d of vector B: " %(i+1)))
        
    print("\nVector B not orderly: ",end=' ')
    for i in b:
        print(i,end=' ')
        
    ordenate(b,n)
    print("\nVector B orderly: ",end=' ')
    for i in b:
        print(i,end=' ')
        
    c=[0]*(n+m)
    output = intercalate(a,b,c,m,n)
    print(f'Number of elements of Vector C: {output}')

main()
