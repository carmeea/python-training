## Git Introduction and Setup Python Environment on Ubuntu VM

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
sudo apt update
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
git config --list
cat ~/.gitconfig
```
- Generate ssh-key for working with github. Use 'cat' command to display the public key. Copy the key to github
```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub
```
- Add key to github account
> Profile > Settings > SSH and GPG keys > Add new ssh key
- clone python-training repository using ssh key (terminal).
> For learning purposes: using the terminal, we will make a 'work' folder, clone repository inside and open it with VS code.
```bash
mkdir work
cd work
git clone git@github.com:carmeea/python-training.git
cd python-training
code .
```

### Python Installation
- ubuntu comes with python 3.10.12 preinstalled. To check version:
```bash
python3 --version
```
- install pip and upgrade
```bash
sudo apt-get install python3-pip
pip3 install --upgrade pip
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
>Terminal windows must be re-open for changes to work.
To check alias works run in terminal following lines.
```bash
python —-version
pip --version
```

### Creating a Virtual Environment

### Installing Black Formatter

### VS Code Setup