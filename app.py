from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
         'Notification': Notification, 'Task': Task}
app.run(debug=True,host='127.0.0.1',port=6379)