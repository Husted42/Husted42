import sys
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path

import sympy as sp

OUTPUT_DIR = Path(__file__).parent / "outputs"
LOG_DIR = OUTPUT_DIR / "logs"


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


def calculate_gradients(functions, variables, values, loss_name="L"):
    """
    Calculate symbolic and numerical gradients of a loss.

    Parameters
    ----------
    functions : dict
        Dictionary of intermediate functions, evaluated in order.
        Example:
        {
            "h": sp.Max(0, w * x),
            "y": v * h,
            "L": sp.Rational(1, 2) * (y - t)**2
        }

    variables : list
        Variables we want gradients with respect to.
        Example: [w, v]

    values : dict
        Numerical values for the input variables.
        Example:
        {x: 1, t: 6, w: 2, v: 4}

    loss_name : str
        Name of the loss function in `functions`.
    """

    expanded = {}

    # Substitute intermediate functions into later functions
    for name, expression in functions.items():
        expression = expression.subs(expanded)
        symbol = sp.Symbol(name)

        expanded[symbol] = expression

    loss_symbol = sp.Symbol(loss_name)
    loss = expanded[loss_symbol]

    divider = "-" * 60

    print(divider)
    print("Initial variables")
    print(divider)
    for symbol, value in values.items():
        print(f"  {str(symbol):<6} = {value}")

    print()
    print(divider)
    print("Expanded loss")
    print(divider)
    print(f"  {loss_name} = {sp.simplify(loss)}")

    print()
    print(divider)
    print("Forward pass")
    print(divider)
    for name in functions:
        symbol = sp.Symbol(name)

        if symbol in expanded:
            result = sp.N(expanded[symbol].subs(values), 6)
            print(f"  {str(name):<6} = {result}")

    print()
    print(divider)
    print("Numeric result")
    print(divider)
    print(f"  {loss_name} = {sp.N(expanded[loss_symbol].subs(values), 6)}")

    print()
    print(divider)
    print("Gradients")
    print(divider)

    gradients = {}
    gradient_values = {}

    for variable in variables:
        gradient = sp.diff(loss, variable)
        gradient_value = sp.N(gradient.subs(values), 6)

        gradients[variable] = gradient
        gradient_values[variable] = gradient_value

        print(f"  d{loss_name}/d{variable} = {gradient_value}")
        print(f"    symbolic: {gradient}")
    print()

    return {"gradients": gradients, "gradient_values": gradient_values}


def run_config(config):
    """Runs a single settings config and saves its log, prefixed with the config name."""
    name = config["name"]

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"{name}_{timestamp}.log"
KJHGFDSAZ<>ZXCVBNM,.-
    with open(log_path  , "w") as log_file, redirect_stdout(Tee(sys.stdout, log_file)):
        print("=" * 60)
        print(f"Config: {name}")
        print("=" * 60)
        results = calculate_gradients(
            functions=config["functions"],
            variables=config["variables"],
            values=config["values"],
            loss_name=config.get("loss_name", "L"),
        )

    print(f"Log saved to {log_path}")

    return {"name": name, "gradient_values": results["gradient_values"]}


def main():
    x, t, w, v = sp.symbols("x t w v")

    configs = [
        {
            "name": "relu_default",
            "functions": {
                "h": sp.Max(0, w * x),
                "y": v * sp.Symbol("h"),
                "L": sp.Rational(1, 2) * (sp.Symbol("y") - t) ** 2,
            },
            "variables": [w, v],
            "values": {x: 1, t: 6, w: 2, v: 4},
        },
        {
            "name": "relu_large_v",
            "functions": {
                "h": sp.Max(0, w * x),
                "y": v * sp.Symbol("h"),
                "L": sp.Rational(1, 2) * (sp.Symbol("y") - t) ** 2,
            },
            "variables": [w, v],
            "values": {x: 1, t: 6, w: 2, v: 10},
        },
        {
            "name": "sigmoid_activation",
            "functions": {
                "h": 1 / (1 + sp.exp(-w * x)),
                "y": v * sp.Symbol("h"),
                "L": sp.Rational(1, 2) * (sp.Symbol("y") - t) ** 2,
            },
            "variables": [w, v],
            "values": {x: 1, t: 6, w: 2, v: 4},
        },
        {
            "name": "negative_input",
            "functions": {
                "h": sp.Max(0, w * x),
                "y": v * sp.Symbol("h"),
                "L": sp.Rational(1, 2) * (sp.Symbol("y") - t) ** 2,
            },
            "variables": [w, v],
            "values": {x: -1, t: 6, w: 2, v: 4},
        },
    ]

    summary = [run_config(config) for config in configs]

    print("\n" + "=" * 60)
    print("Summary (all configs)")
    print("=" * 60)
    for entry in summary:
        print(f"{entry['name']}:")
        for var, val in entry["gradient_values"].items():
            print(f"    dL/d{var} = {val}")

if __name__ == "__main__":
    main()