# Some examples
 
## Create bare repository on the server:

```
mkdir my_project.git
cd my_project.git
git init --bare
```
 
then in the existing local repository
```
git remote add origin URL
git push origin master
 ```
 
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