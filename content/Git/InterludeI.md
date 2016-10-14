Title: The Git Adventure Interlude: Shit happens. Let's be prepared for it
Authors: Salvador Pérez
Date: 2016-10-14 19:31
Tags: Git, Tutorial

No matter how careful you are, when working with git you'll always end up doing
something you didn't intend to. In this interlude we are going to take a look
at the most common and easy to fix mistakes you may have faced by now.


### "Unstage" a file

Wether you did `git add` a file only to later realize it wasn't the right one
or you added a full directory but now want to unstage some of the files
it contains, git got you covered. The solution to this "mistake" would
be to use `git reset`.

Let's put it to practice. You can either use the same repository we used
in the first post or create a new one.

Let's create a file. It doen't matter if it's empty. In my case I'll
call it `foo`.

If we `git add foo`, the status of the repository will show this:

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   foo

Oh no!!! I didn't want to add it. Shame on me. Let's `git reset foo`.
The status of the repository will go:

    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

    	foo

And git just saved the day again!
(Remember, to check the status of the repository just run `git status`).


### "Uncommit" a file

This is another usual mistake. You recklessly thought all the files
inside a directory were good to go and commited it without checking it
further. Here we have two solutions depending on which case you are
facing:


##### I want to uncommit a new file

In this case you commited a file for the first time. In the previous
commit this file didn't exist. This is the easiest of the two cases.
The way to go here will be to store a copy of the file outside the
repository, tell git that you no longer want that file and once git has
removed it, move your copy back to the original place, so that git sees
it as a new file. Sounds like an awful lot of work. Maybe even complicated.
Let's put it to practice to see that it's not:

Let's add a new file to our repository.

    $ `git add foo` --> This will apply the staged status
    $ `git commit`  --> This will create a new snapshot of the code

Nice. Git knows abut the new file. Now we realize we don't actually want
that file to be commited yet. Let's undo it then!

    $ `cp foo ~/safe/place/foo` --> This will create a copy of the file
    $ `rm foo` --> This will actually remove the file
    $ `git add foo`
    $ `git commit`
    $ `mv ~/safe/place/foo foo`

Let's take a closer look at the last 3 lines.

- `git add foo`: This is a funny one. Here you are telling git to add the
  latest version of `foo` in the next snapshot. In this case it will
  mean to remove it from the repository, as the latest version is for it
  to not exist.

- `git commit`: As usual, for git to keep track of the changes you want
  it to keep track you need to make a new commit of it.

- `mv ~/safe/place/foo foo`: By just moving the file back again to the place
  where it was before git will see it as a completely new one. We
  understand and forgive it. I wish I will be able to do so many things as git
  when I am its age.


##### I want to uncommit the last changes to a file

This case is as straightforward as the previous one, but will introduce
a new git command. Forgive me for not explaining it in this post, but
I'd prefer to have a bit of context when explaining it. You won't have
to wait too long though. I'll explain it in the next one.

In this case we are taking a similar approach to the previous one. Let's
create a copy of the file, revert it to the previous version, and put
the latest one in place again (to not lose the changes). Let's do this!

    $ `cp foo ~/safe/place/foo` --> This will create a copy of the file
    $ `git checkout HEAD^ -- foo` --> This will revert the changes in foo
    $ `git add foo`
    $ `git commit` --> Now git has the previous version of this file
    $ `mv ~/safe/place/foo foo`


I hope these small tips have helped you with all of the issues you may
have faced by now (If not, leave me a comment and I'll be glad to reply
and add the solution to your problem to the post.

*If you have any question or any suggestion to make this series better,
please, comment in the box below, and I'll reply as soon as possible*
