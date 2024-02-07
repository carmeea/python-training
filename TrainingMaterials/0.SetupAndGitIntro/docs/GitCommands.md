## Git Introduction
Git is a DevOps tool used for source code management. It is a free and open-source version control system used to handle small to very large projects efficiently. Git is used to track changes in the source code, enabling multiple developers to work together on non-linear development.

Git Useful Links
- [Git Tutorial: 10 Common Git Problems and How to Fix Them](https://www.codementor.io/@citizen428/git-tutorial-10-common-git-problems-and-how-to-fix-them-aajv0katd)
- [Common mistakes](https://ohshitgit.com/)
- [Sandbox GIT](https://learngitbranching.js.org/)

## Git Workflow
![GitWorflow](/Assets/gitworkflow.jpg)

### Git Roadmap
- git clone - clone repository
- git checkout - move to another branch
- git pull - update branch
- git branch - view branches
- git status - view changes on curerent branch
- git stash - save shanges
- git add - add changes before commit
- git commit - commit changes
- git push - push changes remote
- git cherry-pick - select changes
- git merge - merge changes
- git branch delete - delete branch
- git diff - view diferences between branches
- git log - view commits
- git blame - who did changes on a file
- git reflog - list of changes from all branches

### HowTos in Git

How to view all remote and local branches
```bash
git fetch -—all #fetch all branches from all remotes
git branch # view local branches 
git branch -r #view remote branches
git branch -a #view all remote and local branches
```
How to view pretty logs
```bash
git log --pretty=oneline --abbrev-commit
git log --oneline #short version of command above
```

How to create a new branch
```bash
git branch local-branch-name #creates branch from branch you were on, does not switch to it
git push -u origin local-branch-name #push branch remote
```

How to create a local branch from main and push to remote
```bash
git checkout main
git checkout -b local-branch-name # create branch and switch to it
git push --set-upstream origin # or push the current branch and set the remote as upstream
```

How to create a local branch from a remote branch
```bash
git fetch origin <remote-branch> 
git checkout --track origin/[remote-branch-name] #using the same remote branch name
git checkout -b local-branch-name --track origin/[remote-branch-name] #using a different local branch name
```

How to add changes and commit
```bash
git status
git add .
git commit -m "message"
git push
```

How to add changes to last commit
```bash
git commit —amend -m "message"
git push —force
```

How to rebase your branch against master
```bash
git checkout local-branch-name #if you are not already on it
git fetch origin
git rebase origin/main
```

How to save or stash changes
```bash
git stash -u # git stash --include-untracked stash untracked files.
git stash -a # git stash --all stash untracked files and ignored files
git stash list # view your stashes,stashes are saved in a last-in-first-out
git stash clear # empties the stash list by removing all the stashes.
git stash drop <stash_id> # deletes a particular stash from the stash list.
```

How to soft cancel commits
```bash
git revert HEAD —no-edit # git revert HEAD
git push
```

How to delete changes
```bash
git reset —hard [HEAD~2 or c87a087] # deletes changes
git reset —soft [HEAD~2 or c87a087] # needs only to commit
git reset [—mixed][HEAD~2 or c87a087] # needs add and commit
```

How to view changes in time from all branches
```bash
git reflog
```

How to view who changed a file
```bash
git blame -L <start_line>,<end_line><filename>
# ex: git blame -L 7,8 README.md
```

How to delete local and remote branches
```bash
git branch -d local-branch-name #delete branch locally
git branch -D local-branch-name # force delete local branch
git push origin --delete remote-branch-name #delete branch remotely
```
