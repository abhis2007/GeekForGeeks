    n=list(input())
    count=0
    i=0
    while(i<len(n)):
        if(len(n)-i>=3):
            if(n[i]=="g" and n[i+1]=="f" and n[i+2]=="g"):
                i+=2
                count+=1
            else:
                i+=1
        else:
            break
    print(count) if count>0 else print(-1)
            
