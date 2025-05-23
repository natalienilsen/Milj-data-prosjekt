import unittest
import os
import pandas as pd
from io import StringIO
from src.databehandling import clean_and_save_data, validate_luftkvalitet_data, check_odd_values

class TestDatabehandling(unittest.TestCase):

    def setUp(self):
        #Laget dummy-data med både gyldige og ugyldige rader
        self.raw_data = pd.DataFrame({
            "AQI": [100, -999, 300, 0, 550],
            "city": ["Oslo", "  paris", "Berlin", None, "Madrid"],
            "category": ["good", "moderate", "poor", "good", "severe"],
            "main_pollutant": ["pm2_5", "no2", "o3", "pm10", "co"]
        })
        self.test_raw_path = "test_raw.csv"
        self.test_clean_path = "test_clean.csv"
        self.raw_data.to_csv(self.test_raw_path, index=False)

    def tearDown(self):
        for f in [self.test_raw_path, self.test_clean_path]:
            if os.path.exists(f):
                os.remove(f)

    def test_raw_file_created(self):
        """Sjekker at testfil ble lagret riktig"""
        self.assertTrue(os.path.exists(self.test_raw_path))
        df = pd.read_csv(self.test_raw_path)
        self.assertEqual(len(df), 5)
        self.assertIn("AQI", df.columns)

    def test_clean_and_save_data(self):
        """Tester at ugyldige AQI og duplikater fjernes"""
        clean_and_save_data(self.test_raw_path, self.test_clean_path)
        self.assertTrue(os.path.exists(self.test_clean_path))

        df_clean = pd.read_csv(self.test_clean_path)
        print(df_clean["aqi"])
        
        # Kolonnenavn skal være normalisert
        self.assertIn("aqi", df_clean.columns)
        self.assertTrue((df_clean["aqi"] > 0).all())
        self.assertTrue((df_clean["aqi"] <= 500).all())
        self.assertNotIn(-999, df_clean["aqi"].values)

        # Sjekk at 'city' er renset og standardisert
        self.assertTrue(df_clean["city"].str[0].str.isupper().all())

    def test_validate_luftkvalitet_data(self):
        """Tester at validate returnerer riktig struktur"""
        clean_and_save_data(self.test_raw_path, self.test_clean_path)
        df_clean = pd.read_csv(self.test_clean_path)
        report = validate_luftkvalitet_data(df_clean)

        self.assertIsInstance(report, dict)
        self.assertIn("missing_values", report)
        self.assertIn("aqi_stats", report)
        self.assertIn("unique_categories", report)

    def test_check_odd_values_output(self):
        """Tester at funksjonen skriver ut informasjon (manuelt visuell sjekk)"""
        # Rediriger output til buffer for å analysere print
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        check_odd_values(self.test_raw_path)

        sys.stdout = sys.__stdout__  # tilbakestill
        output = captured_output.getvalue()
        self.assertIn("Antall NaN-verdier", output)
        self.assertIn("Duplikater", output)

    def test_file_not_found(self):
        """Tester at funksjonen håndterer manglende fil"""
        with self.assertRaises(FileNotFoundError):
            pd.read_csv("fil_som_ikke_finnes.csv")

        # check_odd_values skal ikke kaste feil, men skrive ut
        import sys
        captured = StringIO()
        sys.stdout = captured
        check_odd_values("fil_som_ikke_finnes.csv")
        sys.stdout = sys.__stdout__
        self.assertIn("Filen finnes ikke", captured.getvalue())


if __name__ == "__main__":
    unittest.main()
