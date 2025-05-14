units=int(input())
if units>0 and units<=100:
    amount=units*1.50
elif units >100 and units<300:
    amount=100*1.5+(units-100)*2.50
elif units>300:
    amount=100*1.5+200*2.50+(units-300)*4.00
    if units>500:
        subcharge=amount*0.15
        total=subcharge+amount
    else:
        print("no extra charge")
if units<500:
    print(amount)
else:
    print(amount)
    print(f"{subcharge:.2f}")
    print(total)
    
