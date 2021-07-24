minify = '/min/'
only_domain = '192.168.73.227:8000'
only_www_domain = 'www.' + only_domain
domain = 'http://' + only_domain
www_domain = "http://" + only_www_domain

paths = {
    "html": {
        "index": domain + '/templates' + minify + 'index.html',
        "resume": domain + '/templates' + minify + 'resume.html',
        "activities": domain + '/templates' + minify + 'activities.html',
        "contact": domain + '/templates' + minify + 'contact.html',
    },
    "css": {
        "main_css": domain + '/static/css' + minify + 'personal_site.css',
    },
    "js": {
        "main_js": domain + '/static/js' + minify + 'personal_site.js',
    },
    "videos": domain + '/static/videos/',
    "images": domain + '/static/images/',
    "documents": domain + '/static/documents/',
    "sitemap": domain + '/sitemap.xml',
}
