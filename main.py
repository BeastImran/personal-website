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
    # response.headers["strict-transport-security"] = "max-age=63072000; includeSubDomains; preload"
    response.headers["cache-control"] = "private, must-revalidate"
    response.headers[
        "content-security-policy"] = "script-src 'self'; object-src 'none'; connect-src 'self'; font-src 'self'; img-src 'self'; manifest-src 'self'; media-src 'self'; worker-src 'none';"
    response.headers["referrer-policy"] = "strict-origin-when-cross-origin"
    response.headers["x-content-type-options"] = "nosniff"
    response.headers["x-frame-options"] = "SAMEORIGIN"
    response.headers["x-xss-protection"] = "1; mode=block"
    response.headers["access-control-allow-origin"] = "no"


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
                if already_received <= 1:
                    already_received = "success"
                elif already_received <= 5:
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
