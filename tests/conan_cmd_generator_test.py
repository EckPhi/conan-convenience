#!/usr/bin/python3
from __future__ import annotations

from pathlib import Path

from conan_convenience import config
from conan_convenience.helper.conan_cmd_generator import ConanHelper


class Object:
    pass


def test_get_conan_install_command():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.ide_build = True

    ch = ConanHelper()
    profile = (
        config.project_path / "profiles" / "windows-noos-nucleo_u575-debug.profile"
    )
    assert (
        ch.get_conan_install_command(
            profile,
        )
        == f"conan install . -if clion-build-windows-noos-nucleo_u575-debug -pr {str(profile.name)} -e PROJECT_DIR_IDE_BUILD=1"
    )

    config.ValidatedConfig.ide_build = False
    assert (
        ch.get_conan_install_command(
            profile,
        )
        == f"conan install . -if cmake-build-windows-noos-nucleo_u575-debug -pr {str(profile.name)}"
    )


def test_get_conan_build_command():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.ide_build = True

    ch = ConanHelper()
    profile = (
        config.project_path / "profiles" / "windows-noos-nucleo_u575-debug.profile"
    )
    assert (
        ch.get_conan_build_command(
            profile,
        )
        == f"conan build . -bf clion-build-windows-noos-nucleo_u575-debug"
    )

    config.ValidatedConfig.ide_build = False
    assert (
        ch.get_conan_build_command(
            profile,
        )
        == f"conan build . -bf cmake-build-windows-noos-nucleo_u575-debug"
    )


def test_get_conan_source_command():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.ide_build = True

    ch = ConanHelper()
    profile = (
        config.project_path / "profiles" / "windows-noos-nucleo_u575-debug.profile"
    )
    assert (
        ch.get_conan_source_command(
            profile,
        )
        == f"conan source . -if clion-build-windows-noos-nucleo_u575-debug"
    )

    config.ValidatedConfig.ide_build = False
    assert (
        ch.get_conan_source_command(
            profile,
        )
        == f"conan source . -if cmake-build-windows-noos-nucleo_u575-debug"
    )


def test_get_conan_package_name():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.ide_build = True

    ch = ConanHelper()
    assert ch.get_conan_package_name() == f"project_dir/0.1.0-branch@local/test"


def test_get_conan_package_command():
    config.ValidatedConfig = Object()
    config.branch_name = "test-branch"
    config.project_path = Path(__file__).parent / "test_files" / "project_dir"
    config.project_name = "project_dir"
    config.ValidatedConfig.ide_prefix = "clion"
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.ide_build = True

    ch = ConanHelper()
    profile = (
        config.project_path / "profiles" / "windows-noos-nucleo_u575-debug.profile"
    )
    package_name = "project_dir/0.1.0-branch@local/test"

    assert (
        ch.get_conan_package_command(
            package_name,
            profile,
        )
        == f"conan create . {package_name} -pr {str(profile.name)}"
    )
