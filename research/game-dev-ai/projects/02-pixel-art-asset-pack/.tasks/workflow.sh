#!/bin/bash
# task-manager.sh - Gestor de tareas estilo Jira

TASKS_DIR="$(dirname "$0")"
BOARD="$TASKS_DIR/TASK-BOARD.md"
TASK_NUM=$1
ACTION=$2

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

show_help() {
    echo "🎯 Task Manager - Medieval Pixel Pack"
    echo ""
    echo "Usage: ./workflow.sh [TASK_ID] [ACTION]"
    echo ""
    echo "Actions:"
    echo "  start     - Mover a IN PROGRESS"
    echo "  review    - Mover a IN REVIEW"
    echo "  qa        - Mover a QA TESTING"
    echo "  done      - Mover a DONE"
    echo "  fail      - Mover a TODO (con razón)"
    echo "  status    - Mostrar status de tarea"
    echo "  board     - Mostrar board completo"
    echo "  next      - Mostrar siguiente tarea"
    echo ""
    echo "Examples:"
    echo "  ./workflow.sh T-001 start"
    echo "  ./workflow.sh T-001 review"
    echo "  ./workflow.sh T-001 done"
    echo "  ./workflow.sh T-001 status"
    echo "  ./workflow.sh board"
}

show_board() {
    echo ""
    echo "📋 TASK BOARD - Medieval Pixel Art Collection"
    echo "═══════════════════════════════════════════════"
    echo ""
    
    echo "🔴 TODO:"
    grep -l "Status.*TODO" *.md 2>/dev/null | sed 's/.md//' | while read t; do
        priority=$(grep "Prioridad" $t.md | head -1)
        echo "  $t $priority"
    done
    echo ""
    
    echo "🟡 IN PROGRESS:"
    grep -l "Status.*IN PROGRESS" *.md 2>/dev/null | sed 's/.md//' | while read t; do
        echo "  $t"
    done
    echo ""
    
    echo "🔵 IN REVIEW:"
    grep -l "Status.*IN REVIEW" *.md 2>/dev/null | sed 's/.md//' | while read t; do
        echo "  $t"
    done
    echo ""
    
    echo "🟢 QA TESTING:"
    grep -l "Status.*QA TESTING" *.md 2>/dev/null | sed 's/.md//' | while read t; do
        echo "  $t"
    done
    echo ""
    
    echo "✅ DONE:"
    grep -l "Status.*DONE" *.md 2>/dev/null | sed 's/.md//' | while read t; do
        echo "  $t"
    done
    echo ""
}

show_next() {
    next=$(ls -1 T-*.md 2>/dev/null | grep -v "TASK-BOARD" | while read f; do
        if grep -q "Status.*TODO" "$f"; then
            echo "$f"
            break
        fi
    done | head -1)
    
    if [ -n "$next" ]; then
        echo ""
        echo "📌 NEXT TASK: $next"
        echo ""
        grep "^## Description" -A 5 "$next" | head -6
    else
        echo "🎉 All tasks completed!"
    fi
}

show_status() {
    if [ -f "${TASK_NUM}.md" ]; then
        echo ""
        echo "📄 $TASK_NUM"
        echo "══════════════════════════"
        grep "^| **" "${TASK_NUM}.md" | head -10
        echo ""
        echo "📝 Subtasks:"
        grep "^- \[ \]" "${TASK_NUM}.md" | head -10
    else
        echo -e "${RED}❌ Task not found: $TASK_NUM${NC}"
    fi
}

case $ACTION in
    board)
        show_board
        ;;
    next)
        show_next
        ;;
    status)
        show_status
        ;;
    start|review|qa|done)
        echo "Update manually in task file for now"
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        show_help
        ;;
esac
