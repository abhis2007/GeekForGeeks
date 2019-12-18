    lists.sort()
    p=n-1
    alt=0
    while(len(lists)>1):
        try:
            if(lists.count(lists[-1-alt]-1)>=1):
                lists.remove(lists[-1-alt]-1)
            alt+=1
        except:
            break
    print(sum(lists))
        
