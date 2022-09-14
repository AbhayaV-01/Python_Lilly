d1={"k1":"v1","k2":"v2","k3":"v3","k4":"v4","k5":"v5","k6":"v6","k7":"v7","k8":"v8","k9":"v9","k10":"v10"}
inp=input("Enter a key \n")
if inp in d1:
    print("\nValue is",d1[inp],"\n")
else:
    print("invalid key")