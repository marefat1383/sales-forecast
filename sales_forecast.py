import argparse

import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_sales(history: list[float], months: int = 1) -> list[float]:
    if len(history) < 3:
        raise ValueError("At least three historical values are required")
    if months <= 0:
        raise ValueError("Months must be positive")
    if any(value < 0 for value in history):
        raise ValueError("Sales values cannot be negative")
    x = np.arange(1, len(history) + 1).reshape(-1, 1)
    model = LinearRegression().fit(x, history)
    future_x = np.arange(len(history) + 1, len(history) + months + 1).reshape(-1, 1)
    return [round(max(0.0, float(value)), 2) for value in model.predict(future_x)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Forecast future sales from historical values.")
    parser.add_argument("history", help="Comma-separated historical sales")
    parser.add_argument("--months", type=int, default=1)
    args = parser.parse_args()
    history = [float(value) for value in args.history.split(",")]
    for month, value in enumerate(forecast_sales(history, args.months), start=1):
        print(f"Forecast month {month}: {value}")


if __name__ == "__main__":
    main()
