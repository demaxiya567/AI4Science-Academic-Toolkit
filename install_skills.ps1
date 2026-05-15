# install_skills.ps1 - 一键安装 AI4Science 工具箱为 Claude Code Skills (Windows)
#
# 用法:
#   powershell -ExecutionPolicy Bypass -File install_skills.ps1
#
# 安装后启动 Claude Code，AI 会自动加载这些技能。

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$SkillsDir = "$env:USERPROFILE\.claude\skills"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " AI4Science Academic Toolkit - Skills 安装" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# 创建 skills 目录
if (-not (Test-Path $SkillsDir)) {
    New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null
    Write-Host "✓ Skills 目录: $SkillsDir" -ForegroundColor Green
}

# 模块映射
$Modules = @{
    "module_01_nature_writing" = "academic-writing-engine"
    "module_02_visualization" = "academic-visualization"
    "module_03_figure_validation" = "academic-validation"
    "module_04_submission" = "academic-submission"
    "module_05_citation" = "academic-citation"
    "module_06_latex_toolchain" = "academic-latex"
}

$Success = 0
$Failed = 0

foreach ($SrcDir in $Modules.Keys) {
    $SkillName = $Modules[$SrcDir]
    $SrcPath = Join-Path $ScriptDir $SrcDir
    $LinkPath = Join-Path $SkillsDir $SkillName

    if (-not (Test-Path $SrcPath)) {
        Write-Host "✗ 源目录不存在: $SrcPath" -ForegroundColor Red
        $Failed++
        continue
    }

    # 如果已存在，备份
    if (Test-Path $LinkPath) {
        $Backup = "${LinkPath}.bak.${Timestamp}"
        Rename-Item -Path $LinkPath -NewName $Backup
        Write-Host "  ⚡ 已有旧链接，已备份到 $Backup" -ForegroundColor Yellow
    }

    # 创建目录连接 (Windows 上的目录符号链接需要管理员权限)
    try {
        New-Item -ItemType Junction -Path $LinkPath -Target $SrcPath -Force | Out-Null
        Write-Host "✓ $SkillName → $SrcDir" -ForegroundColor Green
        $Success++
    }
    catch {
        # 如果没有管理员权限，Junction 可能失败，尝试创建硬链接
        try {
            cmd /c "mklink /J `"$LinkPath`" `"$SrcPath`"" 2>&1 | Out-Null
            Write-Host "✓ $SkillName → $SrcDir (via mklink)" -ForegroundColor Green
            $Success++
        }
        catch {
            Write-Host "✗ $SkillName: 链接失败" -ForegroundColor Red
            Write-Host "  请以管理员身份运行此脚本" -ForegroundColor Yellow
            $Failed++
        }
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "安装完成: $Success 个技能成功, $Failed 个失败" -ForegroundColor $(
    if ($Failed -gt 0) { "Yellow" } else { "Green" }
)
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`n下一步: 启动 Claude Code，Skills 会自动加载。"
Write-Host "手动验证: dir $SkillsDir"
