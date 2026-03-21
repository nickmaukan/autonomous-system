#!/bin/bash
# Autostart del Sistema Autonomo v2.0

echo "🚀 Iniciando Sistema Autonomo v2.0..."

BASE_DIR="$HOME/AutonomousSystem"
cd "$BASE_DIR"

# Cargar config
if [ -f config/system.env ]; then
    export $(cat config/system.env | grep -v '^#' | xargs)
fi

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no encontrado"
    exit 1
fi

# Verificar estado
echo "📊 Estado actual:"
python3 scripts/orchestrator.py

echo ""
echo "🎯 Opciones:"
echo "  1. Ejecutar ciclo único"
echo "  2. Modo continuo (loop)"
echo "  3. Generar boletin inversion"
echo "  4. Salir"

read -p "Selecciona [1-4]: " option

case $option in
    1)
        echo "Ejecutando ciclo único..."
        python3 scripts/orchestrator.py
        ;;
    2)
        echo "Modo continuo - Ctrl+C para salir..."
        while true; do
            python3 scripts/orchestrator.py
            sleep ${CYCLE_INTERVAL:-300}
        done
        ;;
    3)
        echo "Generando boletin..."
        python3 agents/investment_agent.py
        ;;
    4)
        echo "👋 Hasta luego!"
        exit 0
        ;;
    *)
        echo "Opción inválida"
        exit 1
        ;;
esac
