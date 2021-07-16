# Quick links

- [Quick links](#quick-links)
- [Technologies used](#technologies-used)
    - [Frontend](((#F)))
    - [Backend](((#B)))
- [Notes](#notes)
- [Disclaimer](#disclaimer)


# This is my first live personal website

It's been a great journey developing this website as i got chance to learn new things like CSP (content security policy) headers, meta tags, XSS (cross site scripting) security stuffs, iframe attacks, compression techniques, various web performance metrics and techniques to improve the performance, handling hot linking situations, ranking in search resulta, various schemas like schema.org, OG, sitemaps etc.

# Technologies used

These technologies were used:

### [F]

1) HTML, CSS (obviously 🤷🏻‍♂️)
2) [Bootstrap](https://getbootstrap.com/)
   * powering the bare bone structure of the website
3) [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
   * Making things functional like share button, menu buttons etc

### [B]

5) [CPython3.8](https://www.python.org/downloads/release/python-385/)
   * humans know and speaks it 😉 .
6) [Sanic web framework](http://sanicframework.org/en/)
   * Asynchronous web framework.
   * Written to go fast ⚡, as they say.
7) [aiosqlite](https://pypi.org/project/aiosqlite/)
   * asynchronous sqlite querying.
8) [Jinja2](https://pypi.org/project/Jinja2/)
   * A really handy html template engine
9) [Ubuntu 20.04](https://releases.ubuntu.com/20.04/)
   * The usual

# Notes

When this website is configured to run to it's full potential (by setting the workers to max a processor allows), it is capable of handling many thousands of requests per second.

I have an `Intel 9th gen i7 9750H 6 core 12 logical cores` processor which allows a max of `12 workers`. Running the website `locally` with `workers set to 12`, it was able to handle approximately `4500+` requests per second 🤯. Shocking right! All thanks to the [Sanic web framework](http://sanicframework.org/en/). My server allows only one worker (single core), so, it's capable of handling approximately 100 requests per second.

# Disclaimer

Template of this website was borrowed from [here](https://www.bootstrapdash.com/product/free-bootstrap-resume/). I have modified most of it to my taste and needs, made it functional, really usable, improving its performancce by 40 to 60%, reducing size and keeping the overall visual structure same. Template comes under CC BY 3.0 (Creative Commons Attribution) License.
