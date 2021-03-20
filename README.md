# Python-template  <!-- omit in toc -->

A simple template Python repository which describes a workflow and set of tools, to make group projects more manageable.

Other templates exist (see eg: [1](https://github.com/TezRomacH/python-package-template), [2](https://github.com/patevs/python-template), [3](https://github.com/scottclowe/python-template-repo)) and it would be worthwhile to read through them, but they generally feel quite bloated and were likely written for a very different programming environment than what you'll be working in. So, this one is an intentionally simple and ~~opinionated~~ _curated_ overview of a set of tools and practices that I like.


- [IDEs](#ides)
  - [VS Code](#vs-code)
  - [Jupyter Lab](#jupyter-lab)
  - [PyCharm](#pycharm)
- [Applications vs libraries](#applications-vs-libraries)
- [Virtual environments](#virtual-environments)
  - [Conda](#conda)
- [Coding style](#coding-style)
  - [Auto formatters](#auto-formatters)
  - [Linting](#linting)
  - [Logging](#logging)
- [Testing](#testing)
- [Contribution guide](#contribution-guide)
- [Package and upload](#package-and-upload)
- [Software versioning](#software-versioning)
- [Keep a change log](#keep-a-change-log)
- [Writing about Python](#writing-about-python)
- [Learning about Python](#learning-about-python)
- [An opinionated setup](#an-opinionated-setup)

## IDEs

### VS Code
[VS Code](code.visualstudio.com/) is a code editor based around a concept of extensions. By default it's fairly fast and lightweight (especially compared to some other IDEs) but you can easily add functionality -- this means you get all the functionality _you_ need without feeling like the IDE is too complex and bloated. Recommended extensions include:

- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) for your general Python needs. It packages Pylint (mentioned later), among other things.
- [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright) to make sure you spell words like ~~"dependancy"~~ "dependency" correctly.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) which provides useful shortcuts for markdown, and keeps the table of contents up to date automatically.

You can recommend certain extensions as part of a project, so that your collaborators as the same setup -- see [this tutorial](https://tattoocoder.com/recommending-vscode-extensions-within-your-open-source-projects/), or this project's [extensions.json](.vscode/extensions.json) file.

Instead of enabling all extensions for all projects (as is the default), I think it's better to rather disable each extension and then select "Enable (workspace)".

You may need to update the Python path. There are options:
- update `"python.pythonPath"` setting in `.vscode/settings.json`,
- click on a notification if it pops up, or
- click "Python x.y.z" in the panel at the bottom left of the screen.

Some writing about useful parts of VS Code:
- [Key bindings](https://code.visualstudio.com/docs/getstarted/keybindings). See also [VS Code shortcuts](https://alknemeyer.github.io/know-your-tools/#vs-code-shortcuts)
- [Quickly fix issues in VS Code](https://alknemeyer.github.io/know-your-tools/#quickly-fix-issues-in-vs-code)


### Jupyter Lab
Many projects use Jupyter notebooks. Not everyone realises that there is a new version of the Jupyter IDE, called Jupyter Lab. Some blog posts on getting a good set up are:

- [Improving the jupyter notebook workflow](https://alknemeyer.github.io/jupyter-notebook-workflow/)
- [Some unknown Jupyter features](https://alknemeyer.github.io/some-unknown-jupyter-features/)

It's worth mentioning that VS Code can also work with Notebooks, via the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).


### PyCharm
_I ([Alexander Knemeyer](https://github.com/alknemeyer)) don't use PyCharm, so someone else should document it here. For what it's worth, I think it's better to stick to VS Code. The IDEs are developed with different ideas of "what an editor should be" so I understand this is a personal choice, but if your project has new members who 1) may not have beefy computers (Pycharm is a bit of a resource hog), 2) don't know either IDE (VS Code is a lot simpler) or 3) work on multi-language projects, then recommending VS Code seems obvious to me. PyCharm also seems geared more towards web development._


## Applications vs libraries
Projects are _generally_ either applications or libraries. You should bear this in mind when deciding on what tools to include, and what each tool is useful for. An example is logging: libraries should log their activity (`logging.warning("Something bad happened!")`) but they shouldn't set the log level itself (`logging.basicConfig(level="DEBUG")`) - that should be done by applications, where the user decides what an appropriate level is.

Another example: applications are often run from the command line:
  
    $ python myapp.py

where `myapp.py` might import a library (`import mylibrary`).

A project can be both, though: write it as a library, and then include application-type code in a `__main__.py` file. Import it as normal when using it as a library, or run `python -m python_template` to run it as an app. See this project's [`__main__.py`](python_template/__main__.py) file.

This can also be done using `if __name__ == '__main__':` in your library's `__init__.py` file.


## Virtual environments
A virtual environment allows you to have different dependencies for multiple projects on the same computer -- without one, you'd have issues if two projects you're working with require different versions of the same module.

Another benefit is that multiple people can easily work on the same project by sharing a common virtual environment file. This prevents bugs that would otherwise occur from people (accidentally) having different dependencies.


### Conda
The official "getting started" with Conda guide [is here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html). If you just want a summary, install Conda however you want (I recommend [miniconda](https://docs.conda.io/en/latest/miniconda.html)) before proceeding as follows:

Create an environment using

    conda create --name <env_name> --no-default-packages python=3.9

Or whatever version of Python you want to use.

However, if you're working on an existing project, DON'T create a new environment! It will likely result in you having different versions of packages installed, which can create some confusing bugs as code which runs on one person's computer, breaks on another. Instead, an existing environment can be installed using,

    conda env create --file=environment.yml

where `environment.yml` is a file listing the dependencies of the project. Next, activate the environment using,

    conda activate <env_name>

Install packages using,

    conda install <package_a> <package_b> <...>

Some packages aren't available via Conda. In these cases, you can install pip and then `pip install` packages as needed:

    conda install pip
    pip install <package_name>

Conda will still keep track of packages installed this way.

If you've updated your dependency list (by installing, upgrading or removing a package) you should update the `environment.yml` file so that others can keep in sync. Do so as follows:

    conda env export --file environment.yml

This includes a `prefix` key which specifies the location of your environment variable, which _seems_ like it would fail when run on someone else's computer, but it doesn't. This doesn't feel like a "good" solution as the path would change each time someone re-generates the environment file. You could manually remove the prefix line (I haven't for the sake of this example). See [the docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment) for why the prefix line exists.

If you've messed up and want to start again, simply run:

    conda env remove --name <env_name>

Documentation for managing environments [is here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).


<!-- ### venv

TODO! The main advantage is that it's built in and totally universal. But perhaps I should write about it after I've used it more. -->


## Coding style
See the [Google style guide](https://google.github.io/styleguide/pyguide.html) for some thoughts on this, but bear in mind that Google is a huge organisation with many people working on large projects. You shouldn't expect their solutions/workflows to (in general) be perfect for smaller organisations.


### Auto formatters
Multiple tools exist which automatically format the style of your code. [This post](https://www.kevinpeters.net/auto-formatters-for-python) from 2018 compares the main three ([autopep8](https://github.com/hhatto/autopep8), [black](https://github.com/psf/black), [yapf](https://github.com/google/yapf/)).

While I don't particularly like the formatting style used by black, I really like the fact that its lack of options means that you don't have to waste time deciding on formatting rules with your colleagues. Programming is a form of creative expression, though, so choosing something like `yapf` (which is configurable) could lead to a more enjoyable development experience. Up to you!

Hoping that you'll remember to run them before each commit or pull request is a tad optimistic, but there are solutions for this:

- GitHub Actions ([tutorial here](https://peterevans.dev/posts/github-actions-how-to-automate-code-formatting-in-pull-requests/)) can format your code on a pull request, and don't require developers to install/configure anything on their computers. See [this commit](https://github.com/alknemeyer/python-template/commit/07dbbd34329a7f5cf345f126689112db6f4f2d8f) for an example of formatting due to a GitHub Action.
  
  You can install them easily (links: [autopep8](https://github.com/peter-evans/autopep8), [black](https://github.com/psf/black#github-actions)) or specify them in a configuration file (see [this project's](.github/workflows/black.yml) configuration for an example). GitHub actions are free for public repositories, and free within limits for private repositories if you have GitHub Pro.

  A disadvantage of this approach is that your commit history becomes a bit more confusing.

- Git Hooks (tutorials [here](https://githooks.com/) and [here](https://www.hostinger.com/tutorials/how-to-use-git-hooks/)) _basically_ do the same thing, but locally. Strangely, hooks aren't tracked in your Git repository, so [it is advised](https://stackoverflow.com/a/57592188/1892669) to put your hooks in a [`git_hooks/`](`.git_hooks/`) folder before configuring Git to use that folder: `git config core.hooksPath "./git_hooks"`. You'd need to tell others to run that command to configure their projects before contributing to the project.

  If you're worried about running cross platform code: Git on Windows packages Bash and some common utilities, so you can do some Unix style scripting in your hooks.

I think there's a balance between "super easy dev environment setup" (GitHub Actions) and "pre-formatting code before making pull requests makes Git simpler" (Git Hooks). You could use both!

I like to use GitHub Actions, then configure VS Code to format code on save by adding the following line to [`.vscode/settings.json`](.vscode/settings.json):

    "editor.formatOnSave": true,
    "python.formatting.provider": "black",

It's worth mentioning that there are alternatives to GitHub Actions, and that GitHub Actions/Git Hooks can be used for far more than just formatting code. They could be configured to run tests, lint code, automatically remove the `prefix:` line of an `environment.yml` file, etc.


### Linting
To lint code (find missing imports, check for unused code, etc) consider using [pylint](https://pylint.org/). Pylance makes this totally painless, so I haven't looked into this very much - it Just Works.


### Logging
It's tempting to add `print(...)` statements everywhere to tell the user what code is running, but there is A Better Way (TM). See [this blog post](https://alknemeyer.github.io/embedded-comms-with-python-part-2/#setting-up-logging) for introduction to Python's `logging` module.

[Ziko](https://github.com/zicodasilva/) has provided a snippet which sets up a logger, and configures it to level specified by the `LOG_LEVEL` environment variable. If no variable is set, `logging.INFO` is used. This makes it easy to switch between log levels using environment variables, without changing code.

```python
import logging, os

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL)
```

To use another log level, launch Python as follows:

    export LOG_LEVEL="DEBUG" && python script.py


## Testing
TO DO! When I find time to evaluate options.


## Contribution guide
TO DO! Likely just a link or two. Perhaps [African-Robotics-Unit/newcomers-guide.md](https://github.com/African-Robotics-Unit/docs/blob/main/newcomers-guide.md)?


## Package and upload
You'll use a lot of freely shared open source code to get to this point, so why not share your code as well? `flit` makes this ridiculously easy -- [the website](https://flit.readthedocs.io/en/latest/) explains how, so I won’t repeat them here, but you can look at [this repository](https://github.com/alknemeyer/optoforce) for a simple example.

Other projects use `setup.py` and `setup.cfg`. You could use those, but I honestly don't see the point, given that Flit exists.

> Again: there is a difference between packaging (a [`pyproject.toml`](./pyproject.toml) file which describes a loose set of requirements for _the project_, so that when others `pip install` it, the project's requirements are installed too) and virtual environments (an [`environment.yml`](./environment.yml) file which describes a specific set of dependancies, which is useful to make sure you and your collaborators have the exact same set of dependancies, including development dependancies, and can switch between multiple projects the same computer)

Flit requires that the package version is specified by a variable named `__version__` in `__init__.py`, which brings us to:


## Software versioning
Software libraries should be given a version number so that users of the library know what they have installed. [Semantic Versioning](https://semver.org/) (aka "SemVer") seems to be the most popular approach, summarized as follows:

> Given a version number MAJOR.MINOR.PATCH, increment the:
> - MAJOR version when you make incompatible API changes,
> - MINOR version when you add functionality in a backwards compatible manner, and
> - PATCH version when you make backwards compatible bug fixes.
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

There are other versioning styles -- for example, [Calendar Versioning](https://calver.org/) ("CalVer") is used by Ubuntu, where "Ubuntu 18.04" represents the version released in April of 2018. See also [sentimental versioning](http://sentimentalversioning.org/) for a fun read :)


## Keep a change log
On the subject of software versioning, it's a good idea to document the evolution of a project via a change log. See [keepachangelog.com](https://keepachangelog.com/en/1.0.0/) for details, where this idea is explained in more detail. Examples include keepachangelog.com's [CHANGELOG.md](https://github.com/olivierlacan/keep-a-changelog/blob/master/CHANGELOG.md), the Julia [HISTORY.md](https://github.com/JuliaLang/julia/blob/master/HISTORY.md) file and this [HISTORY.rst](https://github.com/pwitab/ublox/blob/master/HISTORY.rst) file which I think serves as a nice simple template - they're named differently, but all represent the same idea.


## Writing about Python
Programmers often write "python" (lower case "p"), but it should be written with an upper case "P" in proper reports. It's similar to how Git commit messages are usually written in a specific, terse style that you wouldn't use when writing a dissertation.


## Learning about Python
[Pycoder's Weekly](https://pycoders.com/): get an email every Tuesday with links to articles and useful Python projects. It's a nice way to continually improve your knowledge of the language and ecosystem.

This post and others describe a set of "best practices". You may rightly feel that they are only worth the hassle for Big Public Projects. However, making mistakes on Big Public Projects can be scary, so I suggest testing these things out on smaller side projects while you learn.


## An opinionated setup
I don't think you'll go wrong if you use:
- IDE: VS Code (with Pylance + friends).
- Python distribution: Conda.
- Autoformatter: Black, formatting on save and using GitHub Actions for enforcement.
- Packaging: flit.
- Git work flow: [feature-branch](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).
