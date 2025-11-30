GIT_COMMANDS = """

# Git Commands Cheat Sheet with Explanations

## 1. Setup and Config
```bash
git config --global user.name "Your Name"
# Sets the name you want attached to your commit transactions

git config --global user.email "your.email@example.com"
# Sets the email you want attached to your commit transactions

git config --list
# Lists all your Git configurations
```

## 2. Getting and Creating Projects
```bash
git init
# Initializes a new Git repository in the current directory

git clone [url]
# Downloads a project and its version history from the provided URL
```

## 3. Basic Snapshotting
```bash
git status
# Shows the status of changes as untracked, modified, or staged

git add [file]
# Adds a file to the staging area for a commit

git add .
# Stages all changed files in the current directory for a commit

git commit -m "[descriptive message]"
# Commits the staged changes with a message

git commit -am "[descriptive message]"
# Adds and commits tracked files in one step with a message

git rm [file]
# Deletes the file from your working directory and stages the deletion

git mv [file-original] [file-renamed]
# Renames a file and stages the change
```

## 4. Branching and Merging
```bash
git branch
# Lists all local branches in the repository

git branch [branch-name]
# Creates a new branch

git checkout [branch-name]
# Switches to the specified branch

git checkout -b [branch-name]
# Creates and switches to a new branch

git merge [branch]
# Combines the specified branch’s history into the current branch

git branch -d [branch-name]
# Deletes the specified branch
```

## 5. Inspecting a Repository
```bash
git log
# Shows the commit history for the repository

git log --oneline
# Shows a compressed version of the commit history

git diff
# Shows the differences between the working directory and the staging area

git show [commit]
# Shows information about the specified commit
```

## 6. Rewriting History
```bash
git reset [commit]
# Resets your working directory to match a previous commit, but leaves changes in the working directory

git reset --hard [commit]
# Resets your working directory and staging area to match a previous commit, discarding all changes

git revert [commit]
# Creates a new commit that undoes the changes of the specified commit

git commit --amend
# Modifies the most recent commit with a new message or additional changes
```

## 7. Synchronizing with Remote Repositories
```bash
git remote add origin [url]
# Adds a remote repository URL to your local repository

git fetch
# Downloads commits, files, and references from a remote repository

git pull
# Fetches and merges changes from the remote repository into the current branch

git push
# Uploads local repository content to a remote repository

git push origin [branch-name]
# Pushes the specified branch to the remote repository
```

## 8. Stashing Changes
```bash
git stash
# Temporarily saves changes that are not yet ready to be committed

git stash list
# Shows a list of stashed changes

git stash apply
# Applies the most recently stashed changes to the working directory

git stash drop
# Deletes the most recently stashed changes
```

## 9. Advanced Git Commands
```bash
git rebase [branch]
# Reapplies commits on top of another base tip

git cherry-pick [commit]
# Applies the changes from a specific commit into the current branch

git bisect start
# Starts the binary search for the commit that introduced a bug

git bisect good [commit]
# Marks a commit as good during a bisect session

git bisect bad [commit]
# Marks a commit as bad during a bisect session
```


"""
