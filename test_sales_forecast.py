import unittest

from sales_forecast import forecast_sales


class SalesForecastTests(unittest.TestCase):
    def test_upward_trend_is_forecast(self):
        result = forecast_sales([100, 110, 120], 1)
        self.assertGreater(result[0], 120)

    def test_short_history_is_rejected(self):
        with self.assertRaises(ValueError):
            forecast_sales([100, 110], 1)


if __name__ == "__main__":
    unittest.main()
