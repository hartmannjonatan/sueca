#!/bin/bash

# Caminho do programa
PROGRAM_PATH="."

# Nomes das pastas de ambientes virtuais (se forem diferentes para cada execução)
VENV_DIRS=("venv" "venv" "venv" "venv")

for VENV in "${VENV_DIRS[@]}"; do
    echo "Iniciando o programa com o ambiente virtual $VENV..."

    (
        # Mudando para o diretório do programa
        cd "$PROGRAM_PATH" || exit

        # Ativando o ambiente virtual
        source "$PROGRAM_PATH/$VENV/bin/activate"

        # Executando o script principal
        python3 "$PROGRAM_PATH/src/main.py"

        # Desativando o ambiente virtual
        deactivate

        echo "Programa com ambiente virtual $VENV concluído."
    ) &
done

# Aguarda todos os processos em segundo plano terminarem, se necessário.
wait