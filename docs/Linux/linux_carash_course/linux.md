# file system in both windows and linux
- file system in **Windows** is organized as Folders  
- while in **Linux** files are ordered in tree structure , starting with root directory
- the root is the start of file system take notation of `/`  

![[Pasted image 20241212184534.png | center]]

## types of files in Linux
- everything in Linux is file devices is also files in Linux  
### General files
- also called `ordinanry files` 
- contains images, videos, programs
- have *ASCII* or a *Binary* format
- usually used (most common) 

### Directory files
- like folders in windows 
- but in Linux is also files
- in the file system we will find all files is stored in the root file 

### Device files 
- all devices are stored in the files , like printer, scanner which is located in the `dev` file

# Users in Linux
## 1. regular user
- regularly created by the creation of Linux
- have its own home file , which contains Desktop, Downloads, images, etc...
- regular user have no access to other users files

## 2. Root user 
- can access restricted files install software and has administrative privileges 

## 3. Service user
- a service user is not in the ubuntu regular version , its in the ubuntu server edition
- service users uses services on a server
- it helps to improve security 

# understanding shell 

![[Pasted image 20241212230010.png | center]]


# directory location
- we know the directory location by `pwd`
- `pwd` : print working directory
```bash
# using pwd
pwd
```

# Navigation
- if we want to navigate through files , we will use `cd`
- `cd` : change directory

- moving forward
```bash
# using cd 
cd ~/Desktop/file1
```

- moving backward
```bash
# maving backward
cd ..
```

### Navigate to home
- we use `~`
```bash
# navigate to home
cd ~
```

### Navigate to Root
- we use `/`
```bash
# navigate to root
cd  /
```


# Absolute and relative path
| Absolute path          | relative path                   |
| ---------------------- | ------------------------------- |
| the whole path to file | file by file                    |
| specify the full path  | we don't specify the whole path |

# listing
- we use `ls` command 
```bash
# listing files
ls
```

- there are different colors for files and directories (folders)
- in my distro , I have the directories highlighted with green , while files have green text color
## options 

- `-R` listing directories and sub-directories
```bash
ls -R
```

- `-a` show hidden files
```bash
ls -a
```

- `-al` long list `l` with hidden files `a`
```bash
ls -al
```

![[Pasted image 20241212232140.png | center]]

# Creating and Viewing files
- `cat` command used to 
	- copy 
	- Display
	- Combine 
	- Create text files

- how to use `cat` command
	- `cat` + `file` : show file content
	- `cat` + `>` + `file1` : writing in file called file1
	- `cat` + `file1 + file2` : concatenating files

```bash
# using cat
cat > file1.py 
print("hello world")
## we press (ctrl + D) to Exit the cat mode 

# concatenating
cat file1 file2 > file3

# showing conntent of file3
cat file3
```

# delete files
- we use `rm` 
- `rm` stands for remove
<br><br>
-  in some cases the file requires a privileged mode
- we use options like
	- `-r` : recursively 
	- `-f` : by force 

```bash
# deleting file
rm file1

# deleting file with privileges  
rm -rf file1
```


# Moving & Renaming files
## Moving files
- we use `mv` command 
- `mv`: stands for move 
- the `mv` command may require privilege , so we need to use `sudo`
<br><br>
**Syntax**
- `mv` + `file` + `location`

```bash
# using the mv command
mv file1 ~/Desktop

# with sudo
sudo mv file1 ~/Desktop
```

## Renaming files
- like the last command , instead of providing a destination we need to provide a new name 
<br><br>
**syntax**
- `mv` + `old_name` + `new_name`
```bash
# renaming files
mv file1 file_1.py
```

# Creating & removing directories
## creating directories
- we can create directories with command `mkdir`
```bash
# making directories
mkdir new_dir
```

- making directory in a new location
```bash
mkdir ~/Desktop/new_dir2
```

- making many directories 
```bash
# making many dir
mkdir folder1 folder2 folder3
```

## Removing Directories
- we use `rmdir` command 

```bash
# removing dir
rmdir test
```

>[!NOTE]
> - if we used the command `rm` , the command will return an error `cannot remove 'test' : Is a directory`
> - we can handle this by using option `-r` recursively 
> ```bash
> # remove directory by rm
> rm -r test
> ```

# man command
- `man` stands for manual 
- it returns manual page for any command in Linux 
- used by developers to know how to use any new command  
```bash
man man 
```

# finding history
- finding the history of command in the terminal 
- we use `history` command 
```bash
# finding the hsitory of teh commands
history
```

![[Pasted image 20241214173931.png  | center]]

- what really cool about this command that we can execute the any command in the history by using `!` 
```bash
# executing command 1998
!1998
```

- to execute the last command we usually type `!!` 
```bash
# executing the last command in the shell
!!
```

## Clearing terminal
- we type `clear`
```bash
# clearning terminal
clear
```

# File permission

- security is highly considered aspect in Linux where every file have an owner and have it's own permissions 
- so in term of security we will discuss **Ownership** and **Permissions** 
## Ownership in Linux
- every file have an owner 
- by default if a file was created the owner of this file is the user 
- owner & root user  are the people who decide which should use the file
### Users in Linux
1. owner of file
2. Group of users
3. other users
<br><br>
- <u>How to manage the usage of a file ?</u>
	- by using permissions 
## Permissions 
- we need to understand that we have 3 permissions in Linux [`r` , `w` , `x`]
	- `r` : allow user to read file
	- `w` : allow user to write/change the file  content
	- `x` : allow the user to execute the file
		- without this permission the file will not open in Linux
	- `-` : no permission

![[Pasted image 20241214175803.png | center]]
- **Let's see what it tell us**
	- each 3 characters represent permissions for a specific user
	- $1^{st}\ three\ char$ : represent the permission for the *Owner* 
	- $2^{nd}\ three\ char$ : represent the permission for the *Group of users --> called 'root'* 
	- $3^{rd}\ three\ char$ : represent the permission for the *Other Users* 
## Changing permissions
- we use the command `chmod`  
- we can use the command in 2 ways 
	- absolute
	- symbolic

### Absolute way
- we use numbers to express the permissions for each one

![[Pasted image 20241214202815.png | center]]

- we use 3 numbers each one represent the permission for a specific user/group 
```bash
# change the permission by absolute way
chmod 764 test.py
```

- the above command gives the Root user all permissions (read, write, execute)
- the group gets (read and write)
- while the user get read Only
### Symbolic way
- we use some notations to change the permission

![[Pasted image 20241214204313.png | center]]

- also we specify every user/group and specify the permission
- we can add permission to only one user or more 
	- we can add permissions to the group and Root user regarding of the users
	- we can remove permissions from the group users only 
	- if we gonna change mode to more than one user , we need to separate the modes by `,` 

```bash
# changing the mode for root 
sudo chmod u+rw- first.py

# changing the mood for group and others
chmod g-x,o-wx first.py
```

![[Pasted image 20241214222403.png | center]]

## Changing owner of the file 
- we use `chown` command 
```bash
# changing owner of the file
sudo chown root file1.py

## we changed the owner to root 
```

- changing the group
```bash
# change group
sudo chown root:root file1.py # we type owner(root):new_group(root)
```
- we changed the group from darsh to root 

![[Pasted image 20241214221018.png | center]]


# Groups
- as a user in Linux you must be related to a group
- to see all groups user is part in , we type `groups`

```bash
# see all groups
groups
```

- changing group , we use command `newgrp`
```bash
# changing group
newgrp dip
```

- now of we created a file , it will be owned by `dip` group

![[Pasted image 20241214225528.png | center]]

>[!NOTE] 
> - 2 groups cannot have the same file
> - a group can be sub-group of another , and have the same file

# Installing software
- in windows installing software is done by running launcher 
- the installation contains both program and independent components
<br><br>
- in Linux , installation files are distributed as packages , that contain only the program
- any dependent components will have to be installed separately  
- to install a program we run the command `apt-get`

```bash
# installing VLC
sudo apt-get vlc
```

# Redirection in Linux
- most commands have inputs and outputs 
- `stdin` standard input device is keyboard
- `stdout` standard output device is the screen

## Redirecting output in Linux
- we use `>` symbol
- this way is very useful in Linux , Saving information in files
```bash
# writing in a file
echo print\(\"hello world\"\) > file.py
```

- **concatenation**
	- we use `>>` to concat on a file content
```bash
# concatenating on a file
echo  pass >> file.py
```

1:14:25 -- > input redirecting