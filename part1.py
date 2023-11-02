import numpy as np
from datasets import load_dataset


dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
ages = data["age"]


ages_np = np.array(ages)


average_age = int(round(np.mean(ages_np)))


print("Promedio de edad:", average_age)

