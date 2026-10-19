from tests.kernel_runner.runner import KernelTestRunner


def main():
    runner = KernelTestRunner()
    code = runner.run()
    exit(code)


if __name__ == "__main__":
    main()
