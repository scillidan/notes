# [Weblate](https://weblate.org) (Cache)

````{tab} Ubuntu 22 ARM [^1]
```sh
sudo apt install -y \
   libxml2-dev libxslt-dev libfreetype6-dev libjpeg-dev libz-dev libyaml-dev \
   libffi-dev libcairo-dev gir1.2-pango-1.0 libgirepository1.0-dev \
   libacl1-dev libssl-dev libpq-dev libjpeg-dev build-essential \
   python3-gdbm python3-dev python3-pip python3-virtualenv virtualenv git
```

```sh
sudo apt install -y \
   libldap2-dev libldap-common libsasl2-dev \
   libxmlsec1-dev
```

```sh
sudo apt install -y nginx uwsgi uwsgi-plugin-python3 redis-server postgresql postgresql-contrib exim4 gettext
```

```sh
sudo apt-get install git-svn
```
````

[^1]: [Installing on Debian and Ubuntu](https://docs.weblate.org/en/latest/admin/install/venv-debian.html)
[^2]: [Mercurial](https://docs.weblate.org/en/latest/vcs.html#vcs-mercurial)
[^3]: [Gerrit](https://docs.weblate.org/en/latest/vcs.html#vcs-gerrit)