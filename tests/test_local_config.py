import py_compile
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_config_defaults_are_safe():
    import kullanici

    assert isinstance(kullanici.nickname, str)
    assert isinstance(kullanici.password, str)
    assert isinstance(kullanici.kisi, int) and kullanici.kisi > 0
    assert isinstance(kullanici.scroll, int) and kullanici.scroll > 0
    assert isinstance(kullanici.hesap, int) and kullanici.hesap > 0


def test_all_python_scripts_compile():
    for name in ["follow.py", "follow_main.py", "search.py", "search_main.py", "kullanici.py"]:
        target = ROOT / name
        assert target.exists(), f"Missing {name}"
        py_compile.compile(str(target), doraise=True)
