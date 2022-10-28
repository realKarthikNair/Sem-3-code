def common(l1,l2):
    for i in l1:
        if i in l2:
            print("Common element found!")
            break
l1=[23,45,2,44,33]
l2=[23,7,67,88,66]
common(l1,l2)
    #[print("Common elements!") if i in l2 for i in l1]