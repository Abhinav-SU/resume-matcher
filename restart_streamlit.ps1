Param(
    [switch]$Recreate
)

# Ensure script runs from repository root
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

$venvPath = Join-Path $root ".venv"
$python = Join-Path $venvPath "Scripts\python.exe"
$pip = Join-Path $venvPath "Scripts\pip.exe"

function Invoke-Cmd($command, $arguments) {
    & $command $arguments
}

if (Test-Path $python -and -not $Recreate) {
    Write-Host "Using existing virtual environment at $venvPath"
} else {
    if (Test-Path $venvPath) {
        Write-Host "Removing existing virtual environment because -Recreate was requested"
        Remove-Item $venvPath -Recurse -Force
    }
    Write-Host "Creating virtual environment (.venv)..."
    python -m venv .venv
}

if (-not (Test-Path $pip)) {
    Write-Host "Bootstrapping pip and installing requirements..."
    & $python -m pip install --upgrade pip
    if (Test-Path "requirements.txt") {
        & $python -m pip install -r requirements.txt
    } else {
        Write-Host "No requirements.txt found. Skipping package install."
    }
} else {
    Write-Host "Virtual environment already has pip. Skipping install unless -Recreate is used."
}

# Start Streamlit using the venv python
Write-Host "Starting Streamlit (this will run in a separate process)."
$streamlitArgs = @('-m','streamlit','run','app.py','--server.port','8501','--server.headless','true')
Start-Process -FilePath $python -ArgumentList $streamlitArgs -WorkingDirectory $root
Write-Host "Streamlit launched. Open http://localhost:8501"
