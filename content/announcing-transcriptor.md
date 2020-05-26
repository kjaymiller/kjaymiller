title: Announcing Transcriptor
date: 25 May 2020 22:32


_This was the launch month for [Transcriptor]. This is a helper package that I use for doing transcriptions for PIT Clients._

Transcriptions can be accomplished in a plethora of ways, but in order to do it, you need to have a good idea of how to work with the results from your transcription engine. While I usually use [Amazon Transcribe], I have used [Google Could Services Speech to Text] and I would love to look into the [Microsoft Azure] and [Wit.Ai]. All of these systems use their own schema for your task and your results.

The goal of transcriptor is to create a single Job object that is responsible (currently) for handling the results in a consistent object-oriented way. By using it, I've been able to create some clarity in my coding projects for folks and reduced the amount of copying and pasting across the board.

**FAQ:**

* _Can you use it?_ **At your own risk, sure.**
* _Is it documented?_ **Not Yet**
* _Is it stable?_ **I wouldn't say that...**
* _Is it open source?_ **Of course it is!**
* _Am I accepting contributions_ 
 
I am accepting testing and documentation PRs, I'm also looking at incoming issues and If you have a fix (Not a Feature Request), I will accept after testing and reviews.

[Transcriptor]: https://pypi.org/project/transcriptor
