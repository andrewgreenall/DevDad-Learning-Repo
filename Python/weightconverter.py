inputWeight = float(input("Enter the weight: "))
inputKgsOrLbs = input("(K)gs or (L)bs: ").upper()
answer = 0

if inputKgsOrLbs == "K":
    answer = inputWeight / 0.45
else:
    answer = inputWeight * 0.45

print("the weight is: ", answer)
