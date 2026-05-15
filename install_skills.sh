#!/bin/bash
# install_skills.sh - 一键安装 AI4Science 工具箱为 Claude Code Skills
#
# 用法:
#   chmod +x install_skills.sh && ./install_skills.sh
#
# 这个脚本将6个模块注册到 Claude Code 的 skills 目录。
# 安装后启动 Claude Code，AI 会自动加载这些技能。

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${HOME}/.claude/skills"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="${SCRIPT_DIR}/install_skills_${TIMESTAMP}.log"

# 颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "========================================"
echo " AI4Science Academic Toolkit - Skills 安装"
echo "========================================"

# 检查 Claude Code 是否安装
if ! command -v claude &> /dev/null; then
    echo -e "${YELLOW}⚠ claude 命令未找到。脚本仍会安装 skills，但要等安装 Claude Code 后才生效。${NC}"
fi

# 创建 skills 目录
mkdir -p "${SKILLS_DIR}"
echo -e "${GREEN}✓ Skills 目录: ${SKILLS_DIR}${NC}"

# 模块映射: 源目录 → skill 名称
declare -A MODULES=(
    ["module_01_nature_writing"]="academic-writing-engine"
    ["module_02_visualization"]="academic-visualization"
    ["module_03_figure_validation"]="academic-validation"
    ["module_04_submission"]="academic-submission"
    ["module_05_citation"]="academic-citation"
    ["module_06_latex_toolchain"]="academic-latex"
)

SUCCESS=0
FAILED=0

for SRC_DIR in "${!MODULES[@]}"; do
    SKILL_NAME="${MODULES[$SRC_DIR]}"
    SRC_PATH="${SCRIPT_DIR}/${SRC_DIR}"
    LINK_PATH="${SKILLS_DIR}/${SKILL_NAME}"

    if [ ! -d "${SRC_PATH}" ]; then
        echo -e "${RED}✗ 源目录不存在: ${SRC_PATH}${NC}"
        FAILED=$((FAILED + 1))
        continue
    fi

    # 如果已存在，备份并覆盖
    if [ -L "${LINK_PATH}" ] || [ -d "${LINK_PATH}" ]; then
        BACKUP="${LINK_PATH}.bak.${TIMESTAMP}"
        mv "${LINK_PATH}" "${BACKUP}"
        echo -e "${YELLOW}  ⚡ 已有旧链接，已备份到 ${BACKUP}${NC}"
    fi

    # 创建符号链接
    if ln -s "${SRC_PATH}" "${LINK_PATH}" 2>/dev/null; then
        echo -e "${GREEN}✓ ${SKILL_NAME} → ${SRC_DIR}${NC}"
        SUCCESS=$((SUCCESS + 1))
    else
        echo -e "${RED}✗ ${SKILL_NAME}: 链接失败${NC}"
        FAILED=$((FAILED + 1))
    fi
done

echo ""
echo "========================================"
echo -e "${GREEN}安装完成: ${SUCCESS}个技能成功, ${FAILED}个失败${NC}"
echo "========================================"
echo ""
echo "下一步:"
echo "  启动 Claude Code，Skills 会自动加载。"
echo "  或手动验证: ls -la ${SKILLS_DIR}/"
echo ""

if [ $FAILED -gt 0 ]; then
    echo -e "${YELLOW}提示: Windows 用户请用 install_skills.ps1${NC}"
fi
