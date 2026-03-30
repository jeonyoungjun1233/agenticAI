param(
    [string]$ProjectRoot = $(Split-Path -Parent $PSScriptRoot)
)

$outputDir = Join-Path $ProjectRoot 'output'
$logDir = Join-Path $ProjectRoot 'logs'
$reportPath = Join-Path $outputDir 'practice5_hook_report.json'
$logPath = Join-Path $logDir 'practice5_hook.log'

$requiredPaths = @(
    $outputDir,
    (Join-Path $outputDir 'summary.md'),
    (Join-Path $outputDir 'practice3_mcp_result.json')
)

$missingPaths = @()
foreach ($path in $requiredPaths) {
    if (-not (Test-Path -LiteralPath $path)) {
        $missingPaths += $path
    }
}

$warnings = @()
if (-not (Test-Path -LiteralPath (Join-Path $ProjectRoot 'code\03_minimal_mcp_test.py'))) {
    $warnings += '정상/오류 입력 테스트 스크립트가 없어 보입니다.'
}
if (-not (Test-Path -LiteralPath (Join-Path $ProjectRoot 'logs\practice3_minimal_mcp.log'))) {
    $warnings += '최소 MCP 서버 테스트 로그가 없습니다.'
}

$success = ($missingPaths.Count -eq 0)
$report = [ordered]@{
    hook_name = 'verify-week3-output'
    checked_at = (Get-Date).ToString('o')
    output_dir = $outputDir
    required_paths = $requiredPaths
    missing_paths = $missingPaths
    warnings = $warnings
    success = $success
    note = '작업 완료 후 output 생성 여부와 핵심 산출물 존재를 검사하는 예시 hook 결과입니다.'
}

$report | ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 $reportPath

$logLines = @(
    "$(Get-Date -Format s) - INFO - hook verify-week3-output 실행",
    "$(Get-Date -Format s) - INFO - output 디렉터리: $outputDir",
    "$(Get-Date -Format s) - INFO - missing_paths=$($missingPaths.Count)",
    "$(Get-Date -Format s) - INFO - warnings=$($warnings.Count)",
    "$(Get-Date -Format s) - INFO - success=$success"
)
$logLines | Set-Content -Encoding UTF8 $logPath

if (-not $success) {
    Write-Error '필수 산출물이 없어서 hook 검증이 실패했습니다.'
    exit 1
}
