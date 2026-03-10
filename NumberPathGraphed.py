import matplotlib.pyplot as plt

p1 = 1 
p2 = 1/2 

Prob = [p1, p2]

for n in range(3, 26):
    pn = 0.5 * (Prob[n-2] + Prob[n-3]) 
    Prob.append(pn)

print(Prob)

plt.figure(figsize=(8,4))
plt.plot(range(1, 26), Prob, marker='o', label='Probability of reaching 25')

plt.axhline(y=2/3, color='r', linestyle='--', label='Convergence to 2/3')

plt.title("Convergence of Probability to Reach a Given Position")
plt.xlabel("Position on Path")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)

plt.show()
