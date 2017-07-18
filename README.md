Simple Web Scraper for Python
=============================

Welcome to the more recently rocket technology on Web Scrapers ever. Take sit and enjoy. Sorry my bad english (and my bad jokes).


# How to run this example:

There is not to much magic. I spend some time trying make a `config.py` file and a more pythonic
way to simplify this step, but I didn't success (and the test is so simple to keep trying).

So, To run the example request:

```
python main_example.py
```

and to run the only test file I made (bad for me):
```
python lib/scraper/test_operations.py
```

That is all.

# Architecture of this example

I follow a OOP style, doing classes and proper abstractions in order to
make the application the most extendable I can. Some simplifications were
made to avoid make the code too long, but I tried to use design patterns
and use loose coupling and high cohesion the best I could.
Each Class has a single purpose on the system, and collaborates with the
others to get the simple aim of the test.

The class diagram of my Scraper is the following:


# Assumptions:

In order to limit the scope of the project for the purposes of this example,
some assumptions and limitations were made and are listed below

## 1. Foreign HTML elements are not present
As we can see in the HTML specification here: <http://w3c.github.io/html/syntax.html#void-elements>
there are some HTML elements that don't have a pairing closing tag. This kind of elements
are called Void Elements.
Some of them are part of the HTML specification itself, and are listing in there.
But apart from those, there are others void elements that are part of other specifications
(SVG and MathML spaces, specifically). We'll assume that only regular HTML-space void elements are
present in web pages (and this is true for the web page requested for the test).

## 2. Non-valid DOMs will stop the execution
In the wild web, there are a lot non-w3c compiliant HTML pages and the web browser do
a lot of effort guessing, in order to render pages the more closest they can to the programmer's
intention. This means handle some non-closed tags, sintax errors and things like that.
For our example, we'll not tolerate and handle that. If there is missing tags o sintax
error we will inmediatly stop the excecution indicating that we can't parse the HTML.

## 3. Any Web Page fits in memory
At first I intended to make the fetching-parsing process asynchronyc. My idea was to
put a buffer in the middle of the output of the http-reader and the domBuilder, and even
put each task in his only thread.
This give us two benefits: we don't have to wait for the whole page to be loaded in order
to start parsing and also we fix a bug: we can't trust the whole page fits in system
memory (usually does, of course) and read one at once pretending that.
So, because I was having some troubles doing that works (As a begginer python developer I am)
I'll assume that we'll don't have a buffer overflow reading syncronically the webpage, and that
is what I'll do.

## 4. Test covergage is poor.
One of my surprises as a begginer in python was the version 2.7 doesn't came charged with a
mock library to use in our unit test. You need to use Python 3 in order to have urllib.mock
library available, o download that dependency (that is not allowed in the test statement).

Because the modeling and coding of this example has taken more time I would wish, I just
include unit test for the operations module, that I think is the core of this application.
(also, as is evident, I didn't use a BDD/TDD approach, I just create the Test Suite after
having code working).

# Final Considerations
Appart from the assumptions described above, I tried to make the code the most decoupled I could.
In some parts I decided to do it in a more "hardcore" fashion for the sake of the example,
but I tried to explain in comments when that was the case.
Also, I tried to document all classes (it was not so as I would wish with functions) and
did some investigation in more pythonic ways to do some parts of the code.

Also I left with some unresolved questions like a proper way to place and execute the test
(my test case file is just in the same path where the tested module is stored, and I didn't
find another way to discover/run the test automatically more than just execute manually the file
with `python testfile.py`).

As self-critisism, I tried to do this to-much OOP-style and force some patterns in some
places that maybe it adds unnecesary complecity for the purpose of this example.
This takes me a little bit more time refactoring, for a problem that I almost resolve in a
sandbox in 15 min (I left the sandbox file just in case you have curiosity)