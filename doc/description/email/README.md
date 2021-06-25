# README

this is a simple email sending program, providing two ways: SMTP and SMTP SSL abstract modules with dev version.

- [One. preconditions](#one-preconditions)
- [Two. the email config](#two-the-email-config)
  - [2.1 smtp config](#21-smtp-config)
  - [2.2 smtp ssl config](#22-smtp-ssl-config)
- [Three. usage](#three-usage)
- [Four. explain](#four-explain)

## One. preconditions

- only plain text email is supported

## Two. the email config

the please create a new `conf` folder in the current project directory, Then create a new `email_config.cfg` or `email_ssl_config.cfg` file

```bash

- this your project root
| - .
| - ..
| + conf
|    - email_config.cfg         // smtp config files
|    - email_ssl_config.cfg     // smtp ssl config files
|
| + src
|    + ...
|
| + tests
|    + ...
|
| - .gitignore
| - LICENSE.txt
| - MANIIFEST.in
| - pyproject.toml
| - README.md
| - setup.cfg
| - setup.py
| - tox.ini
| ...

```

> since the `conf` folder contains private information, please add the directory to the .gitignore file.

### 2.1 smtp config

```bash
# set up server
mail_host = smtp.xxx.com
# server default port that is 25
mail_port = 25
# user name
mail_user = xxx@gmail.com
# password
mail_pass = your_password_or_token
# sender
mail_sender = xxx@gmail.com
sender_alias = sender_alias
# receiver
mail_receiver = yyy@163.com
receiver_alias = receiver_alias
```

### 2.2 smtp ssl config

```bash
# set up server
mail_host = smtp.xxx.com
# server default port that is 465/994
mail_port = 465
# user name
mail_user = xxx@gmail.com
# password
mail_pass = your_password_or_token
# sender
mail_sender = xxx@gmail.com
sender_alias = sender_alias
# receiver
mail_receiver = yyy@163.com
receiver_alias = receiver_alias
```

## Three. usage

```python
# -*- coding:utf-8 -*-

from com.dvsnier.email.email import Email

email = Email()
# smtp cfg file
email.config_file('conf/email_config.cfg')
# smtp ssl cfg file
# email.config_file('conf/email_ssl_config.cfg')

# true is smtp ssl way, otherwise smtp
email.init(True)
# email.init()

email.builderText('subject', 'content')
email.sendmail()
email.quit()
```

## Four. explain

since it is only a `development version`, `only text mode` is provided at present, and the attachment of multimedia mode is supported in the future
