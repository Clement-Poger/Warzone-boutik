import tempfile
from pathlib import Path
from boutik.invoice import save_invoice

def test_la_facture_est_enregistree():
    with tempfile.TemporaryDirectory() as folder:
        path = save_invoice("TOTAL TTC : 12.00 €", folder)
        assert Path(path).exists()
        assert Path(path).name.startswith("facture_")
        assert Path(path).read_text(encoding="utf-8") == "TOTAL TTC : 12.00 €"