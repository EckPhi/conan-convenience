#!/usr/bin/python3
from __future__ import annotations

from pathlib import Path
from pathlib import WindowsPath

from conan_convenience import config
from conan_convenience.helper.downloader.local import Local


class Object:
    pass


def test_local_sha265():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.local = Object()
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.local.path = WindowsPath(
        "C:\\Users\\eph\\Documents\\Projects\\tools\\conan-convenience\\tests",
    )
    config.ValidatedConfig.path = "test_files"
    down = Local()
    assert (
        down.sha256(
            "lorem_ipsum.txt",
        )
        == "6cd4e575f6667648876849e763d2929e862e545b73cf903fe7c23856c4875fe7"
    )
    assert (
        down.sha256(
            "lorem_ipsum_x2.txt",
        )
        == "e7a5730646f91a918a77ee201ccc4246662621aa23ee83846e66bc61cb3b801c"
    )


def test_local_get():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.local = Object()
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.local.path = WindowsPath(
        "C:\\Users\\eph\\Documents\\Projects\\tools\\conan-convenience\\tests",
    )
    config.ValidatedConfig.path = "test_files"
    down = Local()
    assert (
        down.get("lorem_ipsum.txt")
        == open(
            Path(__file__).parent / "test_files" / "lorem_ipsum.txt",
        ).read()
    )


if __name__ == "__main__":
    test_local_sha265()
    test_local_get()
