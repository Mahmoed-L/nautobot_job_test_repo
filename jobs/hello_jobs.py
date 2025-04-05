# from nautobot.apps.jobs import Job Version 3.1 
from nautobot.extras.jobs import Job

class HelloJobs(Job):
    class Meta:
        name = "Hello jobs from Git repo 1"

    def run(self, data, commit):
        self.log_info("this is from the Git repo 1.")
        # self.logger__("this is from the Git repo.")
