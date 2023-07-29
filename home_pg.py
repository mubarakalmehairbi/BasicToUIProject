from toui import Page, get_global_app

app = get_global_app()
home_pg = Page("assets/index.html", url="/")

def print_value():
    pg = app.get_user_page()
    pg.get_element("output").set_content("10")

home_pg.get_element("print").onclick(print_value)