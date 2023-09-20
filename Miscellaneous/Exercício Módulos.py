import time as t
from turtle import TurtleScreenBase
import matplotlib.pyplot as plt

times = []
turns = []
legend = []
turn = 1
reps = 5

print("Este programa marcará o tempo gasto para digitar a palavra \"batata\". Você terá que digitá-la " + str(reps) + " vezes.")
input("Aperte ENTER para começar!")

while turn <= reps:
    start = t.perf_counter()
    input("Digite a palavra: ")
    end = t.perf_counter()
    time = round(end - start, 2)
    times.append(time)
    turns.append(turn)
    turnstr = str(turn) + "ª vez"
    legend.append(turnstr)
    turn += 1


plt.xticks(turns, legend)
plt.plot(turns, times)
plt.show()