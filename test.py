import datetime

# add comment for test buildbot gitpoller


with open("count", "rw") as f:
        content = f.read()
        if count is not None:
                f.write("{}:{}".formate(datetime.now(), int(content) + 1))
