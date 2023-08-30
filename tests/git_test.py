#!/usr/bin/python3
from __future__ import annotations

import shutil
from pathlib import Path
from pathlib import WindowsPath

from conan_convenience import config
from conan_convenience.helper.git import GitHelper


class Object:
    pass


def test_get_current_branch():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.gitignore_info_text = (
        "# This section is managed by conan-convenience\n"
    )
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True

    git = GitHelper()
    assert (
        git.get_current_branch(
            Path(__file__).parent / "test_files" / "project_dir",
        )
        == "test-branch"
    )
    assert (
        git.get_current_branch(
            Path(
                __file__,
            ).parent
            / "test_files"
            / "project_dir"
            / "test-dir",
        )
        == "test-branch"
    )


def test_add_to_gitignore_no_section():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.gitignore_info_text = (
        "# This section is managed by conan-convenience\n"
    )
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True

    initial_gitignore = (
        Path(__file__).parent / "test_files" / "project_dir" / "test.gitignore.initial"
    )
    ignore_file = Path(__file__).parent / "test_files" / "project_dir" / ".gitignore"
    modified_gitignore = (
        Path(
            __file__,
        ).parent
        / "test_files"
        / "project_dir"
        / "test.gitignore.modified"
    )

    ignore_file.unlink(missing_ok=True)
    shutil.copy(initial_gitignore, ignore_file)

    git = GitHelper()
    git.gitignore_info_text = "# This section is managed by conan-convenience"
    git.add_to_gitignore(
        Path(__file__).parent / "test_files" / "project_dir" / "test-dir",
        "test_file.txt",
    )
    git.add_to_gitignore(
        Path(__file__).parent / "test_files" / "project_dir",
        "test.txt",
    )
    git.add_to_gitignore(
        Path(__file__).parent / "test_files" / "project_dir",
        "test-file.txt",
    )
    assert ignore_file.read_text() == modified_gitignore.read_text()
    ignore_file.unlink()


def test_add_to_gitignore_present_section():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.gitignore_info_text = (
        "# This section is managed by conan-convenience\n"
    )
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True

    initial_gitignore = (
        Path(__file__).parent
        / "test_files"
        / "project_dir"
        / "test.gitignore.initial.alt"
    )
    ignore_file = Path(__file__).parent / "test_files" / "project_dir" / ".gitignore"
    modified_gitignore = (
        Path(
            __file__,
        ).parent
        / "test_files"
        / "project_dir"
        / "test.gitignore.modified.alt"
    )

    ignore_file.unlink(missing_ok=True)
    shutil.copy(initial_gitignore, ignore_file)

    git = GitHelper()
    git.gitignore_info_text = "# This section is managed by conan-convenience"
    git.add_to_gitignore(
        Path(__file__).parent / "test_files" / "project_dir" / "test-dir",
        "test_file.txt",
    )
    git.add_to_gitignore(
        Path(__file__).parent / "test_files" / "project_dir",
        "test.txt",
    )
    git.add_to_gitignore(
        Path(__file__).parent / "test_files" / "project_dir",
        "test-file.txt",
    )
    assert ignore_file.read_text() == modified_gitignore.read_text()
    ignore_file.unlink()


if __name__ == "__main__":
    test_get_current_branch()
    test_add_to_gitignore_no_section()
    test_add_to_gitignore_present_section()
