# Git Basics: Local Workflow Tutorial

This tutorial is designed for developers who are new to Git. We focus entirely on the **local workflow** to build a strong foundation before moving to remote collaboration (GitHub/GitLab).

---

## 1. Identity & Setup
Before you commit anything, Git needs to know who you are so it can attribute changes to the right person.

### Set your identity
```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"
```

### Useful Aliases
Aliases save time on common commands.
```bash
git config --global alias.s status
git config --global alias.lg "log --oneline --graph --all"
```

---

## 2. The Mental Model: The Three States
Understanding where your files "live" is the key to mastering Git.

1.  **Working Directory:** The folder on your computer where you are currently editing files.
2.  **Staging Area (The Index):** A "waiting room." You put changes here when they are ready to be snapshotted.
3.  **Local Repository (.git):** The permanent database of all your snapshots (commits).

---

## 3. Starting a Project
Every Git project starts with a "birth" command.

### Initialize a repository
```bash
mkdir my-project
cd my-project
git init
```

### Your first commit
```bash
# 1. Create a file
echo "# My Project" > README.md

# 2. Stage the file (move to waiting room)
git add README.md

# 3. Commit (create the snapshot)
git commit -m "Initial commit: Add README"
```

---

## 4. Monitoring Progress
The most important command in Git is `git status`.

### Check status
Always run this to see what Git is thinking.
```bash
git status
```

### See what changed
Before staging a file, see exactly what lines were modified.
```bash
# Edit README.md
echo "This is a local tutorial." >> README.md

# Check the difference
git diff
```

---

## 5. History & Navigation
Git keeps a detailed log of every snapshot you've ever taken.

### View History
```bash
# Basic log
git log

# Compact log (using our alias from step 1)
git lg
```

### Looking at old versions
```bash
# Look at a specific commit (replace <hash> with the code from git log)
git checkout <hash>

# Return to the latest version
git checkout main  # or 'master' depending on your default branch
```

---

## 6. Branching: Parallel Universes
Branches allow you to work on new features without breaking the "main" (stable) code.

### Create and switch
```bash
# Create a new branch
git branch feature-login

# Switch to it
git checkout feature-login

# Shortcut: Create and switch in one go
git checkout -b feature-profile
```

---

## 7. Merging & Conflict Resolution
Once your feature is ready, you bring it back into the `main` branch.

### Merging
```bash
git checkout main
git merge feature-login
```

### Handling Conflicts
If you changed the same line in two different branches, Git will stop and ask for help.
1. Open the file. Look for `<<<<<<<`, `=======`, and `>>>>>>>`.
2. Delete the markers and keep the version you want.
3. Save the file.
4. `git add <filename>` and `git commit` to finish.

---

## 8. Fixing Mistakes
Everyone makes mistakes. Here is how to fix them locally.

### Amend the last commit
Forgot to add a file or made a typo in the message?
```bash
git commit --amend -m "Corrected commit message"
```

### Discarding local changes
If you messed up a file and want to revert it to how it looked at the last commit:
```bash
git restore <filename>
```

### Unstaging a file
If you ran `git add` but changed your mind:
```bash
git restore --staged <filename>
```
