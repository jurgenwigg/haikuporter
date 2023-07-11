# haiku-porter

[![Release](https://img.shields.io/github/v/release/haikuports/haiku-porter)](https://img.shields.io/github/v/release/haikuports/haiku-porter)
[![Build status](https://img.shields.io/github/actions/workflow/status/haikuports/haiku-porter/main.yml?branch=main)](https://github.com/haikuports/haiku-porter/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/haikuports/haiku-porter/branch/main/graph/badge.svg)](https://codecov.io/gh/haikuports/haiku-porter)
[![Commit activity](https://img.shields.io/github/commit-activity/m/haikuports/haiku-porter)](https://img.shields.io/github/commit-activity/m/haikuports/haiku-porter)
[![License](https://img.shields.io/github/license/haikuports/haiku-porter)](https://img.shields.io/github/license/haikuports/haiku-porter)

HAIKUPORTER

- **Github repository**: <https://github.com/haikuports/haiku-porter/>
- **Documentation** <https://haikuports.github.io/haiku-porter/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:haikuports/haiku-porter.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with 

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting 
[this page](https://github.com/haikuports/haiku-porter/settings/secrets/actions/new).
- Create a [new release](https://github.com/haikuports/haiku-porter/releases/new) on Github. 
Create a new tag in the form ``*.*.*``.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

The HaikuPorter tool is provided to ease the fetching, patching and building of source code. It can be compared to a slim version of [Gentoo Portage](https://www.gentoo.org/main/en/about.xml). Each port contains the [Haiku](http://haiku-os.org) specific patches to the original source code. It fetches the original source code, applies the Haiku-specific patches, builds the software, and packages it.

Detailed information available on the [wiki](https://github.com/haikuports/haikuports/wiki/).

## Quick start

## Single Machine (Haiku)

A single machine installation is for building individual packages.

### Installation (Haiku)

HaikuPorts installation can be done via the following command sequence:
 - `git clone https://github.com/haikuports/haikuporter.git`
 - `git clone https://github.com/haikuports/haikuports.git --depth=10`
 - `cd haikuporter`
 - `cp haikuports-sample.conf /boot/home/config/settings/haikuports.conf # Copy the config file`
 - `lpe ~/config/settings/haikuports.conf # and edit it`

### Build port
 - `./haikuporter mesa -j4`

### Build port and all outdated dependency ports
 - `./haikuporter mesa --all-dependencies -j4`

## Multi-node cluster (Linux + Haiku)

A multi-node cluster is for mass building large numbers of packages.

### Running buildmaster in a container with docker

 - `docker pull haikuporter/buildmaster`
 - `mkdir ~/buildmaster.x86`
 - `docker run -v ~/buildmaster.x86:/data -it -e ARCH=x86 haikuporter/buildmaster`
 - Provision builders
   - `createbuilder -n test01 -H 127.0.0.1`
   - copy generated public key to builder
   - `builderctl health`
 - exit
 - Copy the packages from a nightly to ports/packages on the buildmaster
 - `docker run -v ~/buildmaster.x86:/data -it -e ARCH=x86 haikuporter/buildmaster`
 - buildmaster everything

buildmaster.x86 will persist between build runs. Feel free to exit, update, or
erase the container without losing your work.

### Manually Deploy buildmaster (Linux)

 - Install requirements
   - `pip install paramiko` or `dnf install python-paramiko`
   - buildtools dependencies: autoconf, flex, bison, texinfo, zlib-devel
   - Haiku host tools dependencies: libstdc++-static, libcurl-devel
 - Bootstrap the buildmaster instance
   - `git clone https://github.com/haikuports/haikuporter.git`
   - `./haikuporter/buildmaster/bin/bootstrap_buildmaster.sh ...`
 - Configure your builders within instance ports tree with createbuilder
   - `cd buildmaster_<arch>/haikuports`
   - example: `../haikuporter/buildmaster/bin/createbuilder -n mybuilder01 -H 127.0.0.1`
 - Validate and provision your builders
   - `../haikuporter/buildmaster/bin/builderctl health`
   - `../haikuporter/buildmaster/bin/builderctl provision`
 - `../haikuporter/buildmaster/bin/buildmaster everything`

### Deploy buildslave (Haiku)

 - Checkout Haikuporter and Haikuports, matching the paths specified in createbuilder on buildmaster side
 - Add the public key from the buildmaster to authorized\_keys
 - useradd sshd ; ssh-keygen -A
 - Enable PermitRootLogin in /system/settings/ssh/sshd\_config and make sure the path to the sftp server is correct
 - install xz\_utils\_x86, lzip\_x86 (required for extracting packages), patch, dos2unix (required for PATCH() function in some packages)

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
