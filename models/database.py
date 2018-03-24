from collections import defaultdict
db = defaultdict(list)

class Model(object):
    """
    Simple base class for data models.
    """
    def __init__(self, id):
        self.__dict__['id'] = id

    def __init_subclass__(cls, table=None):
        if table is None:
            raise KeyError
        cls._table = db[table]

    @classmethod
    def new(cls, **data):
        cls._table.append(data)
        id = cls._table.index(data)
        return cls(id)

    @classmethod
    def get_all(cls):
        return cls._table

    def __getattr__(self, key):
        return self._table[self.id][key]

    def __setattr__(self, key, value):
        self._table[self.id][key] = value

    def __repr__(self):
        return "<%s id='%d' at %s>" % (
            self.__class__.__name__, self.id, id(self)
        )
