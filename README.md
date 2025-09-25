# genai-tests — Oficina simples (Python + pytest + LLMs)

Este repositório acompanha a oficina “Seu 1º contato com LLMs para testes unitários (Python + pytest)”.

## Requisitos
- Python 3.10+ (ou superior)
- (Opcional) pyenv / venv

## Setup rápido
    git clone https://github.com/samuelcardoso/genai-tests
    cd genai-tests
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # macOS/Linux:
    source .venv/bin/activate
    pip install -r requirements.txt

## Rodar a suíte base
    pytest -q

## Cobertura (opcional)
    pytest -q --cov=src --cov-report=term-missing

## Oficina
Siga o passo a passo em **WORKSHOP.md**.  
Os prompts para a LLM estão em **PROMPTS.md**.

## Estrutura
- src/text_utils.py            (código de exemplo)
- tests/test_text_utils.py     (testes base já prontos)
- tests/test_text_utils_llm.py (você cria durante a oficina)
