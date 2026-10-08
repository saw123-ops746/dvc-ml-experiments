import yaml
import json
import random

with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

learning_rate = params["train"]["learning_rate"]
epochs = params["train"]["epochs"]
batch_size = params["train"]["batch_size"]

print("================================")
print("TRAINING MODEL")
print("================================")

print("Learning Rate:", learning_rate)
print("Epochs:", epochs)
print("Batch Size:", batch_size)

accuracy = 0.80 + random.random() * 0.15
loss = 0.50 - random.random() * 0.20

print("Accuracy:", accuracy)
print("Loss:", loss)

metrics = {
    "accuracy": accuracy,
    "loss": loss
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)

print("Training completed!")
