## Working with Git

### HowTos in Git

How to view all remote and local branches
```bash
git fetch —all
git branch -r #view remote branches
git branch -a #view all remote and local branches
```
How to create a local branch from a remote branch
```bash
git fetch origin <remote-branch> 
git checkout --track origin/[remote-branch-name] #using the same remote branch name
git checkout -b local-branch-name --track origin/[remote-branch-name] #using a different local branch name
```

How to rebase your branch against master
```bash
git fetch origin
git remase origin/master
```

How to delete local and remote branches
```bash
git branch -d local-branch-name #delete branch locally
git branch -D local-branch-name # force delete local branch
git push origin --delete remote-branch-name #delete branch remotely
```