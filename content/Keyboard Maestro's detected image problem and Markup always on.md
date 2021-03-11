title: Markup Tools Always On and Keyboar Maestros Detected Image Problem
date: 08 Mar 2021 16:33
tags: productivity, Keyboard Maestro, automation
YouTube: 

I've been hoping to support more folks by creating Keyboard Maestro automations. I've been helping a few fellow podcasters. The latest request included an automation that makes the Markup menu in _Preview_ "Always On". 

To my knowledge, you can't make the Markup toolbar always available in Preview. You can, however, trigger the Markup toolbar based on state. 

## How did I do this? ##

This was a quick automation (my favorite type of automation).

It uses the _Found Image Condition_ to check if the Markup toolbar is enabled. If it is then do nothing. Otherwise, Trigger the hotkey. Have this automation fire whenever _Preview_ activates.

![update tags](../../../Desktop/Keyboard%20Maestro%20Detected%20Image%20Problem/75001D5E-C5BE-491E-B912-1DED5D5E41C1.tiff)

I then added a little delay (0.3 seconds) to make sure that the window had time to fully load.

## This worked! Until it didn't! ##

I was happy to see this working well but when I shared it, I got a very unexpected reply. 

> _This isn't working for me!_

What could be wrong with a three action command? I spent time troubleshooting and finally after getting a video from the requestor, I saw a big problem. They weren't using dark mode.

...

## This is a new problem ##

 The whole purpose of automation is that consistency is key. While there was a temporary solution to just create a version that likes light mode. But that's not an elegant solution. There should be a way to change what an icon would look like 

You can download the final version that supports both Light/Dark Mode via this [GitHub Gist](https://gist.github.com/kjaymiller/b4d8b33bfadb57a87b3247bf441ba72b#file-always-show-markup-window-kmmacros).