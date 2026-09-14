from gen_traning_data import x_train, x_validation, x_test, y_train, y_validation, y_test

import sys
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import torch
import torch.nn as nn

OUTPUT_DIR = Path(__file__).parent / "outputs"
LOG_DIR = OUTPUT_DIR / "logs"
PLOT_DIR = OUTPUT_DIR / "plots"


class Tee:
    """Writes to multiple streams at once (e.g. console and log file)."""

    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for stream in self.streams:
            stream.write(data)

    def flush(self):
        for stream in self.streams:
            stream.flush()


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(2, 4)
        self.output = nn.Linear(4, 3)

    def forward(self, x):
        x = self.hidden(x)
        x = torch.relu(x)
        x = self.output(x)

        return x


class WideNeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(2, 16)
        self.output = nn.Linear(16, 3)

    def forward(self, x):
        x = self.hidden(x)
        x = torch.relu(x)
        x = self.output(x)

        return x


class DeepNeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(2, 8)
        self.hidden2 = nn.Linear(8, 8)
        self.output = nn.Linear(8, 3)

    def forward(self, x):
        x = torch.relu(self.hidden(x))
        x = torch.relu(self.hidden2(x))
        x = self.output(x)

        return x


class DropoutNeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.hidden = nn.Linear(2, 16)
        self.dropout = nn.Dropout(0.2)
        self.output = nn.Linear(16, 3)

    def forward(self, x):
        x = torch.relu(self.hidden(x))
        x = self.dropout(x)
        x = self.output(x)

        return x


def simple_traning_loop(model, data):
    print(f'########## {model.__class__.__name__} ##########')

    x_train = torch.tensor(data["x_train"], dtype=torch.float32)
    y_train = torch.tensor(data["y_train"], dtype=torch.float32)
    x_validation = torch.tensor(data["x_validation"], dtype=torch.float32)
    y_validation = torch.tensor(data["y_validation"], dtype=torch.float32)
    x_test = torch.tensor(data["x_test"], dtype=torch.float32)
    y_test = torch.tensor(data["y_test"], dtype=torch.float32)

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    print("Inspecting model")
    print(model)

    print(f'Hidden layer weight shape: {model.hidden.weight.shape} bias shape: {model.hidden.bias.shape}')  # torch.Size([4, 2])
    print(f'Output layer weight shape: {model.output.weight.shape} bias shape: {model.output.bias.shape}')  # torch.Size([3, 4])

    print(f'\nStart traning')
    train_losses = []
    val_losses = []
    for epoch in range(1000):
        optimizer.zero_grad()
        outputs = model(x_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            val_outputs = model(x_validation)
            val_loss = criterion(val_outputs, y_validation)
        train_losses.append(loss.item())
        val_losses.append(val_loss.item())

        if (epoch+1) % 100 == 0:
            print([round(x, 2) for x in model.hidden.weight.flatten().tolist()])
            print(f'Epoch [{epoch+1}/1000], Loss: {loss.item():.4f}, Validation Loss: {val_loss.item():.4f}')

    with torch.no_grad():
        test_predictions = model(x_test)
        test_loss = criterion(test_predictions, y_test)

    return {
        "train_losses": train_losses,
        "val_losses": val_losses,
        "y_test": y_test,
        "test_predictions": test_predictions,
        "test_loss": test_loss.item(),
    }


def plot_loss_curve(model_name, train_losses, val_losses, save_path):
    plt.figure()
    plt.plot(train_losses, label="Train loss")
    plt.plot(val_losses, label="Validation loss")
    plt.xlabel("Epoch")
    plt.ylabel("MSE loss")
    plt.title(f"{model_name} - Training vs Validation Loss")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_predictions(model_name, y_test, test_predictions, save_path):
    y_true = y_test.numpy()
    y_pred = test_predictions.numpy()
    n_outputs = y_true.shape[1]

    fig, axes = plt.subplots(1, n_outputs, figsize=(5 * n_outputs, 5))
    if n_outputs == 1:
        axes = [axes]

    for i, ax in enumerate(axes):
        ax.scatter(y_true[:, i], y_pred[:, i], alpha=0.6)
        lims = [min(y_true[:, i].min(), y_pred[:, i].min()), max(y_true[:, i].max(), y_pred[:, i].max())]
        ax.plot(lims, lims, "r--", linewidth=1)
        ax.set_xlabel("Actual")
        ax.set_ylabel("Predicted")
        ax.set_title(f"Output {i}")

    fig.suptitle(f"{model_name} - Predictions vs Actual (Test set)")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def run_model(model, data):
    """Trains a single model and saves its log + plots, prefixed with the model name."""
    model_name = model.__class__.__name__

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    prefix = f"{model_name}_{timestamp}"
    log_path = LOG_DIR / f"{prefix}.log"

    with open(log_path, "w") as log_file, redirect_stdout(Tee(sys.stdout, log_file)):
        results = simple_traning_loop(model, data)

    loss_plot_path = PLOT_DIR / f"{prefix}_loss.png"
    predictions_plot_path = PLOT_DIR / f"{prefix}_predictions.png"
    plot_loss_curve(model_name, results["train_losses"], results["val_losses"], loss_plot_path)
    plot_predictions(model_name, results["y_test"], results["test_predictions"], predictions_plot_path)

    print(f"Log saved to {log_path}")
    print(f"Loss plot saved to {loss_plot_path}")
    print(f"Predictions plot saved to {predictions_plot_path}")

    return {"model_name": model_name, "test_loss": results["test_loss"]}


def main():
    data = {
        "x_train": x_train,
        "y_train": y_train,
        "x_validation": x_validation,
        "y_validation": y_validation,
        "x_test": x_test,
        "y_test": y_test
    }

    models = [
        NeuralNetwork(),
        WideNeuralNetwork(),
        DeepNeuralNetwork(),
        DropoutNeuralNetwork(),
    ]

    summary = [run_model(model, data) for model in models]

    print("\n########## Summary ##########")
    for entry in summary:
        print(f"{entry['model_name']}: Test Loss = {entry['test_loss']:.4f}")

if __name__ == "__main__":
    main()