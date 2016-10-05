Title: The Git Adventure
Authors: Salvador Pérez
Date: 2016-09-23 21:20
Tags: Git, Tutorial


If you have ever tried to learn about git, you will probably
have faced the very same situation once and over again. There
are lots of posts and tutorials teaching the basics, and some
showcasing the advanced stuff. The first ones cover all the
basic operation without assuming any prior knowledge, while
the latter ones assume too much. there is not middle ground.


If this is your case, I'll try and put an end to that cycle.
If it's not, hey! I may save you the frustration!


Throughout this series of posts I will present you with
some practical exercises along with the bits of theory needed
to get to know every corner of this awesome tool, but first
things first. What is this git and why should you spend your
time learning it?


Git is a tool that achieves two purposes: On one hand it
provides a reliable way for people to collaborate in the same
software project. On the other hand it keeps track of all the
versions each file of the project has had. This provides, for
instance, a means to roll back all the changes made to a
project in case the last feature you implemented breaks
something.


## Prerequisites

For this tutorial you are going to need to have git installed.
You can do so by following
 [these instructions](git-scm.com/book/en/v2/Getting-Started-Installing-Git)

After having installed it, you will need to configure two things: Your
name and your email. These will be used by git to identify who made
every change in the code. To do so, you'll need to run these two
commands:

 + `git config --global user.name "Your Name"
 + `git config --global user.email "your@email.com"``

_The --global option is used to set those two data as the default for all
your git projects._

## Index

### Basics: Crafting the key to Wonderland

 + [Working forever alone]({filename}/Git/BasicI.md)
 + Interlude #1: Shit happens. Let's be prepared for it
 + Isolating your code
 + Bragging about your code
 + Enjoying other's code

### Intermediate: Down the rabbit hole

 + Interlude #2: Let's fix the world
 + It's not Magic but Science!
 + Let's share our skills with the world!
 + Can't someone else do it?
 + Best practices
 + The right merge for the right branch
 + Identify the culprit

### Advanced: Master your universe

 + Let's rewrite history!
 + Keeping your branches clean
 + Dodge the bullets; Heal the wounds
