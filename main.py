from fatihserver.framework.app import App, set_log_level
from fatihserver.framework.router import HttpRouter
from fatihserver.server.request_handler import Request, Response
from fatihserver.framework.static_files import StaticFiles
from fatihserver.framework.templates import Templates, TemplateResponse

set_log_level('INFO')

# Create router
router = HttpRouter()

# Create static files
static = StaticFiles()

# Create templates
templates = Templates()


@router.get("/")
def index(request):
    return TemplateResponse(template=templates, name="index", payload={
        "name": "Fatih",
        "title": "FFC | Personal Website",
        "cv_link": "https://google.com",
        "github_link": "https://github.com/FFC12",
        "linkedin_link": "https://linkedin.com/in/furkanfatihcetindil",
        "mail_link": "fatihsaika@gmail.com"
    })


def main():
    # Add static files
    static.add_static_dir(directory="assets/")

    # Add static route
    router.add_static_route(static)

    # Add templates
    templates.add_templates(path="templates/")

    # Create app
    app = App(router=router, host="0.0.0.0", port=8000)

    # Run app
    app.run()


if __name__ == '__main__':
    main()
