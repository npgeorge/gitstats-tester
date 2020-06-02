# for Flask
#from .app import create_app

# for Heroku
from app import create_app

app = create_app()

# if we run the init file, it should run our app after importing it
if __name__ =="__main__":
    app.run_server(debug=True)