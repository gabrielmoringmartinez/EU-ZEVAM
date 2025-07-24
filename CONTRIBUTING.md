# Contributing to EU-ZEVAM

<!-- This CONTRIBUTING.md is adapted from https://gist.github.com/peterdesmet/e90a1b0dc17af6c12daf6e8b2f044e7c -->

First of all, thanks for considering contributing to EU-ZEVAM! 👍 It's people like you that make it rewarding for us - the project maintainers - to work on EU-ZEVAM. 😊

EU-ZEVAM is an open source project, maintained by people who care. We are not directly funded to do so.

[repo]: https://github.com/gabrielmoringmartinez/European-passenger-car-stock-model
[issues]: https://github.com/gabrielmoringmartinez/European-passenger-car-stock-model/issues
[new_issue]: https://github.com/gabrielmoringmartinez/European-passenger-car-stock-model/issues/new
[citation]: https://github.com/gabrielmoringmartinez/European-passenger-car-stock-model#-citation

## Code of conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## How you can contribute

There are several ways you can contribute to this project. If you want to know more about why and how to contribute to open source projects like this one, see this [Open Source Guide](https://opensource.guide/how-to-contribute/).

### Share the love ❤️

Think EU-ZEVAM is useful? Let others discover it, by telling them in person, via Twitter or a blog post.

Using EU-ZEVAM for a paper you are writing? Consider [citing it](README.md#-citation).

### Ask a question ⁉️

Using EU-ZEVAM and got stuck? Browse the [documentation](README.md) to see if you can find a solution. Still stuck? Post your question as an [issue on GitHub][new_issue]. While we cannot offer user support, we'll try to do our best to address it, as questions often lead to better documentation or the discovery of bugs.

Want to ask a question in private? Contact the model maintainer by <gabriel.moeringmartinez@dlr.de>.

### Propose an idea 💡

Have an idea for a new medRCT feature? Take a look at the [documentation](README.md) and [issue list][issues] to see if it isn't included or suggested yet. If not, suggest your idea as an [issue on GitHub][new_issue]. While we can't promise to implement your idea, it helps to:

* Explain in detail how it would work.
* Keep the scope as narrow as possible.

See below if you want to contribute code for your idea as well.

### Report a bug 🐛

Using our_package and discovered a bug? That's annoying! Don't let others have the same experience and report it as an [issue on GitHub][new_issue] so we can fix it. A good bug report makes it easier for us to do so, so please include:

* Your operating system name and version (e.g. Mac OS 10.13.6).
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Improve the documentation 📖

Noticed a typo on the repository? Think a function could use a better example? Good documentation makes all the difference, so your help to improve it is very welcome!

#### Function documentation

Functions in this project are documented using standard Python docstrings, typically following the [Google format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

If you want to improve a function description:

1. Go to the [src/](src) directory in the [code repository][repo].

2. Open the relevant .py file that defines the function.

3. Update the docstring directly beneath the function definition.

4. [Propose a file change](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) with your improvements.

**Note:** Please follow the existing docstring style and conventions for consistency. 

### Contribute code 📝

Care to fix bugs, implement new functionality for EU-ZEVAM, update data to more recent years, or add new countries? Awesome! 👏 Have a look at the [issue list][issues] and leave a comment on the things you want to work on. See also the development guidelines below.

## Development guidelines

We try to follow the [GitHub flow](https://guides.github.com/introduction/flow/) for development.

1. Fork [this repo][repo] and clone it to your computer. To learn more about this process, see [this guide](https://guides.github.com/activities/forking/).
2. If you have forked and cloned the project before and it has been a while since you worked on it, [pull changes from the original repo](https://help.github.com/articles/merging-an-upstream-repository-into-your-fork/) to your clone by using `git pull upstream main`.
3. Create and activate a Python virtual environment:

    ```bash
    python -m venv venv
    ```

    - Activate environment on Windows (Only tested on Windows)

      ```bash
      venv\Scripts\activate
      ```

    - Activate environment on macOS/Linux:

      ```bash
      source venv/bin/activate
      ```
4. Install dependencies:
    ```bash
    pip install -r stock_model_requirements.txt
    ```

5. Make your changes:
    - Write your Python code inside the [src/](src) folder.
    - Add or update tests in the [tests/](tests) folder.
    - Document your code using Python docstrings (following the existing style).
    - Run tests locally using:
        ```bash
        python run_tests.py
        ```

6. Commit and push your changes.
7. Submit a [pull request](https://docs.github.com/de/get-started/exploring-projects-on-github/contributing-to-a-project#making-a-pull-request).