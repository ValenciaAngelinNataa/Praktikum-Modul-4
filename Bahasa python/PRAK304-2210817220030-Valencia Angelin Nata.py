a= int(input())
if  (a==0):
    print("Nol")
elif(a>0 and a<10):
    print("Satuan")
elif(a>10 and a<20):
    print("Belasan")
elif(a==10 or a>19 and a<=99):
    print("Puluhan")
elif(a>99):
    print("Anda Menginput Melebihi Limit Bilangan")