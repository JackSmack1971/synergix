---
title: "Editing files"
source_url: "https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files"
host: "docs.github.com"
depth: 2
selector: "article,main"
fetched_at: "2026-10-24T02:29:57.304Z"
---
In this article

# Editing files

You can edit files directly on GitHub in any of your repositories using the file editor.

Copy markdown

## In this article

## [Editing files in your repository](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-your-repository)

Tip

If a repository has any protected branches, you can't edit or upload files in the protected branch using GitHub. You can use GitHub Desktop to move your changes to a new branch and commit them. For more information, see [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [Committing and reviewing changes to your project in GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop).

Note

GitHub's file editor uses [CodeMirror](https://codemirror.net/).

1.  In your repository, browse to the file you want to edit.

2.  In the upper right corner of the file view, click to open the file editor. ![Screenshot of a file. In the header, a button, labeled with a pencil icon, is outlined in dark orange.](https://docs.github.com/assets/cb-47646/images/help/repository/edit-file-edit-button.png)

    Note

    Instead of editing and committing the file using the default file editor, you can optionally choose to use the [github.dev code editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor) by selecting the dropdown menu and clicking **github.dev**. You can also clone the repository and edit the file locally via GitHub Desktop by clicking **GitHub Desktop**.

    ![Screenshot of a file. In the header, a downwards-facing triangle icon is outlined in dark orange.](https://docs.github.com/assets/cb-18357/images/help/repository/edit-file-edit-dropdown.png)

3.  In the text box, make any changes you need to the file.

4.  Above the new content, click **Preview**.

    ![Screenshot of a file in edit mode. Above the file's contents, a tab labeled "Preview" is outlined in dark orange.](https://docs.github.com/assets/cb-35434/images/help/repository/edit-readme-preview-changes.png)

5.  Click **Commit changes...**

6.  In the "Commit message" field, type a short, meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message. For more information, see [Creating a commit with multiple authors or on behalf of an organization](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors).

7.  If you have more than one email address associated with your account on GitHub, click the email address drop-down menu and select the email address to use as the Git author email address. Only verified email addresses appear in this drop-down menu. If you enabled email address privacy, then a no-reply will be the default commit author email address. For more information about the exact form the no-reply email address can take, see [Setting your commit email address](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

    ![Screenshot of a GitHub pull request showing a dropdown menu with options to choose the commit author email address. octocat@github.com is selected.](https://docs.github.com/assets/cb-72047/images/help/repository/choose-commit-email-address.png)

8.  Below the commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is the default branch, you should choose to create a new branch for your commit and then create a pull request. For more information, see [Creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).

    ![Screenshot of a GitHub pull request showing a radio button to commit directly to the main branch or to create a new branch. New branch is selected.](https://docs.github.com/assets/cb-27122/images/help/repository/choose-commit-branch.png)

9.  Click **Commit changes** or **Propose changes**.


## [Editing files in another user's repository](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-another-users-repository)

When you edit a file in another user's repository, we'll automatically [fork the repository](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo) and [open a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request) for you.

1.  In another user's repository, browse to the folder that contains the file you want to edit. Click the name of the file you want to edit.

2.  Above the file content, click . On the page that appears, click **Fork this repository**.

3.  In the text box, make any changes you need to the file.

4.  Above the new content, click **Preview**.

    ![Screenshot of a file in edit mode. Above the file's contents, a tab labeled "Preview" is outlined in dark orange.](https://docs.github.com/assets/cb-35434/images/help/repository/edit-readme-preview-changes.png)

5.  Click **Commit changes...**

6.  In the "Commit message" field, type a short, meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message. For more information, see [Creating a commit with multiple authors or on behalf of an organization](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors).

7.  If you have more than one email address associated with your account on GitHub, click the email address drop-down menu and select the email address to use as the Git author email address. Only verified email addresses appear in this drop-down menu. If you enabled email address privacy, then a no-reply will be the default commit author email address. For more information about the exact form the no-reply email address can take, see [Setting your commit email address](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

    ![Screenshot of a GitHub pull request showing a dropdown menu with options to choose the commit author email address. octocat@github.com is selected.](https://docs.github.com/assets/cb-72047/images/help/repository/choose-commit-email-address.png)

8.  Click **Propose changes**.

9.  Type a title and description for your pull request.

10.  Click **Create pull request**.
