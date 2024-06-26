# Contributing to logging_helper

Table of contents:

- Bug reports and enhancement requests
- Finding an issue to contribute to
- Submitting a pull request
  - Version control, Git, and GitHub
  - Getting started with Git
  - Create a fork of logging_helper
  - Creating a feature branch
  - Making code changes
  - Pushing your changes
  - Making a pull request
  - Updating your pull request
  - Updating the development environment
- Tips for a successful pull request

All contributions, bug reports, bug fixes, documentation improvements,
enhancements, and ideas are welcome.

## Bug reports and enhancement requests

Bug reports and enhancement requests are an important part of making logging_helper more stable and
are curated though GitHub issues. When reporting and issue or request, please select the [appropriate
category and fill out the issue form fully](https://github.com/davidquintanarperez/logging_helper/issues/new/choose)
to ensure others and the core development team can fully understand the scope of the issue.

The issue will then show up to the logging_helper community and be open to comments/ideas from others.

## Finding an issue to contribute to

If you are brand new to logging_helper or open-source development, we recommend searching
the [GitHub "issues" tab](https://github.com/davidquintanarperez/logging_helper/issues)
to find issues that interest you. Unassigned issues labeled [Docs](https://github.com/davidquintanarperez/logging_helper/issues?q=is%3Aopen+sort%3Aupdated-desc+label%3ADocs+no%3Aassignee)
and [good first issue](https://github.com/davidquintanarperez/logging_helper/issues?q=is%3Aopen+sort%3Aupdated-desc+label%3A%22good+first+issue%22+no%3Aassignee)
are typically good for newer contributors.

Once you've found an interesting issue, it's a good idea to assign the issue to yourself,
so nobody else duplicates the work on it. On the GitHub issue, a comment with the exact
text `take` to automatically assign you the issue
(this will take seconds and may require refreshing the page to see it).

If for whatever reason you are not able to continue working with the issue, please
unassign it, so other people know it's available again. You can check the list of
assigned issues, since people may not be working in them anymore. If you want to work on one
that is assigned, feel free to kindly ask the current assignee if you can take it
(please allow at least a week of inactivity before considering work in the issue discontinued).

We have several `contributor community <community>` communication channels, which you are
welcome to join, and ask questions as you figure things out. Among them are regular meetings for
new contributors, dev meetings, a dev mailing list, and a Slack for the contributor community.
All logging_helper contributors are welcome to these spaces, where they can connect with each other. Even
maintainers who have been with us for a long time felt just like you when they started out, and
are happy to welcome you and support you as you get to know how we work, and where things are.
Take a look at the next sections to learn more.

## Submitting a pull request

### Version control, Git, and GitHub

logging_helper is hosted on [GitHub](https://www.github.com/davidquintanarperez/logging_helper), and to
contribute, you will need to sign up for a [free GitHub account](https://github.com/signup/free).
We use [Git](https://git-scm.com/) for
version control to allow many people to work together on the project.

If you are new to Git, you can reference some of these resources for learning Git. Feel free to reach out
to the `contributor community <community>` for help if needed:

- [Git documentation](https://git-scm.com/doc).

Also, the project follows a forking workflow further described on this page whereby
contributors fork the repository, make changes and then create a pull request.
So please be sure to read and follow all the instructions in this guide.

If you are new to contributing to projects through forking on GitHub,
take a look at the [GitHub documentation for contributing to projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).
GitHub provides a quick tutorial using a test repository that may help you become more familiar
with forking a repository, cloning a fork, creating a feature branch, pushing changes and
making pull requests.

Below are some useful resources for learning more about forking and pull requests on GitHub:

- the [GitHub documentation for forking a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
- the [GitHub documentation for collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests).
- the [GitHub documentation for working with forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks).

### Getting started with Git

[GitHub has instructions](https://docs.github.com/en/get-started/quickstart/set-up-git) for installing git,
setting up your SSH key, and configuring git.  All these steps need to be completed before
you can work seamlessly between your local repository and GitHub.

### Create a fork of logging_helper

You will need your own copy of logging_helper (fork) to work on the code. Go to the [logging_helper project
page](https://github.com/davidquintanarperez/logging_helper) and hit the `Fork` button.
Please uncheck the box to copy only the main branch before selecting `Create Fork`.
You will want to clone your fork to your machine

```shell
git clone https://github.com/your-user-name/logging_helper.git logging_helper-yourname
cd logging_helper-yourname
git remote add upstream https://github.com/davidquintanarperez/logging_helper.git
git fetch upstream
```

This creates the directory `logging_helper-yourname` and connects your repository to
the upstream (main project) *logging_helper* repository.

> **Note**: Performing a shallow clone (with `--depth==N`, for some `N` greater or equal to 1) might break some tests
> and features as `pd.show_versions()` as the version number cannot be computed anymore.

### Creating a feature branch

Your local `main` branch should always reflect the current state of logging_helper repository.
First ensure it's up-to-date with the main logging_helper repository.

```shell
 git checkout main
 git pull upstream main --ff-only
```

Then, create a feature branch for making your changes. For example

```shell
git checkout -b shiny-new-feature
```

This changes your working branch from `main` to the `shiny-new-feature` branch.  Keep any
changes in this branch specific to one bug or feature, so it is clear
what the branch brings to logging_helper. You can have many feature branches
and switch in between them using the `git checkout` command.

When you want to update the feature branch with changes in main after
you created the branch, check the section on `updating a PR <contributing.update-pr>`.

### Making code changes

Before modifying any code, ensure you follow the `contributing environment <contributing_environment>`
guidelines to set up an appropriate development environment.

Then, once you have made code changes, you can see all the changes you've currently made by running.

```shell
git status
```

For files, you intended to modify or add, run.

```shell
git add path/to/file-to-be-added-or-changed.py
```

Running `git status` again should display

```shell
On branch shiny-new-feature
   modified:   /relative/path/to/file-to-be-added-or-changed.py
```

Finally, commit your changes to your local repository with an explanatory commit
message

```shell
git commit -m "your commit message goes here"
```

### Pushing your changes

When you want your changes to appear publicly on your GitHub page, push your
forked feature branch's commits

```shell
git push origin shiny-new-feature
```

Here `origin` is the default name given to your remote repository on GitHub.
You can see the remote repositories

```shell
git remote -v
```

If you added the upstream repository as described above you will see something
like

```shell
origin  git@github.com:yourname/logging_helper.git (fetch)
origin  git@github.com:yourname/logging_helper.git (push)
upstream        git://github.com/davidquintanarperez/logging_helper.git (fetch)
upstream        git://github.com/davidquintanarperez/logging_helper.git (push)
```

Now your code is on GitHub, but it is not yet a part of the logging_helper project. For that to
happen, a pull request needs to be submitted on GitHub.

### Making a pull request

Once you have finished your code changes, your code change will need to follow the 
`logging_helper contribution guidelines <contributing_codebase>` to be successfully accepted.

If everything looks good, you are ready to make a pull request. A pull request is how
code from your local repository becomes available to the GitHub community to review
and merged into project to appear the in the next release. To submit a pull request:

#. Navigate to your repository on GitHub
#. Click on the `Compare & pull request` button
#. You can then click on `Commits` and `Files Changed` to make sure everything looks
   okay one last time
#. Write a descriptive title that includes prefixes. logging_helper uses a convention for title
   prefixes. Here are some common ones along with general guidelines for when to use them:

    * ENH: Enhancement, new functionality
    * BUG: Bug fix
    * DOC: Additions/updates to documentation
    * TST: Additions/updates to tests
    * BLD: Updates to the build process/scripts
    * PERF: Performance improvement
    * TYP: Type annotations
    * CLN: Code cleanup

#. Write a description of your changes in the `Preview Discussion` tab
#. Click `Send Pull Request`.

This request then goes to the repository maintainers, and they will review
the code.

### Updating your pull request

Based on the review you get on your pull request, you will probably need to make
some changes to the code. You can follow the `code committing steps <contributing.commit-code>`
again to address any feedback and update your pull request.

It is also important that updates in the logging_helper `main` branch are reflected in your pull request.
To update your feature branch with changes in the logging_helper `main` branch, run:

```shell
git checkout shiny-new-feature
git fetch upstream
git merge upstream/main
```

If there are no conflicts (or they could be fixed automatically), a file with a
default commit message will open, and you can simply save and quit this file.

If there are merge conflicts, you need to solve those conflicts. See for
example at https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/
for an explanation on how to do this.

Once the conflicts are resolved, run:

#. `git add -u` to stage any files you've updated;
#. `git commit` to finish the merge.

> If you have uncommitted changes at the moment you want to update the branch with `main`, you will need to `stash`
> them prior to updating (see the [stash docs](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)).
> This will effectively store your changes, and they can be reapplied after updating.

After the feature branch has been update locally, you can now update your pull
request by pushing to the branch on GitHub:

```shell
git push origin shiny-new-feature
```

Any `git push` will automatically update your pull request with your branch's changes
and restart the `Continuous Integration <contributing.ci>` checks.

### Updating the development environment

It is important to periodically update your local `main` branch with updates from the logging_helper `main`
branch and update your development environment to reflect any changes to the various packages that
are used during development.`

If using `pip <contributing.pip>` , do:

```shell
 git checkout main
 git fetch upstream
 git merge upstream/main
 # activate the virtual environment based on your platform
 python -m pip install --upgrade -r requirements-dev.txt
```

## Tips for a successful pull request

If you have made it to the *Making a pull request* phase, one of the core contributors may
take a look. Please note however that a handful of people are responsible for reviewing
all the contributions, which can often lead to bottlenecks.

To improve the chances of your pull request being reviewed, you should:

- **Reference an open issue** for non-trivial changes to clarify the PR's purpose
- **Ensure you have appropriate tests**. These should be the first part of any PR
- **Keep your pull requests as simple as possible**. Larger PRs take longer to review
- **Ensure that CI is in a green state**. Reviewers may not even look otherwise
- **Keep** *Updating your pull request*, either by request or every few days
