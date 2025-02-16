### [git](https://git-scm.com/)

```sh
git config --global user.email "user@email.com"
git config --global user.name "username"
```

#### Undo and re-push

```sh
git fetch --all
git reset --hard <commit-hash>
# git reset --hard HEAD~1
git push --force origin <branch>
````