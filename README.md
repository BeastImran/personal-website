# Quick links

- [Quick links](#quick-links)
- [This is my first real personal website](#this-is-my-first-real-personal-website)
- [Technologies used](#technologies-used)
    - [[fe]](#fe)
    - [[be]](#be)
- [Technical things](#technical-things)
- [Notes](#notes)


# This is my first real personal website

It's been a great journey developing this website as i got chance to learn new things like CSP (content security policy) headers and meta tags, XSS (cross site scripting) security stuffs, iframe attacks etc. I really believe this knoweldge will definetly help me a lot in future.

# Technologies used

In frontend and backend, these technologies has been used:

### [fe]

1) HTML, CSS (obviously 🤷🏻‍♂️)

2) [Bootstrap](https://getbootstrap.com/)
   * powering the bare bone structure of the website
3) [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
   * Making things functional like share button, menu buttons etc
4) [Jquery](https://jquery.com/)
   * Simplifies some javascript things.


### [be]

5) [CPython3.8](https://www.python.org/downloads/release/python-385/)
   * humans know and speaks it 😉 .
6) [Sanic web framework](http://sanicframework.org/)
   * Asynchronous web framework.
   * Written to go fast ⚡, as they say.
7) [aiosqlite](https://pypi.org/project/aiosqlite/)
   * asynchronous sqlite querying.
8) [Jinja2](https://pypi.org/project/Jinja2/)
   * A really handy html template engine

# Technical things

When this website is configured to run to it's full potential (by setting the workers to max a processor allows), it is capable of handling many thousands of requests per second.

I have an `Intel 9th gen i7 9750H 6 core 12 logical cores` processor which allows a max of `12 workers`. Running the website `locally` with `workers set to 12`, it was able to handle approximately `4500+` requests per second 🤯. Shocking right! All thanks to the [Sanic web framework](http://sanicframework.org/). My server allows only one worker (single core), so, it's capable of handling approximately 1000 requests per second.


# Notes

Template of this website has been used from [here](https://www.bootstrapdash.com/product/free-bootstrap-resume/) and i modified most of it to my taste and needs, made it functional, really usable. Template comes under CC BY 3.0 (Creative Commons Attribution) License.