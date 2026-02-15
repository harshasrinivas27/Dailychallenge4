regno = "24110011613"

D = int(regno[len(regno)-1])
print("Register Digit (D):", D)

n = int(input("Enter how many activity scores: "))

data = [0]*n

for i in range(n):
    data[i] = int(input("Enter score: "))

low = []
medium = []
high = []
critical = []

valid = 0
ignored = 0

for i in range(n):

    value = data[i]

    if value < 0:
        ignored = ignored + 1

    else:
        valid = valid + 1

        if value >= 0 and value <= 30:
            low = low + [value]

        elif value >= 31 and value <= 60:
            medium = medium + [value]

        elif value >= 61 and value <= 100:
            high = high + [value]

        else:
            critical = critical + [value]

print("\nBefore filtering:")
print("Low Risk:", low)
print("Medium Risk:", medium)
print("High Risk:", high)
print("Critical Risk:", critical)

removed = 0

if D % 2 == 0:

    for i in range(len(low)):
        removed = removed + 1
    low = []

else:

    for i in range(len(critical)):
        removed = removed + 1
    critical = []

print("\nAfter filtering:")
print("Low Risk:", low)
print("Medium Risk:", medium)
print("High Risk:", high)
print("Critical Risk:", critical)

print("\nTotal Valid Entries:", valid)
print("Ignored Entries:", ignored)
print("Removed Due to Personalization:", removed)
