# All  Linux & Git-GitHub Commands

If you want to download all Git command [click_here](https://github.com/RishikeshOps/90DaysOfDevOps/blob/43a29c7b9f747cecfa3d718258058e9341d4bce2/2023/day12/Git%20CheetSheet_1.pdf) or Shoot Me an [Email](mailto:rishikeshmashidkar@gmail.com) I will send you the Original Word File.


## **All About Linux**
### System administration:

- `uptime`: Shows how long the system has been running and the number of users currently logged in
- ```free```: Shows the amount of free and used memory in the system
- ```top```: Shows the running processes and their resource usage
- ```ps```: Shows the running processes
- ```kill```: Sends a signal to a process to terminate it
- ```lso```f: Lists open files and the processes that have them open
- ```netstat```: Shows network connections, routing tables, and interface statistics
- ```df```: Shows the amount of free space on a file system
- ```du```: Shows the size of a directory
- ```mount```: Mounts a file system
- ```umount```: Unmounts a file system
- ```chmod```: Changes the permissions of a file or directory
- ```chown```: Changes the owner and group of a file or directory
- ```useradd```: Adds a new user to the system
- ```userdel```: Deletes a user from the system
- ```passwd```: Changes a user's password
- ```crontab```: Schedules commands to be executed automatically

### Networking:

- ```ping```: Tests the reachability of a host
- ```traceroute```: Shows the route packets take to a host
- ```telnet```: Opens a telnet connection to a host
- ```nc```: Opens a network connection
- ```ssh```: Opens a secure shell connection to a remote host
- ```scp```: Copies files over a secure shell connection
- ```ftp```: Opens an ftp connection to a host

### File management:

- ```ls```: Lists the files and directories in the current directory
- ```cd```: Changes the current working directory
- ```mkdir```: Creates a new directory
- ```touch```: Creates a new file
- ```rm```: Deletes a file
- ```rmdir```: Deletes an empty directory
- ```mv```: Renames or moves a file or directory
- ```cp```: Copies a file or directory
- ```pwd```: Prints the current working directory
- ```cat```: Prints the contents of a file
- ```echo```: Prints a message to the console
- ```less```: Allows you to view the contents of a file one page at a time
- ```grep```: Searches for a pattern in a file or a stream of text
- ```sed```: Modifies the contents of a file using a script
- ```awk```: Processes text files and data streams
- ```find```: Searches for files and directories
- ```tar```: Creates and extracts archive files
- ```gzi```p: Compresses and decompresses files
- ```unzip```: Uncompresses archive files
- ```find```: Searches for files and directories
- ```locate```: Finds files by name
- ```which```: Shows the path of a command

### Process management
- ```ps```: Shows the running processes
- ```kill```: Sends a signal to a process to terminate it
- ```top```: Shows the running processes and their resource usage
- ```htop```: Interactive process viewer
- ```nohup```: Run a command immune to hangups, with output to a non-tty

## **All About Git-GitHub**

### Repository management:

- ```git init```: Initializes a new Git repository
- ```git clone```: Copies an existing repository from a remote location
- ```git remote```: Shows the remote repository
- ```git remote add```: Adds a new remote repository
- ```git remote remove```: Removes a remote repository
- ```git remote rename```: Renames a remote repository
- ```git remote set-url```: Changes the URL of a remote repository
- ```git remote -v```: Shows the remote repository and its URL
### Branching:

- ```git branch```: Shows the branches in the repository and indicates the current branch
- ```git branch -a```: Shows all branches, including remote branches
- ```git branch -r```: Shows only remote branches
- ```git branch -v```: Shows the last commit on each branch
- ```git branch [branch name]```: Creates a new branch with the given name
- ```git branch -d [branch name]```: Deletes the branch with the given name
- ```git branch -D [branch name]```: Force deletes the branch with the given name
- ```git checkout [branch name]```: Switches to the branch with the given name
- ```git checkout -b [branch name]```: Creates a new branch with the given name and switch to it
- ```git switch [branch name] ```: Create a new branch and switch to it
- ```git merge [branch name] ```: Merges changes from the branch with the given name into the current branch
- ```git rebase [branch name] ```: Reapplies commits from the current branch on top of the branch with the given name
### Committing:

- ```git status```: Shows the status of the repository
- ```git add [file name]```: Adds the file with the given name to the staging area
- ```git add .```: Adds all changes in the current directory to the staging area
- ```git reset [file name]```: Removes the file with the given name from the staging area
- ```git commit -m "[message]"```: Creates a new commit with the changes in the staging area and the given message
- ```git commit --amend -m "[message]" ```: amends the last commit with the changes in the staging area and the given message
- ```git commit --amend --no-edit``` : amends the last commit with the changes in the staging area and keep the same commit message
- ```git commit -a -m "[message]" ```: commit directly without staging the changes
- ```git log```: Shows the commit history
- ```git diff```: Shows the differences between the working directory and the last commit
### Reverting:

- ```git reset [commit hash]```: Reverts the repository to the state of the commit with the given hash
- ```git reset --hard [commit hash]```: Reverts the repository to the state of the commit with the given hash and discards all changes since that commit
- ```git revert [commit hash]```: Creates a new commit that undoes the changes made in the commit with the given hash

### Synchronizing:

- ```git fetch [remote name]```: Downloads new commits from the remote repository with the given name
- ```git pull [remote name] [branch name]```: Fetches and merges changes from the remote repository with the given name and the branch with the given name into the current branch
- ```git push [remote name] [branch name]```: Uploads commits to the remote repository with the given name and the branch with the given name
- ```git push -f [remote name] [branch name] ```: force push the commits to the remote repository with the given name and the branch with the given name
- ```git push [remote name] --all```: Uploads all branches to the remote repository with the given name
- ```git push [remote name] --tags```: Uploads all tags to the remote repository with the given name
- ```git remote prune [remote name]```: Remove branches that were deleted on the remote
- ```git pull --rebase```: This will integrate changes from a remote repository by reapplying your local commits on top of the updated remote head. This will avoid creating unnecessary merge commits
- ```git pull --rebase -X theirs``` : This will resolve merge conflicts by taking the version of the file from the remote repository
- ```git pul --rebase -X ours``` : This will resolve merge conflicts by keeping the version of the file you have locally

### Stashing:

- ```git stash```: Temporarily saves changes that are not ready to be committed
- ```git stash list```: Shows the list of stashes
- ```git stash apply [stash name]```: Applies changes from the stash with the given name
- ```git stash drop [stash name]```: Deletes the stash with the given name
- ```git stash pop [stash name] ```: Applies changes from the stash with
