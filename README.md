# youtrack-api-powerpack
A collection of Jetbrains' YouTrack API scripts

## Installation
You can install via pip as follows

```sh
pip install -U youtrackpowerpack
```

## Setup
Create a .env file into your project root with the following

```sh
YOUTRACK_ENDPOINT='http://yourdomain.myjetbrains.com/youtrack'
YOUTRACK_USERNAME='apiuser'
YOUTRACK_PASSWORD='letmegetin'

ASANA_PERSONAL_ACCESS_TOKEN='YOUR_TOKEN_GOES_HERE'
NOTIFICATION_EMAIL='boss@example.org'

MAIL_DRIVER='mandrill'
MAIL_HOST='smtp.ofmandrill.com'
MAIL_PORT='587'
MAIL_USERNAME='mailformandrill@mail.com'
MAIL_PASSWORD='myhashpassword'
MAIL_FROM_ADDRESS='myfrommail@mail.com'
MAIL_FROM_NAME='My From Mail name'
MAIL_TLS=None

MAIL_DEPLOY_CC='email_copy@mail.com; email_copy2@mail.com'
MAIL_DEPLOY_TO='to@mail.com; to_other@mail.com'
MAIL_DEPLOY_SUBJECT='[Deploy subject] Released version {{release_tag}}.'
MAIL_DEPLOY_MANDRILL_TEMPLATE='mandrill_template_name_for_deploy'

MAIL_VERIFY_CC='email_copy@mail.com; email_copy2@mail.com'
MAIL_VERIFY_SUBJECT='[Youtrack subject] Tasks not verified of release {{release_tag}}.'
MAIL_VERIFY_MANDRILL_TEMPLATE='mandril_tasks_to_verify_template'

MAIL_BRANCH_VERIFY_CC='email_copy@mail.com; email_copy2@mail.com'
MAIL_BRANCH_VERIFY_SUBJECT='[Branch verify subject] branches out of pattern for youtrack'
MAIL_BRANCH_VERIFY_MANDRILL_TEMPLATE='mandrill_template_branch_task_verify'

MANDRIL_APIKEY='myHashApiKey'
```

## Basic Usage
A basic example of how shoot an email
```python
#!/usr/bin/env python
from youtrackpowerpack import semver

try:
    semver.check('the_repo_path')
exception:
    semver.notify(e)
```

## Main features

