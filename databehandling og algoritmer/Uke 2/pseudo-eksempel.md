
## Penger tjent per sang

Hent inn land fra bruker (input)

Hvis land er lik Norge:
    print $0.44 per sang
Hvis land er lik Sverige:
    print $0.34 per sang
Ellers
    print $0.22 per sang

### Python-kode
```python

land = input("Hvilket land kommer artisten fra?")

if land == "Norge":
    print("$0.44 per sang")
elif land == "Sverige":
    print("$0.34 per sang")
else:
    print("$0.22 per sang")

```
## Andel penger tjent per sang

Hvis antall streams er større enn 30 000 000
    print "Penger tjent per sang lik 70%"
Ellers hvis antall streams er større enn 1 400 000
    print "Penger tjent per sang lik 40%"
Ellers 
    print "Penger tjent per sang lik 0%" 

### Pyton-kode
```python

streams = int(input("hvor mange streams har du?"))

if streams > 30000000:
    print("Penger tjent per sang lik 70%")
elif streams > 1400000:
    print("Penger tjent per sang lik 40%")
else:
    print("Penger tjent per sang lik 0%")

```

## Pseudokode som følger UDIRs standard:

SET land TO READ "Hvilket land er du fra?"
IF land EQUALS TO Norge
    THEN DISPLAY "$0.44 per sang"
IF land EQUALS TO SVerige