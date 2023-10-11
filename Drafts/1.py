print("%.2f" % (3.1231241254124))
print("{:.2f}".format(3.1331241254124))
print("{0} {1} {0}".format("Hello", "World"))
data = {
    'name': 'Hodor',
    'email': 'hodor@gmal.com'
}
print("Name: {name}\nEmail: {email}".format(**data))
print("%s %s %s %s" % ("Hello", 12, 131.312, {'hello': 'sup'}))