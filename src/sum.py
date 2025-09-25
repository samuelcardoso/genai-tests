# src/sum.py
from typing import Iterable, Union

Number = Union[int, float]

def sum_numbers(values: Iterable[Number]) -> float:
    """
    Soma os números de 'values'.
    Regras:
      - Retorna 0.0 para iterável vazio.
      - Aceita apenas int e float (bool NÃO é permitido).
      - Lança TypeError se encontrar tipo não numérico.
    """
    total = 0.0

    # Validação leve e soma
    for v in values:
        # bool é subclass de int em Python — rejeitamos explicitamente
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError("sum_numbers aceita apenas int/float (bool não é permitido).")
        total += float(v)

    return total
