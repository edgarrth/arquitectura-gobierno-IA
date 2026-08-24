#!/usr/bin/env python3
"""Generate a browsable Markdown page from every CSV in docs/data-simulada."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "docs" / "data-simulada"
OUTPUT = ROOT / "docs" / "datos-simulados.md"


def escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", "<br>")


def title_from_filename(path: Path) -> str:
    return path.stem.replace("_", " ").title()


def render_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return ["_Archivo vacío._", ""]

    header = rows[0]
    body = rows[1:]
    lines = [
        "| " + " | ".join(escape_cell(v) for v in header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for row in body:
        padded = row + [""] * (len(header) - len(row))
        lines.append("| " + " | ".join(escape_cell(v) for v in padded[: len(header)]) + " |")
    lines.append("")
    return lines


def main() -> None:
    files = sorted(DATA_DIR.glob("*.csv"))
    lines = [
        "# Datos simulados",
        "",
        "> Esta página se genera automáticamente desde los CSV de `docs/data-simulada/` durante el pipeline.",
        "",
        "Los archivos originales también se publican y pueden descargarse desde cada sección.",
        "",
    ]

    for path in files:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))

        lines.extend(
            [
                f"## {title_from_filename(path)}",
                "",
                f"[Descargar `{path.name}`](data-simulada/{path.name})",
                "",
            ]
        )
        lines.extend(render_table(rows))

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
