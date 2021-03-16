import json
from dataclasses import dataclass
from typing import Optional

import dataclass_factory as dcf
import jsons

factory = dcf.Factory()


@dataclass()
class Memo:
    title: str
    lock: bool
    letters: str
    date: str


@dataclass()
class MemoData:
    """Jsonからのシリアライズとキャッシュ"""

    memos: list[Memo]

    def __getitem__(self, k: str) -> Optional[Memo]:
        result: Optional[Memo] = None
        for m in self.memos:
            if m.title == k:
                result = m
        return result

    def titles(self) -> tuple[str]:
        return tuple([m.title for m in self.memos])


def _str_to_data(s: str) -> MemoData:
    return factory.load(json.loads(s), MemoData)


def _fp_to_str(fp: str) -> str:
    return json.dumps(json.load(open(fp)))


def json_to_data(fp: str) -> MemoData:
    return _str_to_data(_fp_to_str(fp))


def writedata_to_file(fp: str, data: MemoData):
    with open(fp, mode="") as f:
        json.dump(jsons.dump(data), f)
