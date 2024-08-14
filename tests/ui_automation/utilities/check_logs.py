"""This conditional deployment in CI/CD is handled through this file.
Here, the deployment will be either successful or aborted based on the number failed cases captured in the logs file"""

import os
import smtplib
import sys
from pathlib import Path


# get all tests from class
class checklist:
    def remove_duplicate_logs(self):
        parent_folder = Path(__file__).parents[1]
        print(parent_folder, " this is the parent folder path in check_logs file")
        log_file_path = os.path.join(parent_folder, "logs", "sanity_logs.log")
        uniqlines = set(open(log_file_path).readlines())
        open(log_file_path, "w").writelines(set(uniqlines))

    # def move_logs_to_s3(self):
    #     parent_folder = Path(__file__).parents[1]
    #     print(parent_folder, " this is the parent folder path in check_logs file")
    #     file_name = 'sanity_logs.log'
    #     S3Tools('annalect-tech-generalreporting', file_name, str(parent_folder) + '/Utils/',
    #             'audiencebuilder/audiencebuilder-sanity-test-reports/failed_tests_screenshots').uploadToS3()

    def read_sanity_log_file(self):
        parent_folder = Path(__file__).parents[1]
        print(parent_folder, " this is the parent folder path in check_logs file")
        bool_sanity_file = os.path.isfile(
            os.path.join(parent_folder, "logs", "sanity_logs.log")
        )
        print(bool_sanity_file, " this is the bool value of bool_sanity_file")
        if bool_sanity_file == True:
            checklist().remove_duplicate_logs()
            # checklist().move_logs_to_s3()
            file_path = os.path.join(parent_folder, "logs", "sanity_logs.log")
            file = open(file_path, "r")
            # read content of file to string
            data = file.read()
            # get number of occurrences of the substring in the string
            failed_occurrences = data.count("FAILED")
            print("Number of occurrences of the word :", failed_occurrences)
            if failed_occurrences < 100:
                print("Deployment should start...")
                pass
            else:
                print("Deployment should get   terminated..")
                sys.exit(
                    f"Number of Failed test cases are {failed_occurrences} that's why deployment has got terminated"
                )
        else:
            print(
                "All the test cases got passed, hence didn't generate the sanity log file"
            )

    # TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    print("Going to read sanity logs")
    checklist().read_sanity_log_file()
    print("sanity log file has been checked")
