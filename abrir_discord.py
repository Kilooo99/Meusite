"""Abre o Google Chrome, pesquisa por Discord e entra no site do Discord."""

from __future__ import annotations

import shutil
import subprocess
import sys
import time


CHROME_CANDIDATES = (
    "google-chrome",
    "google-chrome-stable",
    "chrome",
    "chromium",
    "chromium-browser",
)


def find_chrome_executable() -> str | None:
    """Retorna o executável do Chrome/Chromium disponível no sistema."""
    for candidate in CHROME_CANDIDATES:
        path = shutil.which(candidate)
        if path:
            return path
    return None


def open_discord_flow(delay_seconds: float = 3.0) -> None:
    """Abre o Chrome com uma pesquisa por Discord e depois abre o site do Discord."""
    chrome_path = find_chrome_executable()
    if not chrome_path:
        raise FileNotFoundError(
            "Não foi possível encontrar o Google Chrome/Chromium instalado no sistema."
        )

    search_url = "https://www.google.com/search?q=discord"
    discord_url = "https://discord.com"

    # Abre o Chrome na pesquisa.
    subprocess.Popen([chrome_path, search_url])

    # Aguarda alguns segundos para simular o fluxo pedido.
    time.sleep(delay_seconds)

    # Abre o Discord em uma nova aba/janela.
    subprocess.Popen([chrome_path, discord_url])


if __name__ == "__main__":
    try:
        open_discord_flow()
        print("Chrome aberto com pesquisa por Discord e acesso ao Discord iniciado.")
    except Exception as exc:
        print(f"Erro ao executar automação: {exc}")
        sys.exit(1)
