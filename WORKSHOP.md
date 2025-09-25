# Oficina “Seu 1º contato com LLMs para testes (Python + pytest)”

## O que você vai aprender (usando LLMs)
1) Transformar requisitos em casos de teste com a LLM (brainstorm estruturado).
2) Gerar código de teste (pytest) com prompts claros e restritos.
3) Usar a LLM como pair reviewer: colar erros do pytest e pedir correções específicas.
4) Controlar a saída: pedir “apenas código”, imports corretos, nomes de teste.
5) Reconhecer limites: a LLM às vezes erra imports/paths; você valida rodando.

**Duração total:** 45–60 min (aula prática)

---

## Repositório base
Use este repo e, durante a oficina, crie um novo arquivo: `tests/test_text_utils_llm.py`.

Pastas e arquivos relevantes:
- src/text_utils.py
- src/__init__.py
- tests/test_text_utils.py
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
    pytest -q   # verifique que tudo está verde antes de começar

---

## Atividade 1 — Brainstorm com a LLM (casos) — 10 min
Objetivo: a LLM ajuda a pensar casos antes de gerar código.

Passos:
- Abra sua LLM favorita.
- Copie o Prompt 1 do arquivo PROMPTS.md (“Liste casos”).
- Escolha 5–7 casos (feliz/borda/erro) para transformar em testes.

---

## Atividade 2 — Gerar testes (pytest) — 15 min
Objetivo: gerar rapidamente um arquivo de testes válido.

Passos:
- Crie um arquivo vazio: `tests/test_text_utils_llm.py`
- Na LLM, use o Prompt 2 (“Gere apenas código de teste”).
- Copie apenas o código retornado para `tests/test_text_utils_llm.py`
- Rode:
      pytest -q

---

## Atividade 3 — Corrigir com ajuda da LLM — 10–15 min
Objetivo: usar a LLM para corrigir testes com base em erros reais.

Passos:
- Se houver falhas/erros, copie a saída completa do pytest.
- Use o Prompt 3 (“Corrigir com base no erro do pytest”) na LLM.
- Substitua o conteúdo de `tests/test_text_utils_llm.py` pelo código corrigido.
- Rode novamente:
      pytest -q
- Meta: tudo verde.

---

## Atividade 4 — 1 caso extra (toque humano) — 5 min
Objetivo: direcionar a LLM a cobrir algo que ela esqueceu.

Passos:
- Use o Prompt 4 (“Adicionar 1 caso extra Unicode”).
- Atualize o arquivo e rode:
      pytest -q

---

## O que observar
- A LLM pensa casos e gera código quando o prompt é claro (imports, nomes, limites).
- Erros são úteis: colar a saída do pytest melhora muito a correção da LLM.
- Você mantém o controle: decide casos, evita duplicações, nomeia bem.

---

## Checklist de entrega
- Criou `tests/test_text_utils_llm.py`
- Possui 3 ou mais testes novos (feliz/borda/erro) gerados pela LLM
- `pytest -q` verde
- Adicionou 1 caso extra (Unicode)

---

## Comandos úteis (resumo)
- Ativar venv:
    - Windows: `.venv\Scripts\activate`
    - macOS/Linux: `source .venv/bin/activate`
- Instalar deps:
      pip install -r requirements.txt
- Rodar testes:
      pytest -q
- Cobertura opcional:
      pytest -q --cov=src --cov-report=term-missing

---

## Dúvidas frequentes
- Cobertura é obrigatória? Não — foco é aprender a guiar a LLM.
- Import deu erro? Rode `pytest` na raiz do repo e confirme que o arquivo está em `tests/`.
- A LLM quebrou o layout? Reforce no prompt: `from src.text_utils import ...`.
