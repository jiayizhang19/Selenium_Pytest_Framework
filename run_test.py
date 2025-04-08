import subprocess
import os

# Important! Set the project root directory so that the below command could be run successfully wherever you execute it!
project_root = os.path.dirname(os.path.abspath(__file__))


def run_test(targets=None, markers=None, keyword=None):
    command = ["pytest"]

    if targets:
        if isinstance(targets,list):
            command.extend(targets)
        else:
            command.append(targets)

    if markers:
        command.extend(["-m", markers])
    if keyword:
        command.extend(["-k", keyword]) 

    subprocess.run(
        command,
        cwd=project_root,
        capture_output=True,
    )

if __name__ == "__main__":
    run_test(
        # targets=[
        #     "cases_bfd_regression/testcases_movie/P0/movie-9.air",
        #     "cases_bfd_regression/testcases_movie/P0/movie-10.air"
        # ],
        targets="cases_bfd_regression/testcases_movie/P0"
        # markers="bfd_movie",
        # keyword="",
    )

        


