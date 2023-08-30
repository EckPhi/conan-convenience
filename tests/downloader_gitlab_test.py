#!/usr/bin/python3
from __future__ import annotations

import requests

from conan_convenience import config
from conan_convenience.helper.downloader.gitlab import Gitlab


class Object:
    pass


def test_gitlab_sha265():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.gitlab = Object()
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.gitlab.url = "https://gitlab.com"
    config.ValidatedConfig.gitlab.branch = "46396060a57ec84a958377910a8ec8d536caca2f"
    config.ValidatedConfig.gitlab.project = "gitlab-com/gl-infra/common-ci-tasks"
    config.ValidatedConfig.gitlab.token = None
    config.ValidatedConfig.path = ""
    gl = Gitlab()
    assert (
        gl.sha256(".pre-commit-config.yaml")
        == "3171920cf91d84d823fdfb7c7a86be259e32485f2c7d82579fbc70031681a1ab"
    )

    config.ValidatedConfig.path = "templates"
    assert (
        gl.sha256("standard.yml")
        == "e46e6b99b66b7380dccee463981886b7d195da8fa17307962fb5dc8fc57aad31"
    )


def test_gitlab_get():
    config.ValidatedConfig = Object()
    config.ValidatedConfig.gitlab = Object()
    config.ValidatedConfig.quiet = False
    config.ValidatedConfig.verbose = True
    config.ValidatedConfig.gitlab.url = "https://gitlab.com"
    config.ValidatedConfig.gitlab.branch = "46396060a57ec84a958377910a8ec8d536caca2f"
    config.ValidatedConfig.gitlab.project = "gitlab-com/gl-infra/common-ci-tasks"
    config.ValidatedConfig.gitlab.token = None
    config.ValidatedConfig.path = ""
    gl = Gitlab()
    assert (
        gl.get(".pre-commit-config.yaml")
        == requests.get(
            "https://gitlab.com/gitlab-com/gl-infra/common-ci-tasks/-/raw/46396060a57ec84a958377910a8ec8d536caca2f/.pre-commit-config.yaml",
        ).text
    )

    config.ValidatedConfig.path = "templates"
    assert (
        gl.get("standard.yml")
        == requests.get(
            "https://gitlab.com/gitlab-com/gl-infra/common-ci-tasks/-/raw/46396060a57ec84a958377910a8ec8d536caca2f/templates/standard.yml",
        ).text
    )


if __name__ == "__main__":
    test_gitlab_sha265()
    test_gitlab_get()
