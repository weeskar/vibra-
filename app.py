#app.py
from vibra import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    if not os.path.exists('vibra.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)