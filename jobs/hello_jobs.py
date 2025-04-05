# from nautobot.apps.jobs import Job Version 3.1 
from nautobot.extras.jobs import Job

class HelloJobs(Job):
    class Meta:
        name = "Hello jobs from Git repo"

    def run(self):
        self.log_info("this is from the Git repo.")
        # self.logger__("this is from the Git repo.")
