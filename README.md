 ## Git/Linux Tutorial
###### Written by Oceane Andreis
===================

### 1st Step - Create a Folder/File and Fork & Clone our repository

#### Create a folder and a file
```bash
pwd                                // Let’s see where we are 
ls                                    // List all the folders/files of our location
mkdir  GitTutorial           // Create a folder(pick a place you feel comfortable with) 
cd GitTutorial                 // Go into that folder
touch  README.md      // Create a read me file
vim README.md	  // Edit read me file. Press i to insert, esc+:+wq    (wq = write quit)
rm README.md 	  // Remove our masterpiece
```
#### Fork the repository on github

#### Clone the repository in the folder you created

```bash
git clone https://github.com/Oceanestars/GIT-Linux-Tutorial.git
```
### 2nd Step - Push code

#### Pick a file and fix the error
Use a code editor to edit or you can use vim(use vim if you don’t have a code editor).

##### Instructions for vim(text editor in terminal)
```bash
vim nameoffile
```
It will opent vim in the terminal and you’ll see the file. 
You need to press ‘i’ on your keyboard to be able to edit it.
To save your work you have to press esc then ‘:’ and then type wq  (which mean write quit).
If you didn’t want to write to the file and you just wanted to read you can just do :q

#### Git commands (after you fixed the files and saved them)

```bash
git add . 
git commit -m “First Commit by yourname”
git push // this won’t work right away if you didn’t do the config
```

##### Config command(in your terminal it should tell you exactly what to do, follow those)
```bash
git config --global --edit
git commit --amend --reset-author
```
Now you can git push! 
Go check on your github your changes!

### 3rd Step - Create your branch and fix more errors from a different files

#### Create a branch
Tip: A big benefit to create branch is to unit test your code in the branch before you merge it with master

```bash
git checkout -b YourName 
```

#### Fix the errors in Homepage.html
Hint:  it says 3 errors, but technically you can only fix 2 in the code . The third one you have to add something to your folder .

#### Push your changes to your branch 
```bash
git status
git add .
git commit -m “ Fixed blabla”
git push --set-upstream origin nameofyourbranch 
git log
```
### 4th Step - Pull request
#### Go back to Github
It’ll say pull request click on that
### 5th step - Issue (Optional) 
#### Issue
I wrote an issue you can directly go and discuss it with me if you want.

### Was this too easy?
Next steps:
*  Read about git rebase
*  Read about git squash
*  Read about fixup
*  Read about git cherry picking


### GIT Commands
	*  git add .  → add all changed files in the staged area
	*  git commit - m “ Put something that reflects what you changed/created” →
	*  git push  → push your changes to the remote repository
	*  git pull  → Download the latest changes and integrate them into your project
	*  git status → Check which files have been stages or committed
	*  git branch → Check which branch you’re on
	*  git checkout nameofbranch → Move to nameofbranch
	*  git checkout -b nameofnewbranch → Create a new branch and check it out
	*  git clone link → Clone a repo 
	*  git init → make a directory a git repository  
	*  git log → print a log of your commits


### Linux Commands
	*   cd → Current directory
	*  pwd → Print working directory
	*  touch → Create a file
	*  mkdir → Create a directory
	*  vi name of file → Open and edit a file
	*  cat → Display content of a file
	*  ls → List everything in your current directory
	*  echo  $nameofwhatever→ Will print the path to whatever you want
	*  history → Will print the history of all of your shell commands
	*  man nameofterminalcommand → Will explain that command
	*  mv nameoffile location → Move file/directory somewhere else
	*  tar -xvf yourfile.tar → Extract tar file
	*  whoami → Find out who you are logged in as
	* rm nameofile → Remove name of file
	*  ls -a →  See hidden file(bashrc for example)
	*  tree →  See the hierarchy of your files
	*  find . -name "pattern" -print  →  Find specific files
 

### Resources
[Download Git](https://www.atlassian.com/git/tutorials/install-git "Download git") <br />
[Markdown Online Editor](https://markdown-editor.github.io/ "Markdown Online Editor") <br />
[Markdown Tutorial](https://guides.github.com/features/mastering-markdown/ "Markdown Tutorial") <br />
[Markdown Interactive Tutorial](https://www.markdowntutorial.com/ "Interactive Markdown Tutorial") <br />
[In Browser IDE](https://repl.it/ "In Browser IDE") <br />
[Oh my zsh](https://sourabhbajaj.com/mac-setup/iTerm/zsh.html "Oh My Zsh") <br />
[Homebrew](https://brew.sh/ "Homebrew") <br />
[Cmder](https://cmder.net/ "Console Emulator for Windows") <br />
[Update forked repo](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository "Update forked repo")<br />
[Great upstream explanation](https://stackoverflow.com/questions/37770467/why-do-i-have-to-git-push-set-upstream-origin-branch "Set Upstream for your branch explanation")





