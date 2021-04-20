# Eine Python-spezifische Form von Schleifen ist die list comprehension. Sie
# definiert Operationen, die auf definierte Elemente einer iterable angewendet werden
values = range(0, 20)
even = []
for x in values:
    if x % 2 == 0:
        even += [x]
print(even)
even = [x for x in values]
even = [str(x + 1) for x in values if x % 2 == 0 and x < 12]
print(even)
even = [[y for y in range(0, x)] for x in range(0, 20)]
print(even)

stringdict = dict([(str(x), x) for x in values])
print(stringdict["12"])

# --- Aufgabe 1: List Comprehensions ---


# Funktionsdefinitionen können überall im Code vorkommen (sollten es aber nicht ;) ):
def add(x, y):
    result = x + y
    return result


print(add(3, 7))

# Vorsicht: Funktionen müssen evaluiert worden sein, bevor sie aufgerufen werden (Live-Beispiel)

# Namen in Funktionsdeklaration können auch in Aufruf verwendet werden (named parameters):

print(add(y=10, x=5))


# Default-Parameter sind möglich:
def somefunction(x, y, defaultparam=False):
    result = x - y
    if defaultparam:
        result = abs(result)
    return result


# Was kommt jeweils raus?
print(somefunction(10, 15))
print(somefunction(10, 15, True))


# Besonderheit von Python: Funktionen, die iterierbar sind. yield returnt zwar,
# der Stack der Funktion bleibt aber beim nächsten Aufruf erhalten:

def generatorfunction(maxnum):
    currentnum = 0
    while currentnum < maxnum:
        yield currentnum
        currentnum += 2


# Was wird ausgegeben?
for x in generatorfunction(10):
    print(x)

# Eine Funktion, die mittels yield Werte zurückgibt und somit iterierbar ist,
# wird als Generator bezeichnet.

# Generatoren können schrittweise abgefragt werden:

nums = generatorfunction(1000)
print(next(nums))
print(next(nums))

# Das ist extrem nützlich, um z.B. über Werte einer rekursiv definierten Folge
# zu laufen ohne sie komplett im Speicher zu halten oder sehr große Datensätze
# zu verarbeiten.

# --- Aufgabe 2: Generatoren ---
