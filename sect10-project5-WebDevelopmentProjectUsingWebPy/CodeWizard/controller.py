import web

url = (
    '/', 'home'
)

app = web.application(url, globals())

#Classes/routes

class home:
    def GET(self):
        return "home"

if __name__ == "__main__":
    app.run()