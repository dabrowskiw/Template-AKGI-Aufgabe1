# --- Aufgabe 1: List Comprehensions ---
# Um list comprehensions zu üben, spielen wir ein wenig code-golf: Jede der Aufgaben lässt sich mit einer Zeile
# lösen. Beispielsweise wäre die Lösung, um bei einer übergebenen Liste mit unterschiedlichen Zahlen eine Liste
# nur mit den Zahlen größer x zurückzugeben:
def example_list_comprehension(numbers, x):
    return [value for value in numbers if value > x]


# Geben Sie ein Array zurück, das in jedem Element der Reihe nach einen Buchstaben des Textes enthält. Beispiel:
# text = "test", result = ["t", "e", "s", "t"].
# Lösen Sie diese Aufgabe in einer Zeile unter Verwendung einer list comprehension!
def text_to_array(text):
    return []


# Geben Sie zurück, wie häufig das Zeichen needle im string haystack vorkommt.
# Lösen Sie diese Aufgabe in einer Zeile unter Verwendung einer list comprehension!
# Bitte nicht einfach string.count verwenden!
def count_needle(haystack, needle):
    return []


# Geben Sie eine Liste mit allen ungeraden Zahlen kleiner als maxnumber zurück.
# Lösen Sie diese Aufgabe in einer Zeile unter Verwendung einer list comprehension!
def odd_numbers(maxnumber):
    return []


# Geben Sie eine Liste mit allen Primzahlen kleiner als maxnumber zurück.
# Denken Sie daran, dass Sie list comprehensions verschachteln dürfen!
# Lösen Sie diese Aufgabe in einer Zeile unter Verwendung einer list comprehension!
def primes(maxnumber):
    return []


# --- Aufgabe 2: Generatoren ---

# Schreiben Sie einen Generator, der ungerade Zahlen zurückgibt
def odd_numbers_generator():
    return []


# Schreiben Sie einen Generator, der die Fibonacci-Folge liefert
# Hinweis: Sie können yield überall in der Generator-Funktion verwenden.
def fibonacci_generator():
    return []
