    lists=list(map(int,input().split()))
    w=[]
    for i in range(len(lists)):
        listsa=list(map(int,input().split()))
        w.append(max(listsa))
    val=w.index(max(w))+1
    print("C"+str(val))
    
