from project import tdee, cal, percent, carbs, prot, fat
from io import StringIO

def test_tdee(monkeypatch):
    inputs = StringIO('55\n150\n18\nF\n1\n')
    monkeypatch.setattr('sys.stdin', inputs)
    assert tdee() == 2060.55

def test_cal(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2000")
    assert cal(2200) == 2000

def test_carbs(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "55")
    assert carbs(2000) == (275, 55)

def test_prot(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "25")
    assert prot(2000, 55) == (125, 25)

def test_fat(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "20")
    assert fat(2000) == (100, 20)

def test_percent():
    assert percent(55, 30, 30) == False
    assert percent(55, 25, 20) == True