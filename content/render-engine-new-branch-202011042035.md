Render Engine Beta 0.2 (AKA version 2021) will see a much cleaner and expressive version of the framework.

The biggest change is that the `Engine` will be be responsible for generating pages instead of the `Site`. In fact `Site` be replaced and become a holder of global variables named `SITE_VARIABLES`.

Here is a breakdown of the new engine scheme for Render Engine.
### Functionality from `Site` will be moved into Engine
- Pages will be created on instantiation
- `render` method will be removed


**NOTES**
------
Site Objects have been growing very wild as of late with the introduction of search modules.