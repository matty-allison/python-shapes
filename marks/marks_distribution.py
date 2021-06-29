import numpy as np
import matplotlib.pyplot as plt
the_marks = np.array([12, 99, 65, 85, 42])
names = np.array(["Andy", "Martin", "Zahara", "Vuyo", "Ziyaad"])
plt.bar(names, the_marks, color="Crimson")
plt.xlabel("Students", color="green")
plt.ylabel("Marks(%)", color="green")
plt.title("Python marks for 5 students", color="Crimson")
plt.show()
