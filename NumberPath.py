import random

def NumberPath():
    state = 1
    while state < 25:
        state = state + random.randint(1,2)
    return state

results=[]

for _ in range(1000):
    final_number = NumberPath() 
    results.append(final_number)

print(results.count(25) / len(results))
