# Contributing to AIR-Bench

Thanks for your interest in contributing to AIR-Bench. We're grateful for your initiative! ❤️

In this guide, we're going to go through the steps for each kind of contribution, and good and bad examples of what to do. We look forward to your contributions!

## 🐞 Bugs and issues

### Submitting issues

We love to get issue reports. But we love it even more if they're in the right format. For any bugs you encounter, we need you to:

* **Describe your problem**: What exactly is the bug. Be as clear and concise as possible
* **Why do you think it's happening?** If you have any insight, here's where to share it

There are also a couple of nice to haves:

* **Environment:** Operating system, `air-benchmark` version, python version,...
* **Screenshots:** If they're relevant

<a name="-making-your-first-submission"></a>
## 🥇 Making your first submission

0. Associate your local git config with your GitHub account. If this is your first time using git you can follow [the steps](#associate-with-github-account).
1. [Fork the AIR-Bench repo](https://github.com/AIR-Bench/AIR-Bench/fork) and clone onto your computer.
1. Configure git pre-commit hooks. Please follow [the steps](#install-pre-commit-hooks)
1. Create a [new branch](#naming-your-branch), for example `fix-models-bug-1`.
1. Work on this branch to do the fix/improvement.
1. Commit the changes with the [correct commit style](#writing-your-commit-message).
1. Make a pull request.
1. Submit your pull request and wait for all checks to pass.
1. Request reviews from one of [the code owners](.github/CODEOWNERS).
1. Get a LGTM 👍 and PR gets merged.

**Note:** If you're just fixing a typo or grammatical issue, you can go straight to a pull request.

### Associate with your GitHub account

- Confirm username and email on [your profile page](https://github.com/settings/profile).
- Set git config on your computer.

```shell
git config user.name "YOUR GITHUB NAME"
git config user.email "YOUR GITHUB EMAIL"
```

- (Optional) Reset the commit author if you made commits before you set the git config.

```shell
git checkout YOUR-WORKED-BRANCH
git commit --amend --author="YOUR-GITHUB-NAME <YOUR-GITHUB-EMAIL>" --no-edit
git log  # to confirm the change is effective
git push --force
```

### Install pre-commit hooks

In DocArray we use git's pre-commit hooks in order to make sure the code matches our standards of quality and documentation.
It's easy to configure it:

1. `pip install pre-commit`
1. `pre-commit install`

Now you will be automatically reminded to add docstrings to your code. `black` will take care that your code will match our style. Note that `black` will fail your commit but reformat your code, so you just need to add the files again and commit **again**.

## 📝 Code style conventions:

Most of our codebase is written in Python.

### PEP compliance

We comply to the official PEP: E9, F63, F7, F82 code style and required every contribution to follow it. This is enforced by using [ruff](https://github.com/charliermarsh/ruff) in our CI and in our pre-commit hooks.

### Python version
DocArray is compatible with Python 3.7 and above, therefore we can't accept contribution that used features from the newest Python versions without ensuring compatibility with python 3.7

### Code formatting

All of our Python codebase follows formatting standard. We are following the [PEP8](https://peps.python.org/pep-0008/) standard, and we require that every code contribution is formatted using [black](https://github.com/psf/black) with the default configurations.
If you have installed the pre-commit hooks the formatting should be automatic on every commit. Moreover, our CI will block contributions that do not respect these conventions.

### Type hints

Python is not a strongly typed programming language. Nevertheless, the use of [type hints](https://docs.python.org/3/library/typing.html)
contributes to a better codebase, especially when reading, reviewing and refactoring. Therefore, we **require every contribution
to use type hints**, unless there are strong reasons for not using them.

<a name="-naming-conventions"></a>
## ☑️ Naming conventions

For branches, commits, and PRs we follow some basic naming conventions:

* Be descriptive
* Use all lower-case
* Limit punctuation
* Include one of our specified [types](#specify-the-correct-types)
* Short (under 70 characters is best)
* In general, follow the [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/#summary) guidelines


### Specify the correct types

Type is an important prefix in PR, commit message. For each branch, commit, or PR, we need you to specify the type to help us keep things organized. For example,

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: build, ci, chore, docs, feat, fix, refactor, style, or test.
```

- `ci`: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- `docs`: Documentation only changes
- `feat`: A new feature
- `fix`: A bug fix
- `perf`: A code change that improves performance
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: updating grunt tasks etc.; no production code change

### Writing your commit message

A good commit message helps us track DocArray's development. A pull request with a bad commit message will be *rejected* automatically in the CI pipeline.

Commit messages should stick to our [naming conventions](#-naming-conventions) outlined above, and use the format `type(scope?): subject`:

* `type` is one of the [types above](#specify-the-correct-types).
* `scope` is optional, and represents the module your commit is working on.
* `subject` explains the commit, without an ending period`.`

For example, a commit that fixes a bug in the executor module should be phrased as: `fix(executor): fix the bad naming in init function`

> Good examples:
>
```text
fix(elastic): fix batching in elastic document store
feat: add remote api
```

> Bad examples:
>

| Commit message                                                                                  | Feedback                           |
|-------------------------------------------------------------------------------------------------|------------------------------------|
| `doc(101): improved 101 document`                                                               | Should be `docs(101)`              |
| `tests(flow): add unit test to document array`                                                  | Should be `test(array)`            |
| `DOC(101): Improved 101 Documentation`                                                          | All letters should be in lowercase |
| `fix(pea): i fix this issue and this looks really awesome and everything should be working now` | Too long                           |
| `fix(array):fix array serialization`                                                            | Missing space after `:`            |
| `hello: add hello-world`                                                                        | Type `hello` is not allowed        |
