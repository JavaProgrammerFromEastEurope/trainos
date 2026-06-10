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

            for test_file in stage.tests:
                result = self._run_test(test_file)

                if result != 0:
                    self.failed.append(test_file)
                    self.logger.log(f"FAIL: {test_file}")
                    break

            if self.failed:
                self.logger.log("KERNEL HALTED DUE TO FAILURE")
                return 1

        self.logger.log("ALL STAGES PASSED")
        return 0

    def _run_test(self, test_file: str) -> int:

        self.logger.log(f"RUN: {test_file}")

        result = subprocess.run(
            [sys.executable, "-m", "pytest", test_file, "-q"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.stdout:
            print(result.stdout)

        if result.stderr:
            print(result.stderr)

        return result.returncode
