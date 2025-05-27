﻿# Ce script PowerShell permet de lancer radXLMAC en mode console dans PowerShell.

# Configurer PowerShell en UTF-8.
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
$PSDefaultParameterValues['*:Encoding'] = 'utf8'
cmd /c chcp 65001 > $null

$python_path = Join-Path -Path $PSScriptRoot -ChildPath "special_python313_portable\python.exe"
$scripts_path = Join-Path -Path $PSScriptRoot -ChildPath "scripts"
$python_ver = & $python_path --version
$pip_ver = & $python_path -m pip --version

Write-Host "==============================================="
Write-Host "    Lancement de radXLMAC en mode console      "
Write-Host "==============================================="
Write-Host "Python utilisé : $python_path"
Write-Host "Script lancé : main.py"
Write-Host "Version de Python : $python_ver"
Write-Host "Version de Pip : $pip_ver"
Write-Host ""
Write-Host "This program was made by Thomas VASSY--ROUSSEAU, intern at TIMCOD OUEST in May 2025. More informations about him at https://github.com/esaip-tvassy-bach2026."
Write-Host "Copyright (C) TIMCOD SAS, 2025-2030. All rights reserved."
Write-Host "Copyright (C) TIMCOD OUEST SAS, 2025-2030. All rights reserved."
Write-Host ""
Write-Host "Veuillez patienter... Procédons d-abord à des vérifications avant de commencer."
Write-Host ""

# Vérification de la présence des fichiers et dossiers nécessaires au bon fonctionnement
if (!(Test-Path $python_path)) {
    Write-Host "ERREUR FATALE : Impossible de trouver où est Python !" -ForegroundColor Red
    Write-Host "Merci de vérifier que tous les dossiers et fichiers téléchargés portent bien le même nom qu-à l-origine et contiennent bien tous les fichiers nécessaires." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Powershell doit s-arrêter ici." -ForegroundColor Red
    Pause
    exit 1
}
if (!(Test-Path $scripts_path)) {
    Write-Host "ERREUR FATALE : Impossible de trouver le cerveau du programme !" -ForegroundColor Red
    Write-Host "Merci de vérifier que tous les dossiers et fichiers téléchargés portent bien le même nom qu-à l-origine et contiennent bien tous les fichiers nécessaires." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Powershell doit s-arrêter ici." -ForegroundColor Red
    Pause
    exit 1
}

# Lancement de radXLMAC
try {
    Push-Location $scripts_path
    & $python_path -m main
    Pop-Location
    $exitCode = $LASTEXITCODE
    if ($exitCode -eq 0) {
        Write-Host ""
        Write-Host "L-application s-est arrêtée. Traitement réalisé avec succès !" -ForegroundColor Green
        Write-Host ""
        Pause
        exit 0
    } else {
        Write-Host ""
        Write-Host "L-application s-est arrêtée avec le code d-erreur suivant : $exitCode." -ForegroundColor Red
        Write-Host "Merci de relancer complètement l-application. Cela peut parfois résoudre le problème." -ForegroundColor Yellow
        Write-Host ""
        Pause
        exit 1
    }
} catch {
    Write-Host ""
    Write-Host "ERREUR FATALE : Erreur inconnue (Unknown Error)." -ForegroundColor Red
    Write-Host "Redémarrer l-application complètement peut parfois résoudre certains problèmes." -ForegroundColor Yellow
    Write-Host ""
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Pause
    exit 1
}