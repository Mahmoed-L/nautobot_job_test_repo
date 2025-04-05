from nautobot.extras.jobs import Job, FileVar
# from nautobot.extras.jobs import *
import pandas as pd
import io
import os

name = "First job 5"


class TestingJob(Job):
    class Meta:
        name = "Test job 5 Layla"
        description = "This is an test 5"
    excel_file = FileVar()

    def run(self, data, commit):
        excel_file = data.get("excel_file", None)
        self.log_info("Het werkt")
        if not excel_file:
            self.log_info("The excel file path is invalid of the file does not exists")
        try:
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                self.log_info(index, row)
            self.log_info(f"First 5 rows of the excel file:\n{df.head()}")
        except Exception as e:
            self.log_info(f"Error reading the file str{e}")