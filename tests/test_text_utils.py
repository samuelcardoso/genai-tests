import pytest
from src.text_utils import normalize_whitespace, split_chunks

# ---------- normalize_whitespace ----------
@pytest.mark.parametrize(
    "raw, expected",
    [
        ("  ola   mundo  ", "ola mundo"),
        ("\tola\t\tmundo\n", "ola mundo"),
        ("linha1\nlinha2\n\nlinha3", "linha1 linha2 linha3"),
        ("", ""),                       # vazio -> vazio
        ("   ", ""),                    # só espaços -> vazio
        ("a   b   c", "a b c"),
    ],
)
def test_normalize_whitespace(raw, expected):
    assert normalize_whitespace(raw) == expected


# ---------- split_chunks ----------
def test_split_chunks_basico():
    text = "um dois tres quatro cinco"
    chunks = split_chunks(text, max_len=9)
    # possíveis saídas válidas (depende do encaixe), mas todas <= 9
    assert all(len(c) <= 9 for c in chunks)
    # recompor e normalizar deve dar o texto normalizado
    assert " ".join(chunks) == "um dois tres quatro cinco"

def test_split_chunks_texto_curto_igual_ou_menor_que_max():
    text = "abc def"
    assert split_chunks(text, max_len=7) == ["abc def"]
    assert split_chunks(text, max_len=8) == ["abc def"]

@pytest.mark.parametrize("max_len", [0, -1, -10])
def test_split_chunks_max_len_invalido(max_len):
    with pytest.raises(ValueError):
        split_chunks("qualquer coisa", max_len)

def test_split_chunks_texto_vazio():
    assert split_chunks("", max_len=5) == []

def test_split_chunks_sem_estourar_limite():
    text = "aaaa bbbb cccc"
    # cada palavra tem 4; com max=9, "aaaa bbbb" cabe (9 chars incluindo espaço)
    chunks = split_chunks(text, max_len=9)
    assert chunks == ["aaaa bbbb", "cccc"]
    assert all(len(c) <= 9 for c in chunks)
