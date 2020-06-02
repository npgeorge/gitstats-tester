# import the create_app function from our app file
from git_app.app import create_app

# if we run the init file, it should run our app after importing it
if __name__ =="__main__":
    app = create_app()
    app.run(debug=True)

#try this next
#if __name__ == '__main__':
#    app.run_server(debug=True)