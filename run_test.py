import subprocess
import os

# Important! Set the project root directory so that the below command could be run successfully wherever you execute it!
project_root = os.path.dirname(os.path.abspath(__file__))


def run_test():
    command = [
        "pytest", "-vv",
        "--rootdir", project_root
    ]
    subprocess.run(
        command,
        cwd=project_root,
        capture_output=True,
        text=True
    )

if __name__ == "__main__":
    run_test()

        


