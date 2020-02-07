# How to start
​
### Have your git master walk you through these steps.
### Don't Do anything without your git master
​
### How to clone and start
- Make a directory where you want your cloned folder to live
- Cd into that directory
```
$ cd DirectoryName
```
- Clone the repo by copying the repo orgin
```
$ git clone https://github.com/username/repo-name.git
```
- Change into the cloned repo
```
cd repo-name
```
​
- Open vscode
```
$ code .
```
- Get your task from the git master
- Open the terminal in vscode
- Create a new branch
```
$ git checkout -b yourName-task
```
​
- Start coding!!
​
### During your coding time
- Finished a cool part
```
$ git add .
$ git commit -m "I added a really cool thing"
```
- Finished another cool part
```
$ git add .
$ git commit -m "I added another really cool thing"
```
​
### Done with code! Do this stuff!
​
- Go find your git master
- Push the code with your git master
- The following command will give an error saying there is no upstream. Copy and paste that code.
```
$ git push
```
​
- Walk, don't run to your git masters computer
> Git master controls this part!
- Go to branches
- Go to the current branch for the person that pushed
- Create a pull request
​
- Auto Merge!
  - Follow the green Buttons
  - Pull down the latest code to the git masters computer
  - Test The code on the git masters computer
```
$ git checkout master
$ git pull
```
- Conflict!
  - Resolve Conflict
  - Delete the code before the sources (====== and >>>>>>> symbols)
  - When the code is satisfactory you will be able to click mark resolved
  - Commit Merge
  - Merge Pull Request
  - Confirm Merge
  - Pull down the latest code to the git masters computer
  - Test the code on the git masters computer to make sure it all works
```
$ git checkout master
$ git pull
```
​
- Once everything works
  - Delete the branch on github
  - User and Git Master Go to the users computer
  - Switch to master and pull down lastest code
```
$ git checkout master
$ git pull
```
- Delete your old branch
```
$ git branch -d branchName
```
​
- Get a new assignment and create a new branch
```
$ git checkout -b userName-task
```


# App in a Day MVP
- UI / UX
- Pages
  1. NavBar 
  2. Homepage
  3. About
  4. Contact
  5. Footer
  6. Products
  7. Individual product
- Navbar
  - Needs logo
  - Links to every page
  - Mobile friendly
- Footer
  - Needs logo
  - Social links (link it to hash)
  - Links to every page
  - Mobile friendly
- Homepage
  - Open to you
- About
  - Open to you
- Contact
  - I want a contact form
  - It doesn't have to function
- Products
  - I want this data to not be hard coded in the html
  - You need to get your product information from the database
- Individual product
  - I should be able to click on a product and it should take me to that individual product page for more information.
  - It should have more information than before such as a description, price, manufactor, more pictures, etc.
- Database
  - Create a Shoe
  - Get a Shoe
  - Get all Shoes
  - Update a Shoe
  - Delete a Shoe
  - Flask app should render all the html via templates
Collapse































