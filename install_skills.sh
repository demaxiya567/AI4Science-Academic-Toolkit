#!/bin/bash
# install_skills.sh - 一键安装 AI4Science 工具箱为 AI Agent Skills
#
# 支持:
#   1. Claude Code (.claude/skills/)
#   2. Codex CLI (.codex/skills/)
#   3. 本地副本 (直接下载到当前目录)
#
# 用法:
#   chmod +x install_skills.sh && ./install_skills.sh
#
# 安装后启动 AI 工具，Skills 会自动加载。

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# 颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# 模块映射
declare -A MODULES=(
    ["module_01_nature_writing"]="academic-writing-engine"
    ["module_02_visualization"]="academic-visualization"
    ["module_03_figure_validation"]="academic-validation"
    ["module_04_submission"]="academic-submission"
    ["module_05_citation"]="academic-citation"
    ["module_06_latex_toolchain"]="academic-latex"
)

install_to_dir() {
    local TARGET_DIR="$1"
    local TOOL_NAME="$2"
    local SUCCESS=0
    local FAILED=0

    echo ""
    echo -e "${CYAN}[${TOOL_NAME}] 安装到: ${TARGET_DIR}${NC}"

    if [ ! -d "${TARGET_DIR}" ]; then
        mkdir -p "${TARGET_DIR}"
        echo -e "  ${YELLOW}创建目录: ${TARGET_DIR}${NC}"
    fi

    for SRC_DIR in "${!MODULES[@]}"; do
        SKILL_NAME="${MODULES[$SRC_DIR]}"
        SRC_PATH="${SCRIPT_DIR}/${SRC_DIR}"
        LINK_PATH="${TARGET_DIR}/${SKILL_NAME}"

        if [ ! -d "${SRC_PATH}" ]; then
            echo -e "  ${RED}✗ ${SKILL_NAME}: 源目录 ${SRC_DIR} 不存在${NC}"
            FAILED=$((FAILED + 1))
            continue
        fi

        # 备份旧链接
        if [ -L "${LINK_PATH}" ] || [ -d "${LINK_PATH}" ]; then
            BACKUP="${LINK_PATH}.bak.${TIMESTAMP}"
            mv "${LINK_PATH}" "${BACKUP}"
            echo -e "  ${YELLOW}⚡ 备份旧链接 → ${BACKUP}${NC}"
        fi

        # macOS/Linux: 符号链接
        if ln -s "${SRC_PATH}" "${LINK_PATH}" 2>/dev/null; then
            echo -e "  ${GREEN}✓ ${SKILL_NAME}${NC}"
            SUCCESS=$((SUCCESS + 1))
        else
            echo -e "  ${RED}✗ ${SKILL_NAME}: 链接失败${NC}"
            FAILED=$((FAILED + 1))
        fi
    done
    echo -e "  ${GREEN}结果: ${SUCCESS}成功, ${FAILED}失败${NC}"
}

# ========== 主流程 ==========
echo "============================================"
echo " AI4Science Academic Toolkit - Skills 安装"
echo "============================================"
echo ""
echo "选择安装方式:"
echo "  1) Claude Code (.claude/skills/)"
echo "  2) Codex CLI (.codex/skills/)"
echo "  3) 全部安装"
echo "  4) 仅本地副本（手动复制到所需位置）"
echo ""
read -p "请输入 [1-4] (默认: 3): " CHOICE
CHOICE=${CHOICE:-3}

case $CHOICE in
    1)
        install_to_dir "${HOME}/.claude/skills" "Claude Code"
        ;;
    2)
        install_to_dir "${HOME}/.codex/skills" "Codex CLI"
        ;;
    3)
        install_to_dir "${HOME}/.claude/skills" "Claude Code"
        install_to_dir "${HOME}/.codex/skills" "Codex CLI"
        ;;
    4)
        DEST="${SCRIPT_DIR}/skills_dist"
        mkdir -p "${DEST}"
        for SRC_DIR in "${!MODULES[@]}"; do
            cp -r "${SCRIPT_DIR}/${SRC_DIR}" "${DEST}/${MODULES[$SRC_DIR]}"
        done
        echo -e "${GREEN}本地副本已创建: ${DEST}${NC}"
        echo "手动复制到 ~/.claude/skills/ 或 ~/.codex/skills/ 即可使用"
        ;;
    *)
        echo -e "${RED}无效选择，退出。${NC}"
        exit 1
        ;;
esac

echo ""
echo "============================================"
echo -e "${GREEN}安装完成！${NC}"
echo "============================================"
echo ""
echo "下一步:"
echo "  Claude Code: 启动 claude，Skills 自动加载"
echo "  Codex CLI:   启动 codex，确保 AGENTS.md 引用了这些技能"
echo "  手动验证:    ls -la ~/.claude/skills/"
echo ""
echo "更详细的 AI 工具配置指南见 README.md → '安装为 AI 可加载的 Skills'"
