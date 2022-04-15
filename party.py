class Party:
    def __init__(self):
        self.people = []


party = Party()

names = input()
while names != "End":

    party.people.append(names)
    names = input()

total = len(party.people)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {total}")

