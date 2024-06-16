from dotenv import dotenv_values

SERVER_CONFIG = dotenv_values(".env")

"""Server port"""
PORT = SERVER_CONFIG["PORT"] if "PORT" in SERVER_CONFIG else "3000"
