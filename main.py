import gzip
from io import BytesIO as IO

from aiofiles import open
from jinja2 import Environment, FileSystemLoader
from sanic import Sanic, html, HTTPResponse
from sanic.response import file, empty, redirect

from paths import paths, minify
from utils.contact_form import add_contact

html_paths = paths['html']
css_file_names = tuple([file_name.rpartition('/')[2] for file_name in paths["css"].values()])


async def css(body, headers=None):
    content_type: str = "text/css; charset=utf-8"
    return HTTPResponse(body, headers=headers, content_type=content_type)


async def js(body, headers=None):
    content_type: str = "application/javascript; charset=utf-8"
    return HTTPResponse(body, headers=headers, content_type=content_type)


async def send_response(request, response):
    host = request.headers.get('host', '')
    if host == '' or (host == "beastimran.com" or host == "www.beastimran.com"):
        accept_encoding = request.headers.get("Accept-Encoding", "") or request.headers.get("accept-encoding", "")

        if ("gzip" not in accept_encoding.lower()) or (response.status < 200 or response.status >= 300 or "Content-Encoding" in response.headers):
            return response

        gzip_buffer = IO()
        gzip_file = gzip.GzipFile(mode="wb", fileobj=gzip_buffer)
        gzip_file.write(response.body)
        gzip_file.close()

        response.body = gzip_buffer.getvalue()
        response.headers["content-encoding"] = "gzip"
        response.headers["vary"] = "accept-encoding"
        response.headers["content-length"] = len(response.body)
        return response

    return redirect("http://beastimran.com/")


file_loader = FileSystemLoader('templates/' + minify)
env = Environment(loader=file_loader)
app = Sanic("BeastImran.com")
app.static("/static/videos/", "./static/videos/", use_content_range=True)
app.static("/static/images/", "./static/images/")
app.static("/static/documents/", "./static/documents/")
app.static("/favicon.ico", "./static/favicon.ico")
app.config.update_config({"REQUEST_MAX_SIZE": 1000})


@app.get("/static/css/<css_file_name:path>")
async def serve_css(request, css_file_name):
    if css_file_name.rpartition('/')[2] in css_file_names:
        css_file = await open('./static/css/' + ('min/' + css_file_name.rpartition('/')[2] if '/min/' in css_file_name else '' + css_file_name))
        content = await css_file.read()
        await css_file.close()
        return await send_response(request, await css(content))
    return empty()


@app.get("/static/js/<js_file_name:path>")
async def serve_js(request, js_file_name):
    if js_file_name.rpartition('/')[2] == "personal_site.js":
        js_file = await open('./static/js/' + ('min/' + "personal_site.js" if '/min/' in js_file_name else "personal_site.js"))
        content = await js_file.read()
        await js_file.close()
        return await send_response(request, await js(content))
    return empty()


@app.middleware("response")
async def add_cache_tts_policy(_, response):
    # response.headers["strict-transport-security"] = "max-age=63072000; includeSubDomains; preload"
    response.headers["cache-control"] = "private, must-revalidate"
    response.headers[
        "content-security-policy"] = "img-src 'self' http://beastimran.com http://www.beastimran.com; font-src 'self'; connect-src 'self'; media-src 'self' http://beastimran.com http://www.beastimran.com; object-src 'none'; prefetch-src 'self'; frame-src 'self' https://www.redditmedia.com/ https://www.google.com/; worker-src 'none'; form-action 'self';  script-src 'self' http://beastimran.com http://www.beastimran.com;"
    response.headers["referrer-policy"] = "strict-origin-when-cross-origin"
    response.headers["x-content-type-options"] = "nosniff"
    response.headers["x-frame-options"] = "SAMEORIGIN"
    response.headers["x-xss-protection"] = "1; mode=block"
    response.headers["access-control-allow-origin"] = "no"


@app.route("/")
@app.route("/index")
@app.route("/home")
@app.route("/home.html")
@app.route("/index.html")
async def home_page(request):
    return await send_response(request=request, response=html(
        env.get_template('index.html').render(active='index', css=paths['css'], js=paths['js'], images_path=paths['images'],
                                              doc_path=paths['documents'], videos_path=paths['videos'])))


@app.route("/resume")
@app.route("/resume.html")
async def resume_page(request):
    return await send_response(request=request, response=html(
        env.get_template('resume.html').render(active='resume', css=paths['css'], js=paths['js'], images_path=paths['images'],
                                               videos_path=paths['videos'])))


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

            return await send_response(request=request, response=html(
                env.get_template('contact.html').render(active='contact', already_received=already_received, css=paths['css'], js=paths['js'],
                                                        images_path=paths['images'],
                                                        videos_path=paths['videos'])))
        else:
            return await send_response(request=request, response=html(
                env.get_template('contact.html').render(active='contact', already_received='invalid-data', css=paths['css'], js=paths['js'],
                                                        images_path=paths['images'],
                                                        videos_path=paths['videos'])))
    else:
        return await send_response(request=request, response=html(
            env.get_template('contact.html').render(active='contact', css=paths['css'], js=paths['js'], images_path=paths['images'],
                                                    videos_path=paths['videos'])))


@app.route("/activities")
@app.route("/activities.html")
async def portfolio_page(request):
    return await send_response(request=request, response=html(
        env.get_template("activities.html").render(active='activities', css=paths['css'], js=paths['js'], images_path=paths['images'],
                                                   videos_path=paths['videos'])))


@app.route("/sitemap")
@app.route("/sitemap.xml")
async def sitemap(_):
    return await file('sitemap.xml')


@app.route("/google1ae25284ecc16fa9.html")
async def google_verification(_):
    return await file('google1ae25284ecc16fa9.html')


if __name__ == '__main__':
    app.run(host="192.168.0.103", access_log=False, debug=False, workers=1)
