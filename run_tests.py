"""Lance tous les tests SANS installer pytest : python run_tests.py

(En entreprise on utilise pytest : `python -m pytest`. Ce petit script
fait la même chose en plus simple, si pytest n'est pas installé.)
"""

import importlib
import inspect
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


def main():
    passed, failed = 0, 0
    for path in sorted((ROOT / "tests").glob("test_*.py")):
        module = importlib.import_module(f"tests.{path.stem}")
        for name, func in inspect.getmembers(module, inspect.isfunction):
            if not name.startswith("test_") or func.__module__ != module.__name__:
                continue
            try:
                func()
                passed += 1
                print(f"  OK     {path.stem} > {name}")
            except Exception as error:  # noqa: BLE001 - on veut tout attraper
                failed += 1
                frame = traceback.extract_tb(error.__traceback__)[-1]
                where = f"{Path(frame.filename).name}, ligne {frame.lineno} : {frame.line}"
                print(f"  ÉCHEC  {path.stem} > {name}")
                print(f"         {type(error).__name__} dans {where}")
    print(f"\n{passed} test(s) réussi(s), {failed} échec(s)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
