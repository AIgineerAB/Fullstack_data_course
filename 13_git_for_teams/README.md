# Working with git and github in teams

**git and github in software teams - part 1**

<a href="https://www.youtube.com/watch?v=mIERG2Rck48" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/git_github/git_team.png?raw=true" alt="git and github in teams" width="600">
</a>


## Working with branches

By default, there is one branch called _main_ in both local and remote repositories. This branch serves as the official project history. Developers should work on a new branch whenever they work on a new feature. This is pacticularly important when working in a team.

- `git pull origin main`</br>
  Before creating a new branch, you should update your local main branch by pulling all changes from the main branch of the remote repository. This is to prevent missing changes made by other developers in your team to the central codebase.

- `git branch` and `git checkout`</br>
  After making sure that your local main branch is up-to-date with the remote repository, you can create a new branch with a custom name, for instance, _feature_, with

  ```console
  git branch feature
  ```

  and switch to the new branch with

  ```console
  git checkout feature
  ```

  Alternatively, a short version of these two is `git checkout -b feature`

  Then, you can start working on this feature branch.

- `git push origin feature`</br>
  When you are done with the feature branch, you need to first push the changes of the local feature branch to the remote feature branch. This means that you will NOT update the remote main branch directly.

- pull request and merge </br>
  When the remote feature branch is up-to-date, other developers can find the feature branch on Github but the remote main branch is intact. Then, you can create a pull request, and ask other developers to review and decide if the changes can be merged to the remote main branch.

  Below we have added text for chapter 2 on the feature branch locally and pushed the change to the remote feature branch:

<img src="https://github.com/kokchun/assets/blob/main/git_github/feature.png?raw=true" width="500">

<br>

<img src="https://github.com/kokchun/assets/blob/main/git_github/pull request.png?raw=true" width="500">

The remote main branch will be updated when the pull request is merged. You can modify the branch protection rule to require a pull request for any merge and approvals by reviewers.

<img src="https://github.com/kokchun/assets/blob/main/git_github/merge.png?raw=true" width="500">

## Project management and automated workflow

There are several features in Github that can enhance project management and automate workflow of a project. These are particularly important for the efficiency of team work. Here are some of these features:

Projects, issues and tasks

Github project provides a kanban-style board to track tasks. These tasks can be integrated with Github issues and pull request. The workflow, for instance, when having a bug, becomes:

- create a new task in github projects and create a linked issue using ctrl+return
- you can choose which repository where the issue will be linked to
- when a fix is done, push to your branch and create a pull request into main
- refer to an issue number in the pull request by writing `fix #issue_number`
- when the pull request is closed, the issue will be closed automatically, and the task will also be moved to _DONE_ automatically on the project board


<img src="https://github.com/kokchun/assets/blob/main/git_github/project.png?raw=true" width="500">

<img src="https://github.com/kokchun/assets/blob/main/git_github/task.png?raw=true" width="500">

## Read more

## Other videos
