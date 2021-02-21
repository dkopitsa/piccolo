from enum import Enum


class IndexMethod(str, Enum):
    btree = "btree"
    hash = "hash"
    gist = "gist"
    gin = "gin"

    def __str__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __repr__(self):
        return self.__str__()
