IsWeekend = True

if IsWeekend:
    print("nie idziesz do pracy")
else:
    print("idziesz do pracy")

print("nie idziesz do pracy" if IsWeekend else "idziesz do pracy")

>>>
nie idziesz do pracy
nie idziesz do pracy
>>>

IsWeekend = False

if IsWeekend:
    print("nie idziesz do pracy")
else:
    print("idziesz do pracy")

print("nie idziesz do pracy" if IsWeekend else "idziesz do pracy")

>>>
idziesz do pracy
idziesz do pracy
>>>
