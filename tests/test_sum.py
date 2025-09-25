# tests/test_sum.py
import pytest
from src.sum import sum_numbers

def test_sum_basico_inteiros():
    assert sum_numbers([1, 2, 3]) == 6.0

def test_sum_vazio_retorna_zero():
    assert sum_numbers([]) == 0.0

def test_sum_com_floats_e_negativos():
    assert sum_numbers([-2.5, 10, 0.5]) == 8.0

def test_sum_valor_unico():
    assert sum_numbers([42]) == 42.0

def test_sum_grandes_numeros():
    assert sum_numbers([10_000_000, 2_000_000]) == 12_000_000.0

@pytest.mark.parametrize("entrada", [
    [1, "2"],         # string
    [None],           # None
    [True, 1],        # bool não é permitido
    [{"x": 1}],       # dict
])
def test_sum_tipos_invalidos(entrada):
    with pytest.raises(TypeError):
        sum_numbers(entrada)
