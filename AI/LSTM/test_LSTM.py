import torch
import torch.nn as nn
import matplotlib.pyplot as plt

############### --------------- INPUT AND SETTINGS --------------- ###############
# Building fake data for testing
T = 5      # sequence length
V = 10     # vocabulary size
C = 3      # number of classes

# Example token indices:
# [2, 4, 1, 7, 3]
token_indices = torch.tensor([2, 4, 1, 7, 3])

# Convert to one-hot encoding
x = torch.nn.functional.one_hot(
    token_indices,
    num_classes=V
).float()

# Shape: [T, V]
print("Input shape:", x.shape)

# Single class target
target = torch.tensor([1])

# Shape: [1]
print("Target shape:", target.shape)

############### --------------- Test framework --------------- ###############
'''
    Simple test function for an LSTM model.
'''
def test_model(model, x, target):
    criterion = nn.CrossEntropyLoss()

    model.name = type(model).__name__

    logits = model(x)

    print("\n--- Test ---")
    print("Output:", logits)
    print("Output shape:", logits.shape)

    assert logits.shape == torch.Size([3]), \
        f"Wrong output shape: expected [3], got {list(logits.shape)}"

    # CrossEntropyLoss normally expects:
    # logits: [N, C]
    # target: [N]
    loss = criterion(
        logits.unsqueeze(0),   # [3] -> [1, 3]
        target                 # [1]
    )

    print("Loss:", loss.item())

    # Plot the output logits instead of exporting an ONNX graph
    plt.bar(range(len(logits)), logits.detach().numpy())
    plt.xlabel("Class")
    plt.ylabel("Logit value")
    plt.title(f"{model.name} Output Logits")
    plt.savefig(f"assets/{model.name}_model_graph.png")



############### --------------- Defining models --------------- ###############
class MyLSTM_1(nn.Module):
    def __init__(self, V):
        super().__init__()
        # Define the LSTM and linear layers with each input being of size V
        self.lstm = nn.LSTM(input_size=V, hidden_size=32)
        self.linear = nn.Linear(32, 3)

    def forward(self, x):
        x, (h_n, c_n) = self.lstm(x)
        # We cannot input x[:-1] beacuse a LSTM takes one datapoint at a time
        # So we start from the newest, removes one timestep from the end iterativly until we have non left
        return self.linear(x[-1])

############### --------------- Run --------------- ###############
model = MyLSTM_1(
    V=V
)

test_model(model, x, target)
