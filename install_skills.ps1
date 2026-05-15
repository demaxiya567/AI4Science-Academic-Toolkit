# install_skills.ps1 - 安装 AI4Science 工具箱为 AI Agent Skills (Windows)
#
# 支持:
#   1. Claude Code (.claude/skills/)
#   2. Codex CLI (.codex/skills/)
#   3. 本地副本
#
# 用法:
#   powershell -ExecutionPolicy Bypass -File install_skills.ps1
#
# 安装后启动 AI 工具，Skills 会自动加载。

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

$Modules = @{
    "module_01_nature_writing" = "academic-writing-engine"
    "module_02_visualization" = "academic-visualization"
    "module_03_figure_validation" = "academic-validation"
    "module_04_submission" = "academic-submission"
    "module_05_citation" = "academic-citation"
    "module_06_latex_toolchain" = "academic-latex"
}

function Install-ToDir {
    param($TargetDir, $ToolName)

    Write-Host "`n[$ToolName] 安装到: $TargetDir" -ForegroundColor Cyan

    if (-not (Test-Path $TargetDir)) {
        New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
        Write-Host "  创建目录: $TargetDir" -ForegroundColor Yellow
    }

    $Success = 0
    $Failed = 0

    foreach ($SrcDir in $Modules.Keys) {
        $SkillName = $Modules[$SrcDir]
        $SrcPath = Join-Path $ScriptDir $SrcDir
        $LinkPath = Join-Path $TargetDir $SkillName

        if (-not (Test-Path $SrcPath)) {
            Write-Host "  ✗ $SkillName: 源目录 $SrcDir 不存在" -ForegroundColor Red
            $Failed++
            continue
        }

        if (Test-Path $LinkPath) {
            $Backup = "${LinkPath}.bak.${Timestamp}"
            Rename-Item -Path $LinkPath -NewName $Backup -ErrorAction SilentlyContinue
            Write-Host "  ⚡ 备份旧链接 → $Backup" -ForegroundColor Yellow
        }

        try {
            New-Item -ItemType Junction -Path $LinkPath -Target $SrcPath -Force -ErrorAction Stop | Out-Null
            Write-Host "  ✓ $SkillName" -ForegroundColor Green
            $Success++
        }
        catch {
            try {
                cmd /c "mklink /J `"$LinkPath`" `"$SrcPath`"" 2>&1 | Out-Null
                Write-Host "  ✓ $SkillName" -ForegroundColor Green
                $Success++
            }
            catch {
                Write-Host "  ✗ $SkillName: 链接失败（请以管理员身份运行）" -ForegroundColor Red
                $Failed++
            }
        }
    }
    Write-Host "  结果: $Success 成功, $Failed 失败" -ForegroundColor Green
}

# ========== 主界面 ==========
Write-Host "============================================" -ForegroundColor Cyan
Write-Host " AI4Science Academic Toolkit - Skills 安装" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "选择安装方式:"
Write-Host "  1) Claude Code (.claude\skills\)"
Write-Host "  2) Codex CLI (.codex\skills\)"
Write-Host "  3) 全部安装"
Write-Host "  4) 仅本地副本"
Write-Host ""
$Choice = Read-Host "请输入 [1-4] (默认: 3)"
if ([string]::IsNullOrWhiteSpace($Choice)) { $Choice = "3" }

$UserProfile = $env:USERPROFILE

switch ($Choice) {
    "1" { Install-ToDir "$UserProfile\.claude\skills" "Claude Code" }
    "2" { Install-ToDir "$UserProfile\.codex\skills" "Codex CLI" }
    "3" {
        Install-ToDir "$UserProfile\.claude\skills" "Claude Code"
        Install-ToDir "$UserProfile\.codex\skills" "Codex CLI"
    }
    "4" {
        $Dest = Join-Path $ScriptDir "skills_dist"
        New-Item -ItemType Directory -Path $Dest -Force | Out-Null
        foreach ($SrcDir in $Modules.Keys) {
            $DestPath = Join-Path $Dest $Modules[$SrcDir]
            Copy-Item -Path (Join-Path $ScriptDir $SrcDir) -Destination $DestPath -Recurse -Force
        }
        Write-Host "`n本地副本已创建: $Dest" -ForegroundColor Green
        Write-Host "手动复制到 .claude\skills\ 或 .codex\skills\ 即可使用"
    }
    default { Write-Host "无效选择，退出。" -ForegroundColor Red; exit }
}

Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "安装完成！" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "启动 AI 工具即可自动加载 Skills。"
Write-Host "详细配置见 README.md → '安装为 AI 可加载的 Skills'"
