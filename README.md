# WebApp   
_This will be a project for learning how to develop a Python WebApp using Flask_   

---   
## Terms
* **Repository _(repo)_** : _storage location for software code_
* **Git** : _Software Code "version control"; a tool used for tracking changes while developing/writing code._
* **GitHub** : _An internet based service (website) for managing repositories: sharing code with others, tracking bugs/errors, working on code with others, etc._
* **URL _(Uniform Resource Locator)_** : _A website link/address._
* **IP Address (Internet Protocol)** : _a special "address" that every computer gets when connected to the internet (or network). Example: 192.1.168.1._
  > NOTE : URL/Website names are just text-based (letters) to represent an IP Address (an address to a computer on the internet. For example: http://www.google.com) 
* **Operating System _(OS)_** : _The software that controls how a computer works such as how it saves information and how tools like apps work on it. Example: Microsoft, Linux, Mac OS, etc._
  > NOTE: A mobile OS is just an OS for a phone or a tablet lik Android or iOS.
* **Raspberry Pi** : _A small computer that runs on a linux OS._
* **Terminal** : _A window to control a computer with a linux OS. When computers were first made there was no mouse and no way to do things such as move, create, or delete files on a screen, so you had to write commands with the terminal._
* **Directory** : _A folder on a computer; a place where files or other folders can be saved._
* **Web Browser** : _The software tool to view websites; examples of web browsers: Google Chrome, Chromium, Internet Explorer, FireFox, etc._

___
## Git Commands
* **git clone** : _copies all the code in a repository from a url_
* **git status** : _gets the current local status of your repo; if things are saved or not on your computer (**not on the internet**)_
* **git add** : _adds one or more files to a list to save locally_
* **git commit** : _saves all the added changes of what changes that have been added using:_
* **git push** : _takes all the committed changes/updates and sends them to github (to the interenet)._
* **git pull** : _goes to github to get the latest chnges/updates and updates your local repo (on your computer)._

  ### Steps to _"Pull the latest changes & run"_:
  1. Open Terminal on the Raspberry Pi
  2. Navigate into your Repo directory/folder
  3. Pull the latest changes with the following command:   
     `git pull`
  4. Run the following command to start the WebApp:    
    `python FlaskWebApp/run.py`   
     > NOTE : If your WebApp is already running, you can press CTRL+C in the terminal to force it to stop. If you do not run the webapp, it will not appear in the browser (Chrome).
  5. The IP Address/URL for the WebApp shold be in the terminal after running the last command. That can be copied and pasted into the browser to view the webapp for testing. You can also type in this URL to view the WebApp:
  `localhost:5000`  

  ### To update/change code or add new files to the Repo:
  1. Make changes or add any new file.
  2. Run the following command to add to the list of files to be tracked by git:   
    `git add --all`
  3. Commit the changes to the git tracking locally:  
   `git commit -m "adding new changes"`   
     > NOTE : The Quotation Marks suround the note you want to put when saving any updates/changes to the repo. You can change it to match what makes sense for you.     
  4. Push all the locally made changes to github:   
   `git push`
