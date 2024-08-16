# Load the pipeline
import pickle
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Extract the model from the pipeline
model = pipe.named_steps['step2']  # 'step2' is the name used for the model in your pipeline

# Print the model's name
print("The model used in the pipeline is:", type(model).__name__)
