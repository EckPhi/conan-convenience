#!/usr/bin/python3
from __future__ import annotations

from pathlib import Path

from conan_convenience import config
from conan_convenience.helper.profile_parsers import ProfileHelper


class Object:
    pass


def test_get_profiles():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    ph = ProfileHelper()
    assert ph.get_profiles() == sorted(
        (config.project_path / "profiles").rglob("*.profile"),
    )


def test_get_profile_params():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True

    ph = ProfileHelper()

    assert ph.get_profile_params(
        config.project_path / "profiles" / "ci.profile",
    ) == {"task": "build", "buildOS": "ci"}
    assert ph.get_profile_params(
        config.project_path / "profiles" / "linux-armv8-release.profile",
    ) == {
        "task": "build",
        "buildOS": "linux",
        "hostOS": "armv8",
        "buildType": "release",
    }
    assert ph.get_profile_params(
        config.project_path / "profiles" / "linux-debug-cpu.profile",
    ) == {
        "task": "build",
        "buildOS": "linux",
        "buildType": "debug",
        "flavour": "cpu",
    }
    assert ph.get_profile_params(
        config.project_path / "profiles" / "windows-noos-debug-board.profile",
    ) == {
        "task": "build",
        "buildOS": "windows",
        "hostOS": "noos",
        "buildType": "debug",
        "flavour": "board",
    }
    assert ph.get_profile_params(
        config.project_path / "profiles" / "windows-unittest.profile",
    ) == {
        "task": "development",
        "buildOS": "windows",
        "hostOS": "unittest",
    }
    assert ph.get_profile_params(
        config.project_path / "profiles" / "windows-noos-nucleo_u575-debug.profile",
    ) == {
        "task": "build",
        "buildOS": "windows",
        "hostOS": "noos",
        "board": "nucleo_u575",
        "buildType": "debug",
    }


def test_get_build_directory():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.ide_build = False

    ph = ProfileHelper()

    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "ci.profile",
        )
        == "cmake-build-ci"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "linux-armv8-release.profile",
        )
        == "cmake-build-linux-armv8-release"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "linux-debug-cpu.profile",
        )
        == "cmake-build-linux-cpu-debug"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "windows-noos-debug-board.profile",
        )
        == "cmake-build-windows-noos-board-debug"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "windows-unittest.profile",
        )
        == "cmake-development-windows-unittest"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "windows-noos-nucleo_u575-debug.profile",
        )
        == "cmake-build-windows-noos-nucleo_u575-debug"
    )

    config.ValidatedConfig.ide_build = True

    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "ci.profile",
        )
        == "clion-build-ci"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "linux-armv8-release.profile",
        )
        == "clion-build-linux-armv8-release"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "linux-debug-cpu.profile",
        )
        == "clion-build-linux-cpu-debug"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "windows-noos-debug-board.profile",
        )
        == "clion-build-windows-noos-board-debug"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "windows-unittest.profile",
        )
        == "clion-development-windows-unittest"
    )
    assert (
        ph.get_build_directory_name(
            config.project_path / "profiles" / "windows-noos-nucleo_u575-debug.profile",
        )
        == "clion-build-windows-noos-nucleo_u575-debug"
    )


if __name__ == "__main__":
    test_get_profiles()
    test_get_profile_params()
    test_get_build_directory()
