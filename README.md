

# test-pytest-github-actions e jupyter notebook

Realização de testes unitários com pytest e jupyter notebook no CI do github actions.

## Instalação

Para instalar as dependências do projeto, execute:

```bash
pip install -r requirements.txt

```
## Executando os Testes

Para executar os testes, use:

```bash
pytest tests/

```

## Relatório de cobertura de código

Para executar os testes com cobertura de código e visualizar o relatório:

```bash
coverage run -m pytest tests/
coverage report -m
coverage html

```

