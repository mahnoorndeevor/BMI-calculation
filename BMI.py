# height_in and weight_lb are available as regular lists
weight_lb = [1,2,3,4,5,6,7,8,9]
height_in = [9,8,7,6,5,4,3,2,1]
# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m=np.array(height_in)*0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg=np.array(weight_lb)*0.453592

# Calculate the BMI: bmi
bmi=np_weight_kg/pow(np_height_m,2)

# Print out bmi
print(bmi)