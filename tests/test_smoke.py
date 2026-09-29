from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_openapi_document_can_be_loaded() -> None:
    with (ROOT / "docs" / "openapi.yaml").open(encoding="utf-8") as stream:
        document = yaml.safe_load(stream)

    assert document["openapi"].startswith("3.")
    assert document["paths"]


def test_participant_files_are_present() -> None:
    expected = (
        ".claude/settings.json",
        ".devcontainer/devcontainer.json",
        "CLAUDE.md",
        "Makefile",
        "tracker/CR-2.md",
        "tracker/README.md",
    )

    missing = [relative for relative in expected if not (ROOT / relative).is_file()]
    assert not missing, f"Trūkst faili: {', '.join(missing)}"
