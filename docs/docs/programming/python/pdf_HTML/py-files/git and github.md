# what is Git ?
- version control system

# what is a version control?
- the management of changes to documents , computer programs or any other collection of information

# some terms
- **directory** : folder on my computer
- **CLI** : command line interface
- **cd** : change directory
- **code editor** : where you write a code document
- **repository** : folder where the project is kept
- **git** : the tool that tracks th changes on your device
- **github**: website that host repo

# git commands
- all commands are lowercase
- **clone** : bring repo that is hosted somewhere onto your local machine 
- **add** : track your files and change it on git (when you want git to apply the latest changes that you made on the repo)
- **commit** : save your files on git
- **push** : upload files on github (remote repo)
- **pull** : download changes from remote repo 

# what is a repository ?
- a repo is a project , collection of files that together forms a project

# cloning a remote repository 
- cloning is like *downloading* a repository from github
- we use `clone` command
**syntax** 
- `git` +  `clone` + `link of remote repo` 
```bash
# git clone _link of repo_ 
git clone https://github.com/MOSTAFA-DARSH/test.git
```
- we can use all link according to preferences 
- `ssh` : if we establish an ssh key for our github and git 
- `https` : most common for cloning using https

# how to know that my folder is a repository ?
- you will find `.git` file
- noticed that this file is hidden

# what going on !!! 
- getting notified about every thing in the local repo we use `git status` command
- it shows us the all files that are updated or created or deleted but not saved in a commit yet
```git
git status
```

# the next step  
- the next step is make commit to changes
- but before we commit the changes we need to inform git to <u>track the files</u> 
## track files
- to track files we need to use `add` command
```
git add .
```

# commit changes
- committing changes + adding messages allow the user to track these changes in an organized way
**syntax** 
- we use `git` + `commit` + `-m "message"` 
```git
git commit -m "this is my first commit"
```

# SSH
- alot of documentation

# making repository in my local machine and linking with remote

- now we can reverse the cycle 
- we can start making a repo on our local machine and pushing it to the github
<br>
- first we need to initialize a git repo on our local machine
- we use `git init` command
**syntax**
- `git` + `init` --> on the folder we want to make a git repo
```git
# making a git repo on the local machine
git init
```

- after creating our repo locally and creating files in it
- we need to connect the local repo with the remote repo
- we can create a remote repo and link them
- the easiest way is to create a remote repo is on git hub by GUI 
- then we use `git remote` command
**syntax**
- `git` + `remote` + `add` + `origin` +  `link for the remote repo`
```git
# linking remote repo with local repo
git remote add origin https://github.com/MOSTAFA-DARSH/test_2.git
```

- after we linked the remote with the local we now can push our changes through by using `git push origin master` 
# some terminology
- *origin* : the remote repository
- *master* : main branch we are working on 
# working with branches
## which branch
- if you noticed we are currently working on master branch 
- to ensure that we will run the command `git branch` 
**syntax**
- `git` + `branch`
```git
# getting the branch name
git branch
```
- output `* master` --> (`*`) means that we are working on that branch 
## creating a new branch
- creating a new branch is by command `git checkout _branch name_` 
```git
# creating a new branch
git checkout -b feature_1
```

## switching through branches
- we can merge both repos locally 
- we use `git merge` command
**syntax**
- `git` + `merge` + `repo1` + `repo2`
```git
# merging 2 repos
git merge repo1 repo2
```

## deleting a branch
- we use the `-d` option with `checkout` command
**syntax**
- `git` + `branch` + `-d` + `branch name`
```git
# deleting a branch
git branch -d feature_1
```
# pull 
- pulling changes from remote repo
> the pull is different from the clone
> _clone_ : download the repo
> _pull_ : get the updates in the remote repo

- we use command `git pull`
**syntax**
- `git` + `pull` + `repo` + `branch` 
```git
# pull request
git pull origin master
```

# how to undo changes in git
- undo staging --> use command `git reset`
**syntax**
- `git` + `reset` 
```git
# reset staging 
git reset
```

# how to undo a commit
- we can undo a commit by using `reset HEAD`
- lets focus on that
	1. `HEAD` : pointer to the last commit
	2. `HEAD~1` : undo the last commit (go one commit further --> undo the last commit)
**syntax**
- `git` + `reset` + `HEAD` 
```git 
# undo the last 2 changes (commit and add .)
git reset HEAD~1
```
- output --> <u>un-stage</u> and <u>un-commit</u> 
# see all commits
- by using command `git log`
```git
# see all commits 
git log
```
# un-stage and delete a commit
- we can grab a commit id and undo all commits at this point
## resetting only
**syntax**
- `git` + `reset` + `commit ID`
```git
# resetting a commit 
git reset ec393924878f4097117b513b6f914349393e3ba
```

## resetting and deleting
**syntax**
- `git` + `reset` + `--hard` +`commit ID` 
```git
# reset and delete a commit 
git reset ec393924878f4097117b513b6f914349393e3ba
```

# forks
- forks allow us to have copy of the repo and modify on it
##### why we do that when we have the repo ?
- we always have access to our repo BUT we do not have this full access to others repos 
- so we needs frks to copy others repos and modify on it









