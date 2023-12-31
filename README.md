# conan-convenience

```yml
# required: list of config files
configuration_files:
  - list
  - of
  - files
# required: possible values: gitlab, http, local
provider: local
# required, if provider is set to gitlab
gitlab:
  # optional: URL to the custom gitlab-server (defaults to "https://gitlab.com")
  url: "https://gitlab.example.com"
  # required: the full project name (including namespace)
  project: user/project
  # optional: branch to use (defaults to "master")
  branch: master
  # required: personal access token (see https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
  token: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# required, if provider is set to http
http:
  # required: URL where the files are hosted
  url: http://example.com
# required, if provider is set to local
local:
  # required: path to the config files
  path: /home/user/documents/configs
# optional: sub-path where the config files can be found on the remote (defaults to an empty string)
path: ""
# optional: list of dependencies, which have to be installed
dependencies: ["black==19.3b0", "isort==4.3.15", "pylint", "flake8"]
# optional: gitignore info text
gitignore_info_text: "# This section is managed by conan-convenience"
# optional: enable git-ignore management (defaults to true)
update_gitignore: true
# optional: automatically install updates to the tool using pip
auto_update: true
# optional: prefix for ide-builds (defaults to "clion")
ide_prefix: clion
# optional: build for ide, this can be overwritten by a command-parameter (defaults to true)
ide_build: true
# optional: set the default state of verbosity (defaults to false)
verbose: false
# optionsal: set the default state of quietness (defaults to false)
quiet: false
```

config example:


```yml
configuration_files:
  - ".clang-format"
  - ".pre-commit-hooks.yaml"
provider: local
local:
  path: "C:\\Users\\eph\\Documents\\Projects\\tools\\arni-central-configfiles"
```

```yml
configuration_files:
  - ".clang-format"
  - ".pre-commit-hooks.yaml"
provider: http
http:
  url: "http://test.url.com"

```

## TODO

- [ ] check/install dependencies
- [ ] implement auto-update feature
