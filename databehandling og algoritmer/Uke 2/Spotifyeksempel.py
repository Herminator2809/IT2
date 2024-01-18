land = input("Hvilket land kommer artisten fra?")
streams = int(input("hvor mange streams har du?"))


if land == "Norge":
    print("$0.44 per sang")
elif land == "Sverige":
    print("$0.34 per sang")
else:
    print("$0.22 per sang")

if streams > 30000000:
    print("Penger tjent per sang lik 70%")
elif streams > 1400000:
    print("Penger tjent per sang lik 40%")
else:
    print("Penger tjent per sang lik 0%")

