from flask_socketio import emit
from extensions import socketio
import logging


logger = logging.getLogger(__name__)

@socketio.on('connect')
def handle_connect():
    emit('response', {'data': 'Connected'})

def notify_task_creation(task):
    data = {
        'id': task.id,
        'title': task.title,
        'notes': task.task_content,
        'completed': task.completed,
        'user_id': task.user_id
    }
    logger.info(f"Emitting new task creation: {data}")
    socketio.emit('new_task', data)
