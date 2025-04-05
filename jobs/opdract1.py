from nautobot.extras.jobs import Job
from nautobot.extras.jobs import *
# import pandas as pd
import io
import os

name = "First job 4"


class TestingJob(Job):
    class Meta:
        name = "Test job 4 Layla"
        description = "This is an test 4"

    def run(self, data, commit):
        self.log_info("Het werkt")
