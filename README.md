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

