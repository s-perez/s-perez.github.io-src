Title: The Git Adventure: Working forever alone
Authors: Salvador Pérez
Date: 2016-10-02 22:07
Tags: Git, Tutorial


Welcome to the first part of the git adventure series. This time
we're going to learn and use the most basic commands and the theory
needed to work offline in your own project.

### Starting a new project

Git includes a sub command, `git init` to start a project. Create a
new directory and run it. Don't worry, I'll wait.

Good. You will see a new folder named `.git` has
appeared. That folder holds all the magic that git can offer, but we'll
dig into that in another post. By now, it's enough to know that the
presence of that directory tells git this is a git project (what is
usually called a `repository`).


### Checking the status of the project

Well, we all knew that sooner or later we would have to deal with some
theory about git. Get comfortable: this will be an important but
rather lightweight part.

Put in a very simplified manner, git works by taking snapshots of the
code whenever you ask him to and assigning each of them a unique
identifier. These snapshots are called `commits` in the git jargon.
But it gives you more control than only choosing when to make a new
commit. It also lets you choose which changes you want to include in
the commit. This leads to the next bit of info.

In a git repository every file can be in one of 4 states: untracked, staged,
commited and modified

 - **Untracked** </br>
   git is like a responsible magic apprentice. He won't touch any new
   toy you bring to the lab until you give explicit permission and
   assure him it is safe to play with. In this metaphore the new toy
   is a file you just created. That file will be in untracked state
   until you say otherwise, and while it is in this state, git will
   ignore it.

 - **Staged** </br>
   Every time you tell git to include a file you just created, or the
   last version of a file that was already in the respository in the
   next commit, the file goes to this state. Think of it like telling
   git what do you want to include in the next commit.

 - **Unmodified** </br>
   Once you have added a file and created a new commit, the files you
   commited will go to this state. It simply means that the version
   contained in the last commit is the current version.

 - **Modified** </br>
   Well... The name says it all. If you make a commit including the last
   version of a file and then change it... well... it's modified.

Ok, That's all the theory you'll need for the rest of the post. Let's
get to work!

git comes with a subcommand to check the status of all the files of the
repository, `git status`. if you run it in your newly created
repository, you will see something like this:

    On branch master

    Initial commit

    nothing to commit (create/copy files and use "git add" to track)

Which basically means you don't have anything there for git to use
(let's forget about the "branch master" part. We'll talk about that soon,
but not today. Let's try creating an empty file in the project. If
we run `git status` again, we'll see this:

    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

    	foo

    nothing added to commit but untracked files present (use "git add" to track)


Nothing surprising here. We've created a file (in my case it's called foo),
so it will automatically be classified as `Untracked`. Good, good.


### Adding a file to the repository

As with everything we've seen up until now (and everything we'll see
from now on), this is achieved by using another subcommand. I'll let you
try and guess which one.

If you were thinking on `git add`, then you already know more about git
than you thought. Congratulations!

so... How does this subcommand work? Easy. You can call it passing a
file or folder you want to add to the repository, and git will mark
those as staged. If you are a terminal ninja, you can also pass a glob,
and git will add all matched files. Let's see an example of every use.


#### Adding a single file

Keeping with the same repository we created before, let's run `git add
a`. It seems that nothing is happening, but if we run again `git status`
we'll see that git has marked this file as `staged`:

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   foo


Look at that!
Git is recognising that our empty file is now in the repository (or will
be the next time we make a commit)


#### Adding a directory

Let's start creating a directory in our repository. `mkdir new_dir` will
do. Let's check the status of the repository:

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   foo

Wow, wow, wow... The directory isn't showing... And it's expected. Git
takes care of files only. If we have an empty directory git won't notice
at all. Well then, let's create a dummy file inside (and why not
creating another directory with a file inside that one?)

If we check the status of the repository now, we'll see a funny thing:

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   foo

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

    	new_dir/


Uh... So... if there is only a directory it won't notice but if it has a
file inside, it will notice... the directory? Go home; you're drunk.

Actually everything in git has an explanation, and this is no exception.
Git is assuming here that the whole directory is new and you will want
to add everything in it at once (which was the whole purpose of this
subsection). But let's suppose you are cuffed and a psycho is going to
kill you unless you show him all the untracked files in a new directory.
Don't worry, here comes git to save the day. if you run git status with
the `-u` flag, you will see this:

    >>> git status -u

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   foo

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

    	new_dir/foo
    	new_dir/subdir/foo


Enough of wandering off. If we try adding the directory with `git add
new_dir`, it will add all the files inside recursively, leaving the
status of the repo like this:

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   foo
    	new file:   new_dir/foo
    	new file:   new_dir/subdir/foo


Oh, look at it... now it shows all the files by default without the need
of the `-u`


#### Adding a glob

Let's assume we didn't run the add command from the last subsection. We
still have the new directories and all its contents in untracked state
or you can create new ones. The result will be the same. in my case, I
want to add all the files called foo, independently of where they am, so
let's run

    >>> git add **/foo

    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

    	new file:   foo
    	new file:   new_dir/foo
    	new file:   new_dir/subdir/foo

Nothing surprising here


### Commit this... commit that... how do I create one?

Finally, we are about to create our own commit! exciting, isn't it?
Ok, as we did in the last section, I'll let you guess the command you
have to run.


Did you think on `git commit`? Good guess!

So now we have all the files we want to include in the next commit
added. Let's run it!!

*Note: If git complains and refuses to make a commit prompting you to
run some "git config" command, go check the prerequisites in the
[introduction]({filename}/Git/introduction.md)*

It opens a text editor. Why? Well. In git you must add a comment on what
changes did you add since the last commit, what things must be taken
into account, maybe a note on why did you choose the algorithm you use...
Whatever is necesary. Let's assume this is our initial commit, so we'll
leave it as "Initial commit". Save and close the editor.

    [master (root-commit) 14e2905] Initial commit
     3 files changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 foo
     create mode 100644 new_dir/foo
     create mode 100644 new_dir/subdir/foo


A lot of info here. Let's go bit by bit.

**[master** --> That's the name of the branch we are in. We'll talk
about them in another post.

**(root-commit)** --> This indicates that this is the first commit in
the whole repository.

**14e2905]** --> This is the identifier of this commit (the reduced
version). It's probably different in your case. The next time you create
a new commit in the repository, you will see this identifier instead of
the *root-commit* we saw before.

**3 files changed, 0 insertions(+), 0 deletions(-)** --> This is a brief
of what happened in this commit in terms of what did you add. In this
case we have added 3 new files, we have added and removed 0 lines to
files that were already in the repository.

The remaining lines indicate if a file has been created, modified or
removed, and the mode of the file.


*Note:* There's a good practices guide for the commit messages, that you
can find [here](https://gist.github.com/matthewhudson/1475276)

### What commits are there in my repository?

Let's assume you have a special interest on checking what commits do
your repository have. Right now it doesn't seem an inmensely helpful
feature, but after a couple of posts more, you'll start to unlock its
full potential.

Actually, this is the first command that may not seem straightforward.
it's `git log` meaning some log of what has happened in the repository,
like a captain's logbook.

If you run it, you will see something like this:


    commit 14e29055abccd957a83763b26a8eed9fb7849f80
    Author: John Doe <foo@bar.com>
    Date:   Tue Oct 4 23:37:51 2016 +0100

        Initial commit


Line by line, this is the info we can find here:

*First line*: the full identifier of the commit. Maybe you noticed it
starts by the same characters that you saw when making the commit.

*Second line*: The author of the commit. This information is extracted
from the name and email you set up in the prerequisites section of the
Introduction.

*Third line*: The date in which the commit was created

*Fourth line*: The message you wrote when making the commit.


Well, with everything we have seen in this post, and it's a lot, you can
start working on your own project. Here it starts. The Git Adventure!


*If you have any question or any suggestion to make this series better,
please, comment in the box below, and I'll reply as soon as possible*
