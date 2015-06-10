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
after doing this I had to [set up the tracking explicitly](http://stackoverflow.com/questions/520650/make-an-existing-git-branch-track-a-remote-branch):
```
git br --set-upstream-to=remotename]/[branch] [branch]
```

ot the short-hand command just for tracking a branch
```
git checkout --track origin/daves_branch
```
Check if remote repository has been updated (if pull needed). Stackoverflow discussion [here](http://stackoverflow.com/questions/3258243/git-check-if-pull-needed)
```
git remote -v update
```

## Clean up

Stackoverflow discussion [here](http://stackoverflow.com/questions/61212/remove-local-untracked-files-from-my-current-git-branch)

First test it:
```
git clean -fd -n
```
And then remove all non-tracked files and folders:
```
git clean -fd
```

## Export

Stackoverflow discussion [here](http://stackoverflow.com/questions/160608/do-a-git-export-like-svn-export)
```
git archive --format zip --output /full/path/to/zipfile.zip master
```

## Remove deleted files
Stackoverflow discussion [here](http://stackoverflow.com/questions/492558/removing-multiple-files-from-a-git-repo-that-have-already-been-deleted-from-disk)
```
git rm $(git ls-files --deleted) 
```