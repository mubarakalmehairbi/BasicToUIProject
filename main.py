from toui import Website, DesktopApp, set_global_app

SECRET_KEY = "some secret string" # Change this to a harder to guess value.

# Create the app. You can create a desktop app by replacing `Website` with `DesktopApp`
app = Website(__name__, assets_folder="assets", secret_key=SECRET_KEY)

# Allows the app to be shared across Python scripts
set_global_app(app)

# Import the home page in order to run the home_pg.py script and to add the page to the app.
from home_pg import home_pg
app.add_pages(home_pg)

# Get the Flask app instance. This will be helpful when deploying the app.
flask_app = app.flask_app

if __name__ == "__main__":
    app.run(debug=True)