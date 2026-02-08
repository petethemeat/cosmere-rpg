from cosmere_rpg import __version__
from cosmere_rpg import main as main_mod


def test_version() -> None:
    assert isinstance(__version__, str) and __version__ != ""


def test_main_hello(capsys) -> None:
    rc = main_mod.main(["hello", "--name", "Tester"])
    captured = capsys.readouterr()
    assert rc == 0
    assert "Hello, Tester!" in captured.out
