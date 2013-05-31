pyutils
=======

Python utilities

throttle.py
===========

the way throttle is implemented in underscore.py (and underscore.js) makes it impossible to use in circumstances where there is (unfortunately) thread-local storage, such as in Flask.

Here is the throttle decorator that I wrote which runs the throttled function in the context of the current thread.

it behaves slightly differently:
1. it is only set up to work on functions that don't return a value
2. it doesn't guarantee that the function will be called at the end of the interval because there is no separate thread

here are my two use cases for this:

1. when I want to print or log a something from a function that is called very frequently, such as in high-volume, long-running stream processing to print progress to the console every 'n' seconds

2. when I want to update a database with a count or timestamp, but don't want the writes to happen on every invocation, such as recording the last time a logged-in visitor came to a site, which only needs to be recorded every minute or so.
