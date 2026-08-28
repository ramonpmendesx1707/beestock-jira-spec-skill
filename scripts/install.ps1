param(
    [ValidateSet("All", "Codex", "Claude", "DeepSeek", "Hermes")]
    [string[]]$Harness = @("All"),
    [switch]$Copy
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$SkillNames = @("criar-especificacao", "criar", "jira")
$HermesRoot = if ($env:HERMES_HOME) { $env:HERMES_HOME } else { Join-Path $HOME ".hermes" }
$Targets = @{}

if ($Harness -contains "All" -or $Harness -contains "Codex" -or $Harness -contains "DeepSeek") {
    $Targets["Agents"] = Join-Path $HOME ".agents\skills"
}
if ($Harness -contains "All" -or $Harness -contains "Claude") {
    $Targets["Claude"] = Join-Path $HOME ".claude\skills"
}
if ($Harness -contains "All" -or $Harness -contains "Hermes") {
    $Targets["Hermes"] = Join-Path $HermesRoot "skills"
}

foreach ($TargetRoot in $Targets.Values) {
    New-Item -ItemType Directory -Force -Path $TargetRoot | Out-Null
    foreach ($SkillName in $SkillNames) {
        $SourcePath = Join-Path $RepoRoot "skills\$SkillName"
        $TargetPath = Join-Path $TargetRoot $SkillName
        if (Test-Path $TargetPath) {
            throw "Refusing to replace existing path: $TargetPath"
        }
        if ($Copy) {
            Copy-Item -Recurse -Path $SourcePath -Destination $TargetPath
        } else {
            New-Item -ItemType Junction -Path $TargetPath -Target $SourcePath | Out-Null
        }
        Write-Host "installed $SkillName -> $TargetRoot"
    }
}

Write-Host "Installation complete. Use -Copy only when junctions are unavailable; copied skills do not update with git pull."
