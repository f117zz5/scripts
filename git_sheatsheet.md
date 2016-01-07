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
git br --set-upstream-to=[remotename]/[branch] [branch]
```
or a shorter forma
```
git br --set-upstream branch remotename/branch
```
Please note, after adding a remote, it should be fetched. Link [here](http://stackoverflow.com/questions/14717957/why-does-git-not-recognize-origin-master-as-a-valid-object-name)
```
git remote add remotename URL
git fetch remotename
 ```

ot the short-hand command just for tracking a branch
```
git checkout --track origin/daves_branch
```
Check if remote repository has been updated (if pull needed). Stackoverflow discussion [here](http://stackoverflow.com/questions/3258243/git-check-if-pull-needed)
```
git remote -v update
```
Rename a remote repository. Stackoverflow discussion [here](http://stackoverflow.com/questions/2432764/change-the-uri-url-for-a-remote-git-repository)
```
git remote set-url origin git://new.url.here
```

Delete a branch from the remote server. Stackoverflow discussion [here](http://stackoverflow.com/questions/2003505/delete-a-git-branch-both-locally-and-remotely)
```
git push origin --delete <branchName>
```
or
```
git push origin :<branchName>
```
Remove a reference of a deleted remote brunch. Stackoverflow discussion [here](http://stackoverflow.com/questions/6930147/git-pull-displays-fatal-couldnt-find-remote-ref-refs-heads-xxxx-and-hangs-up)
```
git remote prune origin --dry-run
```
First test the then remove the `--dry-run` to do the actual job.

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

## Stop tracking and ignore changes to a file in Git
Stackoverflow discussion [here](http://stackoverflow.com/questions/936249/stop-tracking-and-ignore-changes-to-a-file-in-git)
Just run
```
git rm --cached
```
on the file that should be removed. But this will also remove the files from the repository.

To keep the files in the repository, but not caring of them being changed anymore, do:
```
git update-index --assume-unchanged [path]
```

To see which files are --assume-unchanged:
```
git ls-files -v
```
Those are the one with lower letters.
One can also use (link [here](http://stackoverflow.com/questions/2363197/can-i-get-a-list-of-files-marked-assume-unchanged)):
```
git ls-files -v | grep '^[[:lower:]]'
```
or
```
[alias]
    ignored = !git ls-files -v | grep "^[[:lower:]]"
```


## Remove deleted files
Stackoverflow discussion [here](http://stackoverflow.com/questions/492558/removing-multiple-files-from-a-git-repo-that-have-already-been-deleted-from-disk)
```
git rm $(git ls-files --deleted) 
```

## Revert past already pushed erroneous commit
Stackoverflow discussion [here](http://stackoverflow.com/questions/2318777/undo-a-particular-commit-in-git-thats-been-pushed-to-remote-repos)
```
git revert hashtag -n 
```

## Compare different commits
Stackoverflow discussion [here](http://stackoverflow.com/questions/6944264/git-diff-show-only-diff-for-files-that-exist-in-both-commits)
Get the list of the altered files with status information showing what has changed.
```
git diff --name-status [HashTag1]..[HashTag2]
```
List only the modified files, not the deleted and added ones.
```
git diff --diff-filter=M [HashTag1]..[HashTag2]
```

## Git configuration
Set Notepad++ as a default editor in Windows. Stackoverflow discussion [here](http://stackoverflow.com/questions/1634161/how-do-i-use-notepad-or-other-with-msysgit/2486342#2486342)
```
git config --global core.editor "'C:\path_to\notepadpp\notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```