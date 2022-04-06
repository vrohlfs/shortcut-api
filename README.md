# Shortcut (formerly Clubhouse) API

This module is a Python client library for The Shortcut project management platform API

**Shortcut (formerly Clubhouse)** is collaborative project management that streamlines and refines your existing workflow. The intuitive and powerful project management platform loved by software teams of all sizes. [Shortcut](https://shortcut.com/) is here.


**API documentation** [https://clubhouse.io/api/rest/v3/](https://clubhouse.io/api/rest/v3/)


## Usage

You can generate a token for shortcut by going to the account section and generating a new token

```python
TOKEN = os.getenv('TOKEN')

shortcut_session = Shortcut(TOKEN, 'v3')
shortcut = shortcut_session.get_api()
```

## Example

Create a new Story in a specific Epic that is returned from the API in the all epics list.


```python
from shortcut_api import Shortcut
import asyncio
import os

TOKEN = os.getenv('TOKEN')

shortcut_session = Shortcut(TOKEN, 'v3')
shortcut = shortcut_session.get_api()

async def main():

    all_projects = await shortcut.projects()
    first_project_id = all_projects[0]['id']

    # get all epics and assign the epic id for the specific epic the new story will belong to. This example: 'First Epic'
    all_epics = await shortcut.epics.get()
    for epic in all_epics:
        if epic['name'] == 'First Epic':
            first_epic_id = epic['id']
    
    # create new story and assign to the Epic found above
    new_story = {'name': 'My new story', 'epic_id': first_epic_id, 'description' : 'This is a story written via API' }
    story = await shortcut.stories.create(**new_story)
    print(story)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```


## Contributing

Bug reports and/or pull requests are welcome

