# xontrib-omx-macos

macOS utilities for Oh-My-Xonsh.

## Installation

To install use xpip:

```shell
xpip install xontrib-omx-macos
# or: xpip install -U git+https://github.com/oh-my-xonsh/xontrib-omx-macos
```

## Usage

Add this to your [rc.xsh]:

```shell
xontrib load omx_macos
```

[xonsh]: https://xon.sh
[omx]: https://github.com/oh-my-xonsh
[ohmyzsh]: https://github.com/ohmyzsh/ohmyzsh
[rc.xsh]: https://xon.sh/xonshrc.html

--------------------

## xontrib promotion (READ and REMOVE THIS SECTION)

After you create the xontrib repository you can do some helpful tasks to spread the word about your xontrib.

**Repository name**. It's a good practice to add `xontrib-` prefix before the name of your repository. It helps Github search find it.

**Add topics to the repository**. To show the xontrib repository in Github Topics please add topics `xonsh` and `xontrib` to the repository "About" setting. Also add thematic topics, for example,  `ssh` if your xontrib helps work with `ssh`.

**Easiest way to publish your xontrib to PyPi via Github Actions**. Users can install your xontrib via `pip install xontrib-myxontrib`. Easiest way to achieve it is to use Github Actions:

1. Register to https://pypi.org/ and [create API token](https://pypi.org/help/#apitoken).
2. Go to repository "Settings" - "Secrets" and add keys `PYPI_USERNAME` and `PYPI_PASSWORD`.
3. Click "Actions" link on your Github repository.
4. Click "Set up this workflow" on "Publish Python Package" Action.
5. Commit the config without any changes.
6. Now when you create new Release the Github Actions will publish the xontrib to PyPi automatically. Release status will be in Actions sction.

**Add preview image**. Add the image to repository "Settings" - "Options" - "Social preview". It allows to show preview image in Github Topics and social networks.

**Add xontrib to the xonsh**. To show xontrib name in `xontrib list` in xonsh add it to the [xonsh/xontribs_meta.py](https://github.com/xonsh/xonsh/blob/master/xonsh/xontribs_meta.py).
