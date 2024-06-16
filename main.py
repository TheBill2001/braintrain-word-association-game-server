from server.app import APP
from server import server_config, route

# Declare routes
@APP.route("/ping")
def hello_world():
    """
    The default route for the server.
    Return a "Hello, World!" message in JSON format.
    """
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    from waitress import serve
    serve(app=APP, host="0.0.0.0", port=server_config.PORT)
