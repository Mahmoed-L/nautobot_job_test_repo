from nautobot.apps.jobs import Job

class HelloJobs(Job):
    class Meta:
        name = "Hello jobs from Git repo"

    def run(self):
        self.logger.debug("this is from the Git repo.")
