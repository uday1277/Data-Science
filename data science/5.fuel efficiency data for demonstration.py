import numpy as np

fuel_efficiency = np.array([25, 30, 22, 35, 28])

average_efficiency = np.mean(fuel_efficiency)

model_index_1 = 1 
model_index_2 = 3  

efficiency_1 = fuel_efficiency[model_index_1]
efficiency_2 = fuel_efficiency[model_index_2]

percentage_improvement = ((efficiency_2 - efficiency_1) / efficiency_1) * 100

print("Average Fuel Efficiency:", average_efficiency, "MPG")
print("Percentage Improvement between Model", model_index_1, "and Model", model_index_2, ":", percentage_improvement, "%")
