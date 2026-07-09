"""Contract tests for Source.

Source is the path-logic value object shared by every adapter. It composes the
folder layout for a simulation (folder / runs_folder / config_path / run
folders) from a base_folder, and — in __post_init__ — disambiguates the
simulation_name if a folder with that name already exists. These tests pin both
the path composition and the naming behaviour, using tmp_path so nothing touches
the real data/ tree.
"""

# ================================================================
# 0. Section: IMPORTS
# ================================================================
from pathlib import Path

import pytest

from simulator.adapters.source import Source


# ================================================================
# 1. Section: Unit Tests
# ================================================================
@pytest.mark.unit
def test_source_folder_is_base_folder_joined_with_name(tmp_path: Path) -> None:
    source = Source("my_sim", "desc", base_folder=tmp_path)

    assert source.folder == tmp_path / "my_sim"


@pytest.mark.unit
def test_source_runs_folder_is_inside_simulation_folder(tmp_path: Path) -> None:
    source = Source("my_sim", "desc", base_folder=tmp_path)

    assert source.runs_folder == tmp_path / "my_sim" / "runs"


@pytest.mark.unit
def test_source_config_path_is_inside_simulation_folder(tmp_path: Path) -> None:
    source = Source("my_sim", "desc", base_folder=tmp_path)

    assert source.config_path == tmp_path / "my_sim" / "config.yaml"


@pytest.mark.unit
def test_source_get_run_folder_composes_run_directory(tmp_path: Path) -> None:
    source = Source("my_sim", "desc", base_folder=tmp_path)

    assert source.get_run_folder("3") == tmp_path / "my_sim" / "runs" / "run_3"


@pytest.mark.unit
def test_source_keeps_name_when_folder_does_not_exist(tmp_path: Path) -> None:
    source = Source("my_sim", "desc", base_folder=tmp_path)

    assert source.simulation_name == "my_sim"


@pytest.mark.unit
def test_source_disambiguates_name_when_folder_already_exists(tmp_path: Path) -> None:
    # Arrange: an existing folder for "my_sim" containing two entries.
    existing = tmp_path / "my_sim"
    existing.mkdir()
    (existing / "runs").mkdir()
    (existing / "config.yaml").touch()

    # Act
    source = Source("my_sim", "desc", base_folder=tmp_path)

    # Assert: name gets suffixed with the number of entries in the folder.
    assert source.simulation_name == "my_sim_2"
