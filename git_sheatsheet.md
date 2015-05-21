# Some examples
 
## Create bare repository on the server:

```
mkdir my_project.git
cd my_project.git
git init --bare
```
 
Then in the existing local repository one should add the remote repository that was 
just created. In this example the remote repository will be known in the local one as __master.
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