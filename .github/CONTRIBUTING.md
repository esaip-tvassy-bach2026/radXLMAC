# Welcome to radXLMAC contributing guide
First, thank you for investing your time in contributing to our project!

Please read our [Code of Conduct](https://github.com/esaip-tvassy-bach2026/radXLMAC/blob/main/.github/CONTRIBUTING.md) to keep our community approachable and respectable.<br />Please also read the [license](https://github.com/esaip-tvassy-bach2026/radXLMAC/blob/main/LICENSE.txt) of this project to keep in mind what type of license it is.

Use the table of contents icon on the top left corner of this document to get to a specific section of this guide quickly.
## New contributor guide
To get an overview of the project, read the [README](https://github.com/esaip-tvassy-bach2026/radXLMAC/blob/main/.github/README.md) file. Here are some resources to help you get started with open source contributions:

- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/git-basics/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)

If you need mre information on how writing Markdown files, please see "[Using Markdown and Liquid in GitHub Docs](https://docs.github.com/en/contributing/writing-for-github-docs/using-markdown-and-liquid-in-github-docs)."
## Get started
1. Fork the repository.
- Using GitHub Desktop:
  - [Getting started with GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop) will guide you through setting up Desktop.
  - Once Desktop is set up, you can use it to [fork the repo](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop)!

- Using the command line:
  - [Fork the repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository) so that you can make your changes without affecting the original project until you're ready to merge them.

2. Create a working branch and start with your changes!
### Commit your update
Commit the changes once you are happy with them. Don't forget to use the "[Self review checklist](https://docs.github.com/en/contributing/collaborating-on-github-docs/self-review-checklist)" to speed up the review process :zap:.
### Pull Request
When you're finished with the changes, create a pull request, also known as a PR.
- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.
- Enable the checkbox to [allow maintainer edits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork) so the branch can be updated for a merge.
Once you submit your PR, a community member will review your proposal. We may ask questions or request additional information.
- We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.
- As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).
- If you run into any merge issues, checkout this [git tutorial](https://github.com/skills/resolve-merge-conflicts) to help you resolve merge conflicts and other issues.
### Your PR is merged!
Congratulations :tada::tada: The radXLMAC team thanks you :sparkles:.

Once your PR is merged, your contributions will be publicly visible.
## Windows contributions
This program can be developed on Windows with a Python IDE, however a few potential gotchas need to be kept in mind:

1. Regular Expressions: Windows uses `\r\n` for line endings, while Unix-based systems use `\n`. Therefore, when working on Regular Expressions, use `\r?\n` instead of `\n` in order to support both environments. You can specify your parameters in Git if you use [GitForWindows](https://github.com/GitForWindows/git).
2. Paths: Windows systems use `\` for the path separator.
3. Bash: Not every Windows developer has a terminal that fully supports Bash, so there's a little tip: you can use [GitForWindows](https://github.com/GitForWindows/git) instead of [Git](https://www.git-scm.com/).