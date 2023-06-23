from fatihserver.framework.app import App, set_log_level
from fatihserver.framework.router import HttpRouter
from fatihserver.server.request_handler import Request, Response
from fatihserver.framework.static_files import StaticFiles

set_log_level('INFO')

router = HttpRouter()

static = StaticFiles()


@router.get("/index")
def index(request):
    with open("index.html", "r") as f:
        page = f.read()
        return Response(status_code=200, body=page, headers={
            "Content-Type": "text/html",
            "Server": "FatihServer"
        })


def main():
    static.add_static_dir(directory="assets/")
    router.add_static_route(static)

    app = App(router=router, host="localhost", port=8080)
    app.run()


if __name__ == '__main__':
    main()
