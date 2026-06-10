import time


class KernelTestLogger:

    def __init__(self):
        self.start = time.time()

    def log(self, msg: str):
        t = time.time() - self.start
        print(f"[KERNEL-TEST {t:.4f}] {msg}")

    def stage(self, name: str):
        print("\n" + "=" * 60)
        print(f"[STAGE START] {name}")
        print("=" * 60 + "\n")
