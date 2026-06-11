import os
import subprocess
import sys

from tests.kernel_runner.config import STAGES
from tests.kernel_runner.logger import KernelTestLogger


class KernelTestRunner:

    def __init__(self):
        self.logger = KernelTestLogger()
        self.failed = []

    def run(self):

        self.logger.log("BOOTING TRAINOS TEST KERNEL")

        for stage in STAGES:
            self.logger.stage(stage.name)

            for target in stage.tests:

                files = self._expand(target)

                for test_file in files:

                    result = self._run_test(test_file)

                    if result != 0:
                        self.failed.append(test_file)
                        self.logger.log(f"FAIL: {test_file}")
                        self.logger.log("KERNEL HALTED DUE TO FAILURE")
                        return 1

        self.logger.log("ALL STAGES PASSED")
        return 0

    def _expand(self, target: str) -> list[str]:

        if os.path.isdir(target):

            result = []

            for root, _, files in os.walk(target):
                for f in files:
                    if f.startswith("test_") and f.endswith(".py"):
                        result.append(os.path.join(root, f))

            return sorted(result)

        return [target]

    def _run_test(self, test_file: str) -> int:

        self.logger.log(f"RUN: {test_file}")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                test_file,
                "-q",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.stdout:
            print(result.stdout, end="")

        if result.stderr:
            print(result.stderr, end="")

        return result.returncode
