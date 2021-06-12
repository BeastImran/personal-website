from jinja2 import Environment, FileSystemLoader
from sanic import Sanic, html

from utils.contact_form import add_contact

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Sanic("My First Sanic App")

app.static(
    "/static/",
    "./static/",
    name="static",
)

app.static('/favicon.ico', './static/favicon.ico')
app.static('/personal_site.css.map', './static/css/personal_site.css.map')
app.config.update_config({'REQUEST_MAX_SIZE': 1000})


@app.middleware("response")
async def add_cache_tts_policy(_, response):
    response.headers["Cache-control"] = "must-revalidate"
    response.headers["X - XSS - Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "same-origin"


@app.route("/")
@app.route("/index.html")
@app.route("/index")
@app.route("/home")
@app.route("/home.html")
async def home_page(_):
    return html(env.get_template('index.html').render(active='index'))


@app.route("/resume.html")
@app.route("/resume")
async def resume_page(_):
    return html(env.get_template('resume.html').render(active='resume'))


@app.route("/contacts.html", methods=["GET", "POST"])
@app.route("/contacts", methods=["GET", "POST"])
@app.route("/contact.html", methods=["GET", "POST"])
@app.route("/contact", methods=["GET", "POST"])
async def contact_page(request):
    if request.method == "POST":
        already_received = await add_contact(request.form)

        if already_received:
            if isinstance(already_received, int):
                if already_received <= 2:
                    already_received = "success"
                elif already_received <= 6:
                    already_received = "warning"
                else:
                    already_received = "danger"

            return html(env.get_template('contact.html').render(active='contact', already_received=already_received))
        else:
            return html(env.get_template('contact.html').render(active='contact', already_received='invalid-data'))
    else:
        return html(env.get_template('contact.html').render(active='contact'))


@app.route("/activities.html")
@app.route("/activities")
async def portfolio_page(_):
    return html(env.get_template('activities.html').render(active='activities'))


if __name__ == '__main__':
    app.run(host="192.168.0.103", access_log=False, debug=False, workers=1)
