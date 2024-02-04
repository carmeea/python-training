## Git Introduction & Setup Python Environment

### Environment Prerequisits
1. Install Virtual Box - Download [here](https://www.virtualbox.org/wiki/Downloads)

   > _**Note:** For Macbook Apple Silicon (M series M1,M2, etc) Virtual Box is not compatible,  download instead UMT [here](https://mac.getutm.app/)_

2. Download Ubuntu Image (22.04 LST) - Official page [here](https://ubuntu.com/download/desktop)

3. Setup Ubuntu VM on VirtualBox 
- [Setup](https://www.youtube.com/watch?v=rJ9ysibH768) VirtualBox tutorial for Windows
- [Setup](https://www.youtube.com/watch?v=yL689oca4GA&t=923s) Virtual Box tutorial for Macbook Intel
- [Setup](https://www.youtube.com/watch?v=-TbilYal2_0) UTM tutorial for Macbook M series
  
4. Download and install VSCode on Ubuntu VM - [Official page](https://code.visualstudio.com/download) 
- Installation tutorial [here](https://www.youtube.com/watch?v=-WhRI9eBEYI)
  > _**Note:** For Macbook Apple Silicon (M series M1,M2, etc) please download VSCode - ARM64 package version._

5. Create a [github](https://github.com/) account (if you don't have already). 

### Installing Git and github account setup
- install git (from terminal) - first check it's not installed and follow steps
```bash
sudo apt update #first we waht to make sure we have latest apt version
sudo apt upgrade
git --version
sudo apt install git
git --version
```
- configure git (useful commands)
```bash
git config --global user.name "yourname"
git config user.name
git config --global user.email "email@address.com"
git config user.email
git config --list #view condfigured username and email
cat ~/.gitconfig # another way to view username and email
```
- Generate ssh-key for working with github. Use 'cat' command to display the public key. Copy the key to github
```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub #view generated public key
```
- Add public key to github account
  > Profile > Settings > SSH and GPG keys > Add new ssh key
- clone python-training repository using ssh key (terminal).
  > For learning purposes: using the terminal, we will make a 'work' folder, clone repository inside and open it with VS code.
```bash
mkdir work
cd work
git clone git@github.com:carmeea/python-training.git #clone repository using ssh
cd python-training
code . #opens VS Code in current directory
```

### Python Installation
- Ubuntu 22.04 comes preinstalled with python 3.10.12. To check version:
```bash
python3 --version
```
- install pip and upgrade
```bash
sudo apt-get install python3-pip
pip3 install --upgrade pip # to make sure you have latest pip version
pip3 —-version
```
- create alias for python3 and pip3. Open file bashrc
```bash
open ~/.bashrc
```
> Using file editor add following lines to bashrc and save changes.
```
# alias for python3
alias python=python3
# alias for pip3
alias pip=pip3
```
>Terminal windows must be reopen for changes to occur.
To verfy alias works, run in terminal following lines.
```bash
python —-version
pip --version
```

### Creating a Virtual Environment
Virtualenv helps you create an isolated python environment where you can install and manage project settings whitout polluting your OS environment.

Use commands bellow to install, create, activate and deactivate the virtual environment.
```bash
sudo pip install virtualenv
virtualenv venv #to create virtual environment named venv
source venv/bin/activate
deactivate
```

### Installing Black Formatter
Black is a [PEP8](https://peps.python.org/pep-0008/) compliant opinionated formatter. Black reformats entire files in place. PEP8 improves the readability and consistency of Python code. PEP stands for Python Enhancement Proposal.

To install black use command.
```bash
pip install black
```
To format files, you can use one of the folowing commands.
```bash
black {source_file_or_directory}
python -m black {source_file_or_directory} #another way to format files or directories
```
You can also install Black formatter extension and set it up as default formatter in VS Code.

### VS Code Setup

First time you work with python files in VS Code, you need to configure default settings (select the language interpreter, default formatter, etc). There are multiple ways to do this. We will use a simplistic method.

Setup python interpretor - Simple way to Configure Python default settings.
   > File > Preferences  > Settings -> search python interpretor
  
Black formatter extension - One way to configure black would be:
   > Modify a python file > Right-click menu > Format document with > Configure default formatter > Select Black formater

Format files when saving changes
   > File > Preference > Settings > Text Editor > Check Format on Save (sometimes it requires VSCode restart)