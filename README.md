HackyTrack
==========

A simple command line tool for tracking time.  It works like a stop watch.  It doesn't do much else.  I am not proud of the code (thats where hacky comes from!)

Notable Features
----------------

- It supports tab completion.
- You can move through history with the up and down keys just like good ol' bash!
- You can tag things. Anything before the first `:` will count as a tag. If you'd like, you can use subtags as well, which will show up when using `hackyanalyze`.

Installation
============

At the moment you can only install via pip.

```
pip install https://github.com/kyle-long/hackytrack/archive/master.zip
```

Usage
=====

hackytrack
----------

Find yourself a directory you would like to store your tracking files in.  `hackytrack` will just start a prompt and ask you to enter a name of a task.  Enter anything you want.  Then when you switch tasks, enter another name and hit enter.  `hackytrack` will show the elapsed time.

```
hackytrack
> blah
> TAG1: doing some stuff
Elapsed Time : 0:00:04.000704
> TAG1: doing some other stuff
Elapsed Time : 0:00:05.177801
> This will show up in other
Elapsed Time : 0:00:03.906421
> TAG2: A tag all its own
Elapsed Time : 0:00:06.790382
> TAG2: <-- will go with the above task
Elapsed Time : 0:00:10.977127
> Done
Elapsed Time : 0:14:31.114860
```

To exit use "exit" keyword.

hackyanalyze
------------

If you want a breakdown of your day, you an use `hackyanalyze`.  You can simply run hackyanalyze to analyze current day's info and if you would like to analyze another days file simply pass it in.

```
hackyanalyze
OTHER: 0:00:10.791086
TAG1: 0:00:09.084222
TAG2: 0:14:42.091987
Total: 0:15:01.967295

hackyanalyze 2016-05-26
OTHER: 0:00:10.791086
TAG1: 0:00:09.084222
TAG2: 0:14:42.091987
Total: 0:15:01.967295
```

You can also add a `-v` (for verbose) option to get a more detailed breakdown.  You can add additonal `v`s to get more detail.

```
hackyanalyze 2016-05-26 -v
OTHER: 0:00:10.791086
    blah: 0:00:04.000704
    This will show up in other: 0:00:06.790382
TAG1: 0:00:09.084222
    doing some stuff: 0:00:05.177801
    doing some other stuff: 0:00:03.906421
TAG2: 0:14:42.091987
    A tag all its own: 0:00:10.977127
    <-- will go with the above task: 0:14:31.114860
Total: 0:15:01.967295
```

Special Syntax
==============

Tags
----

Anything before the first `:` is a tag. These are used organize tasks when using `hackyanalyze`. You are also able to use subtags. For example `MY_TAG: my task` will show up as...

    MY_TAG: <totalTime>
        my task: <timeForThisTask>

If you'd like to use a subtag, you can enter a `>` after the initial tag. You can enter as many as you'd like. For example `MY_TAG > MY_SUBTAG: my task` would show up as...

    MY_TAG: <totalTime>
        MY_SUBTAG: <totalTimeForSubtag>
            my task: <timeForThisTask>

Rename
------
You have the ability to rename a record if you wish. The syntax is like so

```
> /rename <numberOfTasksPreviously> <newName>
```

Where `numberOfTasksPreviously` specifies the number of tasks we should go back in history to alter (**Note: It is not zero indexed. So use `1` if you wish to alter the last task**) and where `newName` is what you would like to rename it as.

Thats about it.

Why did I build this?
=====================

There are plenty of time tracking command line utilities already. The reason I built this one was I wanted everything to work with as little typing and with as little complexity as possible. Many time tracking projects use a lot of options and force me to type the name of the tracking utility every time I'd like to add a task. Some even make you specifically clock out and back in.

This tool has grown organically based on the features I would like without making the original idea more complicated. A single prompt that you can enter a message in. It won't work for everyone but hey, it works for me.
