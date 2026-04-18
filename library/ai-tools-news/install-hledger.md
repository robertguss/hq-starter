---
tags:
  - library
title: "Install - hledger"
url: "https://hledger.org/install.html"
company: [personal]
topics: []
created: 2026-02-13
source_type: raindrop
raindrop_id: 1601801198
source_domain: "hledger.org"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

plain text accounting, made easy

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Install - hledger

URL Source: https://hledger.org/install.html

Published Time: Sat, 18 Apr 2026 00:05:42 GMT

Markdown Content:
The current hledger release is **1.52**. (There is also a **2.0 preview 1** (version number: 1.99.1) available.) Here are the **[release notes](https://hledger.org/release-notes.html)**.

You can install hledger by any of these methods:

*   Install [official binaries](https://hledger.org/install.html#official-binaries) from Github (quick)
*   Install [packaged binaries](https://hledger.org/install.html#packaged-binaries) (quick; not always up to date)
*   Install binaries you [build from source](https://hledger.org/install.html#build-from-source) (takes longer)

and then, [check your setup](https://hledger.org/install.html#check-your-setup).

## [Official binaries](https://hledger.org/install.html#official-binaries)

Official release binaries for Linux, Mac, and Windows are provided in the hledger github repo. You can click the badge below to install them manually, or copy-paste the install command from [Get hledger installed](https://hledger.org/get-hledger-installed.html), or use a download tool like [eget](https://github.com/zyedidia/eget?tab=readme-ov-file#how-to-get-eget):

[![Image 1: hledger release binaries](https://img.shields.io/badge/hledger_release_binaries-1.52-brightgreen.svg)](https://github.com/simonmichael/hledger/releases/tag/1.52)`eget simonmichael/hledger --all`

## [Packaged binaries](https://hledger.org/install.html#packaged-binaries)

Homebrew (Mac, Linux) 

[![Image 2: Homebrew](https://repology.org/badge/version-for-repo/homebrew/hledger.svg)](https://formulae.brew.sh/formula/hledger)`brew install hledger`

Docker (Linux, Mac, Windows)  ([more](https://hub.docker.com/search?q=hledger&type=image&sort=updated_at&order=desc)) 

[![Image 3: Docker](https://img.shields.io/badge/Docker_image-1.52-brightgreen.svg)](https://hub.docker.com/r/dastapov/hledger)`docker pull dastapov/hledger`

Windows 

[![Image 4: Scoop](https://repology.org/badge/version-for-repo/scoop/hledger.svg)](https://scoop.sh/#/apps?q=hledger)`scoop install hledger`

[![Image 5: Winget](https://img.shields.io/badge/Winget_package-1.52-brightgreen.svg)](https://github.com/microsoft/winget-pkgs/tree/master/manifests/s/simonmichael/hledger)`winget install -e --id simonmichael.hledger`

[![Image 6: Chocolatey](https://repology.org/badge/version-for-repo/chocolatey/hledger.svg)](https://community.chocolatey.org/packages/hledger)`choco install hledger -y`

BSD 

[![Image 7: freebsd ports](https://repology.org/badge/version-for-repo/freebsd/hledger.svg)](https://www.freshports.org/search.php?query=hledger)`pkg install hs-hledger hs-hledger-ui hs-hledger-web`

![Image 8: openbsd ports](https://repology.org/badge/version-for-repo/openbsd/hledger.svg)`pkg_add hledger`

Nix (Linux, Mac)  ([Troubleshooting](https://hledger.org/hledger.html#troubleshooting), [#1030](https://github.com/simonmichael/hledger/issues/1030), [#1033](https://github.com/simonmichael/hledger/issues/1033), [#2089](https://github.com/simonmichael/hledger/issues/2089)) 

[![Image 9: Nix](https://repology.org/badge/version-for-repo/nix_unstable/hledger.svg)](https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&type=packages&query=hledger)`nix-shell -p hledger hledger-ui hledger-web`

GNU/Linux

Alpine 

[![Image 10: Alpine edge](https://repology.org/badge/version-for-repo/alpine_edge/hledger.svg)](https://pkgs.alpinelinux.org/packages?name=hledger*&branch=edge)`doas apk add hledger hledger-ui hledger-web`

[![Image 11: Alpine 3.21](https://repology.org/badge/version-for-repo/alpine_3_21/hledger.svg)](https://pkgs.alpinelinux.org/packages?name=hledger*&branch=v3.21)

[![Image 12: Alpine 3.20](https://repology.org/badge/version-for-repo/alpine_3_20/hledger.svg)](https://pkgs.alpinelinux.org/packages?name=hledger*&branch=v3.20)

[![Image 13: Alpine 3.19](https://repology.org/badge/version-for-repo/alpine_3_19/hledger.svg)](https://pkgs.alpinelinux.org/packages?name=hledger*&branch=v3.19)

Arch 

[![Image 14: Arch](https://repology.org/badge/version-for-repo/arch/hledger.svg)](https://archlinux.org/packages/extra/x86_64/hledger/)`pacman -Sy hledger hledger-ui hledger-web`

Debian  ([more](https://packages.debian.org/search?searchon=names&keywords=hledger)): 

[![Image 15: Debian unstable](https://repology.org/badge/version-for-repo/debian_unstable/hledger.svg)](https://packages.debian.org/unstable/hledger)`apt install hledger hledger-ui hledger-web`

[![Image 16: Debian testing](https://img.shields.io/badge/Debian_testing_package-1.32.3-red.svg)](https://packages.debian.org/testing/hledger)

[![Image 17: Debian stable](https://img.shields.io/badge/Debian_stable_package-1.25-red.svg)](https://packages.debian.org/stable/hledger)

[![Image 18: Debian oldstable](https://img.shields.io/badge/Debian_oldstable_package-1.18.1-red.svg)](https://packages.debian.org/oldstable/hledger)

Fedora ([more](https://src.fedoraproject.org/rpms/hledger)) 

![Image 19: Fedora_44](https://img.shields.io/badge/Fedora_44_package-1.43.2-red.svg)`dnf install hledger`

![Image 20: Fedora_44](https://img.shields.io/badge/Fedora_44_package-1.43.2-red.svg)

![Image 21: Fedora_43](https://img.shields.io/badge/Fedora_43_package-1.40-red.svg)

![Image 22: Fedora_42](https://img.shields.io/badge/Fedora_42_package-1.32.3-red.svg)

Gentoo 

[![Image 23: Gentoo](https://img.shields.io/badge/Gentoo_package-1.50.2-red.svg)](https://gentoo.zugaina.org/Search?search=hledger)`eselect repository enable haskell && emerge hledger hledger-ui hledger-web`

Raspberry Pi (unaudited) 

![Image 24: Raspberry Pi release binaries](https://img.shields.io/badge/Raspberry_Pi_release_binaries-1.22.2-red.svg)[hledger-linux-arm32v7.zip](https://github.com/simonmichael/hledger/releases/tag/1.22.1)

![Image 25: Raspberry Pi contributed binaries](https://img.shields.io/badge/Raspberry_Pi_contributed_binaries-1.18.1-red.svg)[hledger-aarch64-manjaro.gz](https://github.com/simonmichael/hledger/releases/tag/1.18.1) , [hledger-armhf32-debian.gz](https://github.com/simonmichael/hledger/releases/tag/1.18)

Ubuntu ([more](https://packages.ubuntu.com/search?suite=all&searchon=names&keywords=hledger)) 

[![Image 26: ubuntu_25_10](https://repology.org/badge/version-for-repo/ubuntu_25_10/hledger.svg)](https://packages.ubuntu.com/questing/hledger)`apt install hledger hledger-ui hledger-web`

[![Image 27: ubuntu_25_04](https://repology.org/badge/version-for-repo/ubuntu_25_04/hledger.svg)](https://packages.ubuntu.com/plucky/hledger)

[![Image 28: ubuntu_24_04](https://repology.org/badge/version-for-repo/ubuntu_24_04/hledger.svg)](https://packages.ubuntu.com/noble/hledger)

[![Image 29: ubuntu_22_04](https://repology.org/badge/version-for-repo/ubuntu_22_04/hledger.svg)](https://packages.ubuntu.com/jammy/hledger)

Void 

[![Image 30: Void Linux x86_64](https://repology.org/badge/version-for-repo/void_x86_64/hledger.svg)](https://voidlinux.org/packages/?q=hledger)`xbps-install -S hledger hledger-ui hledger-web`

Sandstorm (web) 

[![Image 31: Sandstorm](https://img.shields.io/badge/Sandstorm_app-1.31-red.svg)](https://apps.sandstorm.io/search?term=hledger)[HLedger Web sandstorm app](https://apps.sandstorm.io/app/8x12h6p0x0nrzk73hfq6zh2jxtgyzzcty7qsatkg7jfg2mzw5n90)

## [Build from source](https://hledger.org/install.html#build-from-source)

Building hledger requires the GHC compiler and either the stack or cabal build tool which you can install with your package manager (brew, apt, winget..), with [ghcup](https://haskell.org/ghcup), or with [stack](https://docs.haskellstack.org/en/stable/) (simplest). Or, you can use docker. All this may need perhaps 4G of RAM and 4G or more of disk space.

### [On Mac](https://hledger.org/install.html#on-mac)

You will need the XCode Command Line Tools. Homebrew or macports will probably also be helpful.

Old issues:

*   [mac m1: building with ghc 9+ requires extra include dir](https://gitlab.haskell.org/ghc/ghc/-/issues/20592)

### [On Unix/Linux](https://hledger.org/install.html#on-unixlinux)

You will need

1.   The header files for certain C libraries, which stack/cabal can’t install for you; otherwise you’ll see build errors like “cannot find -ltinfo”. The exact package names will be specific to your system, but here are some likely install commands:

    *   Debian-based systems: `apt install libgmp-dev libncurses-dev zlib1g-dev`
    *   Older Debian systems: `apt install libgmp3-dev libncurses5-dev zlib1g-dev`
    *   Redhat-based systems: `dnf install gmp-devel ncurses-devel zlib-devel`
    *   Arch: `pacman -S gmp ncurses zlib`
    *   Alpine: `apk add gmp-dev ncurses-dev zlib-dev`
    *   openSUSE: `zypper install gmp-devel ncurses-devel zlib-devel`
    *   FreeBSD: `pkg install gmp ncurses`

2.   A configured system locale that specifies a text encoding; otherwise you’ll see text decoding errors when processing non-ascii characters. For example, on most unix systems `echo $LANG` should show something like `en_US.UTF-8` or `zh_CN.GB2312` or `C.UTF-8` - it should not be just `C`, or unset. This is discussed more in [Text encoding](https://hledger.org/install.html#text-encoding), below.

Get the [hledger source code](https://github.com/simonmichael/hledger/commits/main) with [git](https://git-scm.com/):

```
git clone https://github.com/simonmichael/hledger
cd hledger
git checkout 1.52   # switch to the latest release tag (optional)
```

Then build and install with stack:

```
stack update; stack install
```

or with cabal:

```
cabal update; cabal install all:exes
```

or with docker:

```
cd docker; ./build.sh   # or build-dev.sh to keep build artifacts
```

Old issues:

*   [arch: haskell build advice from Arch wiki](https://wiki.archlinux.org/index.php/Haskell)
*   [openbsd 6: exec: permission denied](https://deftly.net/posts/2017-10-12-using-cabal-on-openbsd.html)
*   [openbsd: stack install tips](https://github.com/commercialhaskell/stack/issues/3313#issuecomment-570353913)

### [On Windows](https://hledger.org/install.html#on-windows)

These notes are for Windows 11. On Windows, stack is the easiest way to get the haskell tools. (Though if you are on a Windows ARM machine, stack will install slow x86_64 versions of the tools, and build slow x86_64 hledger binaries.)

First, apply all windows updates (to get the latest TLS certificates for network requests).

Install [stack](https://docs.haskellstack.org/en/stable/) - in a command or powershell window, run:

```
winget install -e --id commercialhaskell.stack
```

Install [git](https://en.wikipedia.org/wiki/Git):

```
winget install -e --id Git.Git
```

Get the hledger source:

```
git clone https://github.com/simonmichael/hledger
cd hledger
git checkout 1.52   # switch to the latest release tag (optional)
```

Build and install hledger:

```
stack update
stack install
```

On Windows, this may die repeatedly with a “… permission denied (Access is denied.)” error; we [don’t know why](https://github.com/commercialhaskell/stack/issues/2426). Just run it again to continue (press up arrow, enter).

On Windows, things work best if you build in the environment where you will use hledger. Eg don’t build it in a WSL or MINGW window if you plan to use it in CMD or Powershell.

Old issues:

*   [windows: cross-environment non-ascii display issues](https://github.com/simonmichael/hledger/issues/961#issuecomment-471229644)

### [On Nix](https://hledger.org/install.html#on-nix)

Old issues:

*   [nix: nix install on linux can fail with “cloning builder process: Operation not permitted”](https://github.com/simonmichael/hledger/issues/1030)
*   [nix: on Linux, nix-installed hledger won’t handle non-ascii data](https://github.com/simonmichael/hledger/issues/1033)

### [On Android](https://hledger.org/install.html#on-android)

Here’s [how to build hledger on Android with Termux](https://libera.ems.host/_matrix/media/r0/download/libera.chat/51835530d2b9eed094096d8a2c79e03dda2c35fb), if your phone has plenty of memory.

### [Build tips](https://hledger.org/install.html#build-tips)

*   Building the hledger tools and possibly all their dependencies could take anywhere from a minute to an hour.
*   On machines with less than 4G of RAM, the build may use swap space and take much longer (overnight), or die part-way through. In such low memory situations, try adding `-j1` to the stack/cabal install command, and retry a few times, or [ask](https://hledger.org/support.html) for more tips.
*   You could build just the hledger CLI to use less time and space: instead of `stack install`, run `stack install hledger`
*   It’s ok to kill a build and rerun the command later; you won’t lose progress.
*   You can add `--dry-run` to the install command to see how much building remains.

## [Check your setup](https://hledger.org/install.html#check-your-setup)

With modern hledger versions, you should now run:

```
hledger setup
```

to check your installation. If this doesn’t work, read on..

### [PATH](https://hledger.org/install.html#path)

After installing, try to run the hledger tools (hledger, hledger-ui, hledger-web) and look for the expected versions. Eg:

```
$ hledger --version
hledger 1.52-...-20260320, mac-aarch64
```

If this doesn’t work, you may need to add the binaries’ install directory to your shell’s PATH.

stack or cabal show the install directory in their output, and warn you if it is not in PATH. It could be, eg:

*   `~/.local/bin` or `C:\Users\USER\AppData\Roaming\local\bin\` (stack)
*   `~/.cabal/bin` or `C:\Users\USER\AppData\Roaming\cabal\bin\` (cabal)

On unix, these commands will add both bin directories to PATH permanently (probably):

```
echo "export PATH=~/.local/bin:~/.cabal/bin:$PATH" >> ~/.profile
source ~/.profile
```

On Windows, here’s [how to set environment variables](https://www.devdungeon.com/content/set-environment-variables-windows).

### [Text encoding](https://hledger.org/install.html#text-encoding)

Data files containing non-ascii characters are saved with a text encoding - UTF-8, Latin-1, CP-437, or something else. hledger uses the system’s text encoding when reading data, and it expects data to use the same encoding. So if no system encoding is configured, or if the data uses a different encoding, hledger will give an error when reading it.

TLDR: run `hledger setup` to check this, and ensure your data files use the encoding it recommends.

Here’s more detail:

How likely is this to affect you ? It depends on your platform and the data you are working with:

*   On Mac, the system encoding is always UTF-8. You may see this problem if you are working with files received from another system, eg from a Windows system.

*   On Windows, the system encoding varies by region. You probably won’t see this problem if you are working with your own data (perhaps depending how you create the data - see [Start a journal](https://hledger.org/start-a-journal.html)). If you are on Windows 11 and often need to share files with mac/unix systems, there is a setting for UTF-8 encoding which you might want to use (see below).

*   On GNU/Linux and other unix systems, the system encoding varies, and sometimes is not configured at all. It may be controlled by the `LANG` environment variable, or in other ways. You should ensure that at least some encoding is configured. UTF-8 is usually a good choice.

If you hit this problem, you can solve it by

*   converting the data files to your system’s text encoding. Use `iconv` on unix/mac, powershell or notepad on Windows.
*   configuring your system encoding to match your data files.
*   or (for CSV/SSV/TSV files only), use the [`encoding`](https://hledger.org/hledger.html#encoding) CSV rule.

Here’s an example. Let’s say you want to work with UTF-8 text on a GNU/Linux system, but it’s configured with the C locale, which can only handle ASCII text:

```
$ echo $LANG
C
```

So, first check that you have a UTF-8-capable locale installed (`locale -a`). If not, install one (perhaps by using your package manager, perhaps by uncommenting it in `/etc/locale.gen` and running `locale-gen`).

Then change the system locale. Here’s one common way to set it permanently for your shell. Note exact punctuation and capitalisation of locale names is important on some systems.

```
$ echo "export LANG=C.utf8" >>~/.profile    # or en_US.UTF-8, fr_FR.utf8, etc.
# close the shell/terminal window and open a new one
$ echo $LANG
C.UTF-8
```

For Nix users, the procedure is [different](https://github.com/simonmichael/hledger/issues/1033#issuecomment-1062506027), eg you might need to set `LOCALE_ARCHIVE` instead. Likewise for GUIX users.

Windows users who want to use UTF-8 encoding, eg to interoperate with unix systems, might find the “Use Unicode UTF-8 for worldwide language support” setting helpful. Here’s where it is in Windows 11: ![Image 32: windows 11 UTF-8 setting](https://hledger.org/images/win11-utf8-setting.png) Though it might cause problems with some older applications, including some GUI programs.

Here’s a way to select UTF-8 for Windows Terminal and PowerShell, without affecting the entire system: add this line to the PowerShell profile file:

```
$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding
```

### [Completions](https://hledger.org/install.html#completions)

If you use the bash or zsh shells, you can set up context-sensitive auto-completions for hledger command lines. (Here’s how to [contribute other shells](https://github.com/simonmichael/hledger/tree/main/hledger/shell-completion#completions-for-other-shells).)

#### [bash](https://hledger.org/install.html#bash)

1.   Ensure that [bash-completion](https://salsa.debian.org/debian/bash-completion) is installed and enabled:

On a Mac, using homebrew:

    *   `brew remove -f bash-completion`
    *   `brew install bash-completion@2`
    *   Add the suggested line to your ~/.bash_profile, if it’s not already there
    *   `source ~/.bash_profile` (or open a new bash shell)

On GNU/Linux:

    *   `apt install bash-completion`
    *   `source ~/.bash_profile` (or open a new bash shell)

2.   Install hledger with your system package manager (`brew install hledger`, `apt install hledger` or similar).

Now completions may be working.

If not, eg because your system’s hledger package does not yet include the bash completions, or if they are not up to date, or if you have installed hledger by other means, then install the [latest hledger bash completions](https://raw.githubusercontent.com/simonmichael/hledger/1.50-branch/hledger/shell-completion/hledger-completion.bash) yourself, under your XDG_DATA_HOME directory. Eg:

```
curl https://raw.githubusercontent.com/simonmichael/hledger/1.50-branch/hledger/shell-completion/hledger-completion.bash \
  -o ~/.local/share/bash-completion/completions/hledger --create-dirs
```

Here’s what the bash completions should complete when you press TAB once or twice in a command line:

Before the command argument:

*   the “hledger”, “hledger-ui” and “hledger-web” executable names
*   general flags and flag values
*   hledger’s command argument. Eg `hledger <TAB><TAB>` should list all hledger commands, and `hledger b<TAB><TAB>` should list the ones starting with b.

After the command argument:

*   command-specific flags and flag values
*   account names
*   query prefixes, like `payee:` or `status:`
*   valid query values after these query prefixes: `acct:`, `code:`, `cur:`, `desc:`, `note:`, `payee:`, `real:`, `status:`, `tag:`. Eg `hledger reg acct:<TAB><TAB>` should list your top-level account names.
*   amount comparison operators after `amt:`.

When a completion includes special characters, backslashes will be inserted automatically; this does not work right in all cases.

#### [zsh](https://hledger.org/install.html#zsh)

1.   Ensure that [zsh-completions](https://github.com/zsh-users/zsh-completions/tree/0adf2f053ece56262ad8a173678add97c8ca4042) is installed and enabled.
2.   ? [discussion](https://www.reddit.com/r/plaintextaccounting/comments/1iqqpgg/hledger_shell_completions_for_zsh/)

## [Next steps](https://hledger.org/install.html#next-steps)

Nicely done! Now see [Docs](https://hledger.org/doc.html), or come to the [#hledger chat](https://hledger.org/support.html) where we’ll gladly share tips or receive your feedback.
