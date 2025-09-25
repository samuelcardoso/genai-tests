# PROMPTS — LLMs para testes (copiar/colar)

## Prompt 1 — Liste casos (sem código)
Você será minha dupla de QA. Quero somente uma lista curta de casos de teste, sem escrever código ainda.

Funções alvo (Python):
- normalize_whitespace(s: str) -> str: deve compactar qualquer whitespace em um único espaço e aparar nas bordas.
- split_chunks(text: str, max_len: int) -> list[str]: divide o texto em pedaços de até max_len sem quebrar palavras; se max_len <= 0 deve levantar ValueError; texto vazio retorna [].

Liste:
1) 3–5 casos "felizes" por função
2) 3–5 casos de borda por função
3) 2 casos de erro/exception por função (quando fizer sentido)
Use bullets. Nada de código agora.

---

## Prompt 2 — Gere apenas código de teste (pytest)
Gere APENAS código de teste pytest (sem explicações fora do arquivo) para as funções abaixo.

Regras:
- Importar de: `from src.text_utils import normalize_whitespace, split_chunks`
- Incluir os casos selecionados (feliz, borda, erro).
- Usar `@pytest.mark.parametrize` quando fizer sentido.
- Nomes de testes descritivos.
- Não acessar rede/FS/tempo.

Funções alvo (não reescreva, só use nos testes):

    from typing import List

    def normalize_whitespace(s: str) -> str:
        return " ".join(s.split())

    def split_chunks(text: str, max_len: int) -> List[str]:
        if max_len <= 0:
            raise ValueError("max_len deve ser > 0")
        text = " ".join(text.split())
        if not text:
            return []
        out, cur = [], ""
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

---

## Prompt 3 — Corrigir com base no erro do pytest
Esses testes pytest falharam. Quero que você corrija o arquivo de teste.

Saída do pytest:
<<<COLE AQUI A SAÍDA COMPLETA DO PYTEST>>>

Regras:
- Explique em 2 frases o motivo da falha.
- Em seguida, entregue APENAS o arquivo de teste corrigido (código puro).
- Mantenha nomes de testes claros e remova duplicações.

---

## Prompt 4 — Adicione 1 caso extra (Unicode)
Adicione 1 novo teste à suíte existente cobrindo Unicode com acentos e travessão:
`raw = "  olá   mundo —  teste  "`  =>  `expected = "olá mundo — teste"`
