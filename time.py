hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hdura = int(dura//60)
mdura = int(dura%60)

ohour = hour + hdura
omin = mins + mdura

if omin > 59:
    if ohour > 23:
        print(str(ohour%24+1)+":"+str(omin%60))
    else:
        print(str(ohour+1)+":"+str(omin%60))
else:
    if ohour > 23:
        print(str(ohour%24)+":"+str(omin))
    else:
        print(str(ohour)+":"+str(omin))
