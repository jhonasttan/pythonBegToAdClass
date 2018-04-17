import web

url = (
    '/', 'home'
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(url, globals())

#Classes/routes

class home:
    def GET(self):
        return render.Home()

if __name__ == "__main__":
    app.run()