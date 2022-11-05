bd= int (input())
h= (bd%(86400*30))/86400
j= (bd%86400)/3600
m= (bd%3600)/60
d= (bd%60)
if (h>=1):
    print ("%d hari %02d:%02d:%02d\n"%(h,j,m,d))
else:
    print("%02d:%02d:%02d\n"%(j,m,d))