HackyTrack
==========

A simple command line tool for tracking time.  It works like a stop watch.  It doesn't do much else.  I am not proud of the code (thats where hacky comes from!)

Installation
============

At the moment you can only install via pip.

```
pip install git+git://github.com/kyle-long/hackytrack.git@master
```

Usage
=====

hackytrack
----------

Find yourself a directory you would like to store your tracking files in.  `hackytrack` will just start a prompt and ask you to enter a name of a task.  Enter anything you want.  Then when you switch tasks, enter another name and hit enter.  `hackytrack` will show the elapsed time.

```
hackytrack
> Name : blah
> Name : TAG1: doing some stuff
Elapsed Time : 0:00:04.000704
> Name : TAG1: doing some other stuff
Elapsed Time : 0:00:05.177801
> Name : This will show up in other
Elapsed Time : 0:00:03.906421
> Name : TAG2: A tag all its own
Elapsed Time : 0:00:06.790382
> Name : TAG2: <-- will go with the above task
Elapsed Time : 0:00:10.977127
> Name : Done
Elapsed Time : 0:14:31.114860
```

To exit use Ctrl+c (SIGINIT).  Pretty hacky.

hackyanalyze
------------

If you want a breakdown of your day, you an use `hackyanalyze`.  Just specify a file that `hackytrack` has created.

```
hackyanalyze 2016-05-26 
OTHER: 0:00:10.791086
TAG1: 0:00:09.084222
TAG2: 0:14:42.091987
Total: 0:15:01.967295
```

You can also add a "more" argument to get a more detailed breakdown.  It doesn't actually need to say "more".  It can be anything. In the future I plan to use docopt to make the interface better.

```
hackyanalyze 2016-05-26 more
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
