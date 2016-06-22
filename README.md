HackyTrack
==========

A simple command line tool for tracking time.  It works like a stop watch.  It doesn't do much else.  I am not proud of the code (thats where hacky comes from!)

Notable Features
----------------

- It supports tab completion.
- You can move through history with the up and down keys just like good ol' bash!

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

You can also add a `-v` (for verbose) option to get a more detailed breakdown.  You can add additonal more `v`s to get more detail.

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

Thats about it.
