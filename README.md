# Python-template

This is a template Python repository which describes a workflow and set of tools, to make group projects more manageable.

Other templates exist (see eg: [1](https://github.com/TezRomacH/python-package-template), [2](https://github.com/patevs/python-template), [3](https://github.com/scottclowe/python-template-repo)) and it would be worthwhile to read through them, but they generally feel quite bloated and were likely written for a very different programming environment than what you'll be working in. So, this one is intentionally quite simple.


## IDEs

### VS Code

VS Code is a code editor based around a concept of extensions. By default it's fairly fast and lightweight (especially compared to some other IDEs) but you can easily install just what you need for a particular project -- this means you get all the functionality _you_ need with feeling like the IDE is too complex and bloated. Recommended extensions include:

- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) for your general Python needs. It packages Pylint (mentioned later), among other things
- [Spell Right](https://marketplace.visualstudio.com/items?itemName=ban.spellright) to make sure you spell words like ~~"dependancy"~~ "dependency" correctly

You can recommend certain extensions as part of a project -- see [this tutorial](https://tattoocoder.com/recommending-vscode-extensions-within-your-open-source-projects/).

Instead of enabled all extensions for all projects, it's better to rather disable the extension and then select "Enable (workspace)".

You may need to update the `"python.pythonPath"` setting in `.vscode/settings.json` to your actual virtual environment, click on a notification if it pops up, or just click "Python x.y.z" in the panel at the bottom left of the screen.

Some writing about useful parts of VS Code:
- [Key bindings](https://code.visualstudio.com/docs/getstarted/keybindings). See also [VS Code shortcuts](https://alknemeyer.github.io/know-your-tools/#vs-code-shortcuts)
- [Quickly fix issues in VS Code](https://alknemeyer.github.io/know-your-tools/#quickly-fix-issues-in-vs-code)


## Jupyter Lab
Many projects use Jupyter notebooks. Not everyone realises that there is a new version of the Jupyter IDE, called Jupyter Lab. Some blog posts on getting a good set up are:

- [Improving the jupyter notebook workflow](https://alknemeyer.github.io/jupyter-notebook-workflow/)
- [Some unknown Jupyter features](https://alknemeyer.github.io/some-unknown-jupyter-features/)

It's worth mentioning that VS Code can also work with Notebooks, via the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).


### PyCharm
_I ([Alexander Knemeyer](https://github.com/alknemeyer)) don't use PyCharm, so someone else should document it here. For what it's worth, I think it's better to stick to VS Code. The IDEs are developed with different ideas of "what an editor should be" so I understand this is a personal choice, but if your project has new members who 1) may not have beefy computers (Pycharm is a bit of a resource hog), 2) don't know either IDE (VS Code is a lot simpler) or 3) work on multi-language projects, then recommending VS Code seems obvious to me._


## Virtual environments

### Conda
The official "getting started" with Conda guide [is here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html). If you just want a summary, install Conda however you want (I recommend [miniconda](https://docs.conda.io/en/latest/miniconda.html)) before proceeding as follows:

Create an environment using

    conda create --name <env_name> python=3.9

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

Conda will still keep track of packages installed this way. If you've updated your dependency list (by installing, upgrading or removing a package) you should update the `environment.yml` file so that others can keep in sync. Do so as follows:

    conda env export > environment.yml

Documentation for managing environments [is here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).


## Coding style
See the [Google style guide](https://google.github.io/styleguide/pyguide.html) for some thoughts on this, but bear in mind that Google is a huge organisation with many people working on large projects. You shouldn't expect their solutions/workflows to (in general) be perfect for smaller organisations.


### Auto formatters
Multiple tools exist which automatically format the style of your code. This is a highly contentious topic -- [this post](https://www.kevinpeters.net/auto-formatters-for-python) from 2018 compares the main three ([autopep8](https://github.com/hhatto/autopep8), [black](https://github.com/psf/black), [yapf](https://github.com/google/yapf/)).

Hoping that you'll remember to run them before each commit or pull request is a tad optimistic, but there are solutions for this:
- GitHub Actions ([tutorial here](https://peterevans.dev/posts/github-actions-how-to-automate-code-formatting-in-pull-requests/)) can format your code on a pull request, and don't require developers to install/configure anything on their computers. Links: [autopep8](https://github.com/peter-evans/autopep8), [black](https://github.com/psf/black#github-actions)
- Git Hooks (tutorials [here](https://githooks.com/) and [here](https://www.hostinger.com/tutorials/how-to-use-git-hooks/)) which _basically_ do the same thing, but locally


### Linting
To lint code (find missing imports, check for unused code, etc) consider using [pylint](https://pylint.org/).


### Logging
It's tempting to add `print(...)` statements everywhere to tell the user what code is running, but there is A Better Way (TM). See [this blog post](https://alknemeyer.github.io/embedded-comms-with-python-part-2/#setting-up-logging) for an example `logging` setup.


## Package and upload
You'll use a lot of freely shared open source code to get to this point, so why not share your code as well? `flit` makes this ridiculously easy -- [the website](https://flit.readthedocs.io/en/latest/) explains how, so I won’t repeat them here, but you can look at [this repository](https://github.com/alknemeyer/optoforce) for a simple example.

> Note: there is a difference between packaging (a [`pyproject.toml`](./pyproject.toml) file which describes a loose set of requirements for _the project_, so that when others `pip install` it, the project's requirements are installed too) and virtual environments (an [`environment.yml`](./environment.yml) file which describes a specific set of dependancies, which is useful to make sure you and your collaborators have the exact same set of dependancies, including development dependancies, and can switch between multiple projects the same computer)


## Writing about Python
Programmers often write "python" (lower case "p") but it should be written with an upper case "P"


## Learning about Python
[Pycoder's Weekly](https://pycoders.com/): get an email every Tuesday with links to articles and useful Python projects. It's a nice way to continually improve your knowledge of the language and ecosystem


## Opinionated setup

You can't really go wrong if you use:
- IDE: VS Code (with Pylance + friends)
- Python distribution: Conda
- Autoformatter: Black, using GitHub Actions to enforce it
- Packaging: flit
- Git work flow: [feature-branch](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
