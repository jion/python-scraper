Simple Web Scraper for Python
=============================

We need some information here.

----

# Assumptions:

In order to limit the scope of the project for the purposes of this example,
some assumptions and limitations were made and are listed below

## 1. Foreign elements are not present
As we can see in the HTML specification `here: <http://w3c.github.io/html/syntax.html#void-elements>`
some HTML elements don't have a closing tag. This kind of element are called Void Elements.
Some of them are part of the HTML specification itself, and are listing there.
But apart from those, there are other void elements that are part of other specifications
(SVG and MathML spaces). We'll assume that only regular HTML-space void elements are
present in web pages (and this is true for the web page requested for the test).

## 2. Non-valid DOMs will stop the execution
In the wild web, there is a lot non-w3c compiliant HTML pages and the web browser do
a lot of guessing in order to render pages the more closest they can to the programmer's
intention. This means handle some non-closed tags, sintax errors and things like that.
For our example, we'll not tolerate and handle that. If there is missing tags o sintax
error we will inmediatly stop the excecution indicating that we can't parse the HTML.

## 3. 
