import datetime

# add comment for test buildbot gitpoller


with open("count", "r+") as f:
        content = f.read()
        if content is not None:
                f.write("{}:{}".format(datetime.datetime.now(), int(content) + 1))
