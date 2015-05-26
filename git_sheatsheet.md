# Some examples
 
## Create bare repository on the server:

```
mkdir my_project.git
cd my_project.git
git init --bare
```
 
Then in the existing local repository one should add the remote repository that was 
just created. In this example the remote repository will be known in the local one as _master_.
```
git remote add origin URL
git push origin master
 ```
Please note, that in windows the path should be defined as c:/Path/my_repo.git
 
change the URL of a remote repo:
```
git remote set-url origin New_URL
```
 
push all tags:
```
git push --tags
```
 
push a single tag:
```
git push origin <tag_name>
```

## Check out additional remote repository to a local branch
Stackoverflow discussion [here](http://stackoverflow.com/questions/9537392/git-fetch-remote-branch).

```
git checkout -b [branch] [remotename]/[branch]
```
ot the short-hand command just for tracking a branch
```
git checkout --track origin/daves_branch
```