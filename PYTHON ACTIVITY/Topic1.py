rules = {"speeding": 1000, "signal": 1500, "no_helmet": 500}
total = 0
disqualified = False

vehicle = input("Vehicle (car/bike): ").lower()
n = int(input("Number of offences: "))

for i in range(n):
    offence = input("Offence: ").lower()
    repeat = input("Repeat? (yes/no): ").lower()

    if offence not in rules:
        print("Invalid offence; skipped")
        continue

    fine = rules[offence] + (500 if repeat == "yes" else 0)
    total += fine

    if offence == "signal" or total >= 3000:
        disqualified = True

print("Vehicle:", vehicle)
print("Total penalty: Rs.", total)
print("Disqualification:", "YES" if disqualified else "NO")