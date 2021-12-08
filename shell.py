import basic
while True:
    text=input("basic >")
    #stdin
    res,error=basic.run('<stdin>',text)
    if error:
        print(error)
    else:
        print(res)
