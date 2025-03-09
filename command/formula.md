### Formula

```
# get feed from repo-url
IF(ISNUMBER(SEARCH("release", [subscribe])), CONCATENATE([url], "/releases.atom"), IF(ISNUMBER(SEARCH("commit", [subscribe])), CONCATENATE([url], "/commits.atom"), ""))
```