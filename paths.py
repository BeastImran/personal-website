minify = '/min/'
add_domain = 'http://192.168.0.103:8000'

paths = {
    "html": {
        "index": add_domain + '/templates' + minify + 'index.html',
        "resume": add_domain + '/templates' + minify + 'resume.html',
        "activities": add_domain + '/templates' + minify + 'activities.html',
        "contact": add_domain + '/templates' + minify + 'contact.html',
    },
    "css": {
        "main_css": add_domain + '/static/css' + minify + 'personal_site.css',
        "blog_css": add_domain + '/static/css' + minify + 'personal_site_blog.css',
        "form_css": add_domain + '/static/css' + minify + 'personal_site_form.css',
        "skills_css": add_domain + '/static/css' + minify + 'personal_site_skills.css',
    },
    "js": {
        "main_js": add_domain + '/static/js' + minify + 'personal_site.js',
    },
    "videos": add_domain + '/static/videos/',
    "images": add_domain + '/static/images/',
    "documents": add_domain + '/static/documents/',
    "sitemap": add_domain + '/sitemap.xml',
}
