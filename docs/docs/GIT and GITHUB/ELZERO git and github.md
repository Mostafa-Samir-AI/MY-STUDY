# workflow

![[Pasted image 20250407170100.png | center]]

# Cloning 
- we clone a remote repo in our local machine
- we use `git clone` + link
```bash
# copying a remote repo 
git clone https://github.com/MOSTAFA-DARSH/rrepo.git
```

# Local REPO
- most of the commands will work in the local repo

## Initialize local repo
- we Initialize local repo by using `init` command
```bash
# Initialize repo
git init
```
## checking file status
- we use command `status`
```bash
# checking status
git status 

# short command
git -s
```
## Tracking file (Stagging)
- adding file to stagging area
- we use `git add` + `file`
```bash
git add OCR.py
```

## Untracking File (Unstaging) 
- we remove the file from the stagging area
- we use `reset head`
```bash
# un tracking a file
git reset head OCR.py

# another command
git restore --staged OCR.py
```

## Removing files
- we use `clean` command and its options 
- only works on the un-staged files
### see what files will be removed
- we use `clean -n`
```bash
# list of files that will be removed
git clean -n
```

### removing files
- we use `clean -f`
```bash
# removing files
git clean -f
```

# Undo commit
- if we need to undo a commit we need to reset the head to previous commit 

# Remote REPO
## Submitting changes
- after committing changes in the local repo we submit changes to remote REPO
- we need to know the branches names
	- for local `git branch`
	- for remote `git remote -v`
- then we push changes by using `push` command
- `git push` + `remote branch name` + `local branch name`
```bash
# submitting changes
git push origin main
```

>[!tip] note
> - when working on mega project we use option `-u` in the `push` command
> ```
> git push -u origin main 
> ```
> - `-u` importance is used to first pull changes from remote repo to your local and then push all changes

## Pulling changes
- we can pull changes in the remote REPO by using 2 commands
	1. `git fetch` : to pull all changes in the remote REPO
	2. then `git pull` : to merge all changes in in local to working directory
		- only pull changes , we gonna use `merge` later 
### 1. using fetch
```bash
git fetch origin
```
### 2. using Pull + Merge
```bash
# pulling changes
git pull origin

# merging
git merge 
```

# Configurations
- list of all configurations
```bash
# list of all config
git config -l
```

- documentation of the git
```bash
# Documentation of git
git help config
```

- show the origin of commands
```bash
git config -l --show-origin
```

- user name
```bash
# see user name
git config --global user.name

# set new value for username
git config --global user.name "mostafa"
```

- email
```bash
# see user name
git config --global user.email

# set new value for username
git config --global user.email "mostafa@gmail.com"
```

- modify config with editor
	- we can change colors of status
```bash
git config --global --edit
```

# SSH
- generating SSH key will skip many steps of login 
```bash
# generaating SSH key
ssh-keygen -t rsa -b 4096 -C "mostafa@gmail.com"
```
- 2 files are generated `id_rsa` and `id_rsa.pub`
- the second file `id_rsa.pub` (public) is one we will use to pair the git and Github 
- we go to `settings` >> `SSH and GPG Keys` >> `add new key` 
- we name the new key and add the value we copied from the `id_rsa.pub` 
<br><br>
- we need to check the key was successfully added
- we do 
```bash
# check the validity of SSH key
ssh -T git@github.com
```
- out `Hi Mostafa-Samir-AI! You've successfully authenticated, but GitHub does not provide shell access.`

# Linking remote with local
- `git` + `remote` + `add` + `remote branch name` + `ssh` or `http` link
```bash
# linking remote with local
git remote add origin git@github.com:MOSTAFA-DARSH/my-repo.git
```

# pull request
 - when working on a project , with a lot of developers
 - we may work on with another developers with in the same feature
 - my our code cause conflict to other , so we use pull request
 - we create a request where we ask the admin (Github repo admin) to accept our changes to the project 
 - if there is any conflicts the admin will deny the request 
 - if not the admin will accept the request 
 - watch <a href = "https://youtu.be/n43bagVuJPU?si=jBUtagEHIPfYrST7 ">pull request</a>

# Alias
- alias is used set a nickname to a command 
- always save time when using long commands
- Creating alias
```bash
# creating an alias
git config --global alias.st status
```
- creating an alias for long command
```bash
git config --global alias.edit "config --global --edit"
```

# Branches
### See the current branch
- we use `git branch`
```bash
# finding current branch
git branch
```

### See remote Branch
```bash
git remote -v
```

### Creating a branch
```bash
# creating a branch
git branch dev
```

### Deleting a branch
- you need first to switch away from the branch
```bash
# deleting a branch
git branch -d dev
```

### Creating and switching to a new branch
```bash
# create and switch
git checkout -b dev
```

### Renaming branch
```bash
# rename 
git branch -m development
```


# Stash
- stash is used to hide files before we commit it 
- we store files to make further modification , when we done we make commit 
- only work is the files are stagged 

### Adding file to the stash

```bash
# making new files
echo "hello world" > next.txt

# staging 
git add newxt.txt

# checking status
git status # it will show that next.txt is yet not commited 

# hiding the file 
git stash next.txt
```


### removing the file from stash
- we can remove the file from the stash by command `pop`
```bash
# removing from stash
git stash pop
```

### Adding stash message
```bash
git stash -m "adding new file"
```

### list of all stashes
```bash
git stash list
```

### Apply vs pop
- apply fetch the files from the stash and leave the stash as it is
- pop retreat the files from the stash and delete the stash

```bash
# using apply
git stash apply
```
- removing a specific stash 
```bash
# removing a specific stash
git stash pop "stash{0}"
```
### Differences
- to see what is inside a stash, we use `show` command and specify the stash
```bash
# show differences 
git stash show "stash{0}"
```

```bash
# show full difference between stash
git stash show -p 
```
