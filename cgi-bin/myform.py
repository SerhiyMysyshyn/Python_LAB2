import cgi
import html
import http.cookies
import os

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
count = cookie.get("counter")
if count is None:
    print("Set-cookie: counter=1")
else:
    c = count.value
    c = int(c)
    c = c + 1
    print(f"Set-cookie: counter={c}")

form = cgi.FieldStorage()
text1 = form.getfirst("firstName", "не задано")
text2 = form.getfirst("lastName", "не задано")

checklist = form.getlist("cgBox")
radioBut = form.getvalue("radioB")

text1 = html.escape(text1)
text2 = html.escape(text2)
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Передані дані</title>
        </head>
        <body>""")
print("<h1>Передані дані</h1>")
print("<p> <b>Ім'я:</b> {}</p>".format(text1))
print("<p> <b>Прізвище:</b> {}</p>".format(text2))
print("<b>Стать: </b>" + radioBut)
print("<br><br><b>Професія:</b> " + ', '.join(checklist))

print("<hr>")
print("Кількість звернень: " + count.value)
print("<hr>")
for k,v in os.environ.items():
    print("<p>"+k + " " + v + "</p>")

print("<hr>")
print("""</body>
        </html>""")