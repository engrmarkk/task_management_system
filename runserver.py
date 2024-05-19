from app_config import create_app
from dotenv import load_dotenv
from extensions import socketio

load_dotenv()

app = create_app()

if __name__ == "__main__":
    socketio.run(app, debug=True)
