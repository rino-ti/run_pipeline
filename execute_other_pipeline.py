#!/usr/bin/python3
import gitlab
import time, timeit
import sys

#Variables project remote
projectID=sys.argv[1]
bucket=sys.argv[2]
email=sys.argv[3]
files=sys.argv[4]
ip=sys.argv[5]
path=sys.argv[6]
ambiente=sys.argv[7]


from datetime import timedelta

gl = gitlab.Gitlab("https://github.com//",
                    private_token="XXXXXXXXXXXXXXXXXXX")


project = gl.projects.get( projectID )


def get_or_create_trigger(project):
    trigger_decription = 'my_trigger_id'
    for t in project.triggers.list():
        if t.description == trigger_decription:
            return t
    return project.triggers.create({'description': trigger_decription})

trigger = get_or_create_trigger(project)
create_pipeline = project.trigger_pipeline('master', trigger.token, variables={"bucket": bucket, "email": email, "file": files, "ip": ip, "path": path, "ambiente": ambiente})

# Set default
status = "pending"
start_time = timeit.default_timer()

while (status == "running" or status == "pending"):
    pipeline = project.pipelines.get(create_pipeline.id)
    

    status = pipeline.status

    elapsed_time = timeit.default_timer() - start_time
    formated_time = str(timedelta(seconds=elapsed_time))
    sys.stderr.write("Still running pipeline... ({})\n".format(formated_time))

    if status == "success":
        sys.stderr.write("\nPipeline success\n")
        break
    elif status == "failed":
        raise Exception
    elif status == "canceled":
        raise Exception

    time.sleep(10)
