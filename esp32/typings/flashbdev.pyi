from _typeshed import Incomplete as Incomplete

bdev: Incomplete

class Partition:
    RUNNING: int
    TYPE_APP: int
    TYPE_DATA: int
    BOOT: int
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def set_boot(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def find(self, *args, **kwargs) -> Incomplete: ...
    def get_next_update(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
