from typing import List

def normalize_whitespace(s: str) -> str:
    """
    Converte qualquer sequência de espaços/brancos (espaço, tab, quebra de linha)
    em um único espaço e remove espaços nas bordas.
    """
    # split() sem argumentos quebra por qualquer whitespace
    return " ".join(s.split())

def split_chunks(text: str, max_len: int) -> List[str]:
    """
    Divide 'text' em pedaços de até 'max_len' caracteres, preservando palavras.
    - Lança ValueError se max_len <= 0
    - Se text for vazio, retorna []
    - Nenhum chunk excede max_len
    """
    if max_len <= 0:
        raise ValueError("max_len deve ser > 0")

    text = normalize_whitespace(text)
    if not text:
        return []

    out = []
    cur = ""
    for word in text.split(" "):
        if not cur:
            cur = word
        elif len(cur) + 1 + len(word) <= max_len:
            cur += " " + word
        else:
            out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out
