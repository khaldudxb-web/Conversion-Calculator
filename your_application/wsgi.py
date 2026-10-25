from pathlib import Path


INDEX_FILE = Path(__file__).resolve().parent.parent / "index.html"


def application(environ, start_response):
    request_method = environ.get("REQUEST_METHOD", "GET").upper()
    path = environ.get("PATH_INFO", "/")

    if request_method not in {"GET", "HEAD"}:
        body = b"Method Not Allowed\n"
        start_response(
            "405 Method Not Allowed",
            [
                ("Allow", "GET, HEAD"),
                ("Content-Type", "text/plain; charset=utf-8"),
                ("Content-Length", str(len(body))),
            ],
        )
        return [body]

    if path not in {"", "/", "/index.html"}:
        body = b"Not Found\n"
        start_response(
            "404 Not Found",
            [
                ("Content-Type", "text/plain; charset=utf-8"),
                ("Content-Length", str(len(body))),
            ],
        )
        return [body]

    body = INDEX_FILE.read_bytes()
    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(body))),
        ],
    )
    return [b"" if request_method == "HEAD" else body]
