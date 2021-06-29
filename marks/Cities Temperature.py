import numpy as np
import matplotlib.pyplot as plt
the_marks = np.array([140, 200, 120, 157])
names = np.array(["East London", "Cape Town", "Kimberley", "Durban"])
plt.bar(names, the_marks, color="BLue")
plt.xlabel("Cities", color="BLUE")
plt.ylabel("Rainfall(mm)", color="BLUE")
plt.title("Rainfall for the 4 main cites in SA", color="Blue")
plt.show()
