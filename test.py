import datetime
with open("count", "r+") as f:
        content = f.read()
        if content is not None:
                f.write("{}:{}".format(datetime.datetime.now(), int(content) + 1))
