# Oficina “LLMs e testes unitários (Python + pytest)”

## O que você vai aprender (usando LLMs)
1) Transformar requisitos em casos de teste com a LLM.
2) Gerar código de teste (pytest) com prompts claros e restritos.
3) Usar a LLM como pair reviewer: colar erros do pytest e pedir correções específicas.
4) Controlar a saída: pedir “apenas código”, imports corretos, nomes de teste.
5) Reconhecer limites: a LLM pode errar — você valida rodando.

**Duração total:** 30–45 min (aula prática, bem simples)

---

## Repositório base
Durante a oficina, você criará **um novo arquivo**: `tests/test_sum_llm.py`.

Pastas e arquivos relevantes:
- src/sum.py
- src/__init__.py
- tests/test_sum.py
- requirements.txt

---

## Setup (5–10 min)
    git clone https://github.com/samuelcardoso/genai-tests
    cd genai-tests
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # macOS/Linux:
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest -q   # verifique que tudo está verde

---

## Atividade 1 — Brainstorm com a LLM (casos) — 5–8 min
- Abra sua LLM favorita.
- Copie o Prompt 1 de PROMPTS.md (“Liste casos”).
- Escolha 4–6 casos (feliz/borda/erro) para transformar em testes.

## Atividade 2 — Gerar testes (pytest) — 10–12 min
- Crie `tests/test_sum_llm.py` (vazio).
- Use o Prompt 2 (“Gere apenas código de teste”) e cole o código no arquivo.
- Rode:
      pytest -q

## Atividade 3 — Corrigir com a LLM — 8–10 min
- Se houver falhas, copie a saída do pytest.
- Use o Prompt 3 (“Corrigir com base no erro do pytest”).
- Substitua `tests/test_sum_llm.py` pelo código corrigido e rode novamente:
      pytest -q
- Meta: tudo verde.

## Atividade 4 — 1 caso extra — 3–5 min
- Use o Prompt 4 (caso extra com 0.0/negativos).
- Rode:
      pytest -q

---

## Checklist de resultados
- [ ] Criou `tests/test_sum_llm.py`
- [ ] ≥ 3 testes novos (feliz/borda/erro)
- [ ] `pytest -q` verde
- [ ] +1 caso extra

