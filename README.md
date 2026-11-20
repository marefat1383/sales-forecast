# Sales Forecast

A small educational AI project that forecasts next month's sales from a short historical sequence using linear regression.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python sales_forecast.py "120,135,150,162,180,195" --months 2
```

## Test

```bash
python -m unittest test_sales_forecast.py
```

The example data is synthetic and the model is intended for learning, not business planning.
