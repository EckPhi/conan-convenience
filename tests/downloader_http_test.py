#!/usr/bin/python3
from __future__ import annotations

import requests

from conan_convenience import config
from conan_convenience.helper.downloader.http import Http


class Object:
    pass


def test_http_sha265():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.http = Object()
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.http.url = "https://example-files.online-convert.com"
    config.ValidatedConfig.path = "document/txt"
    down = Http()
    assert (
        down.sha256(
            "example.txt",
        )
        == "cff50b7e86e43a5263c424961007416154b652fef69abc895bcf0b8e409e03eb"
    )

    config.ValidatedConfig.path = "document/xml"
    assert (
        down.sha256(
            "example.xml",
        )
        == "edcc487393c5c07ec6f4369d3562e1d7afa065610db1896409ef66cbac1965f1"
    )

    config.ValidatedConfig.path = ""
    assert (
        down.sha256(
            "LICENSE",
        )
        == "2287218b44c2e7d1d1b3b5694deef570c4cb56a3061f7b0a192867e4b684f897"
    )


def test_http_get():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.http = Object()
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.http.url = "https://example-files.online-convert.com"
    config.ValidatedConfig.path = "document/txt"
    down = Http()
    assert (
        down.get("example.txt")
        == requests.get(
            "https://example-files.online-convert.com/document/txt/example.txt",
        ).text
    )

    config.ValidatedConfig.path = "document/xml"
    assert (
        down.get("example.xml")
        == requests.get(
            "https://example-files.online-convert.com/document/xml/example.xml",
        ).text
    )

    config.ValidatedConfig.path = ""
    assert (
        down.get("LICENSE")
        == requests.get(
            "https://example-files.online-convert.com/LICENSE",
        ).text
    )


if __name__ == "__main__":
    test_http_sha265()
    test_http_get()
