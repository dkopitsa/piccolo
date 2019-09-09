.. _ColumnTypes:

Column Types
============

.. hint:: You'll notice that all of the column names match their SQL equivalents.

Column
------

All other columns inherit from ``Column``. Don't use it directly.

The following arguments apply to all column types:

default
~~~~~~~

.. code-block:: python

    class Band(Table):
        name = Varchar(default="hello")

null
~~~~

...

Varchar
-------

.. code-block:: python

    class Band(Table):
        name = Varchar()

ForeignKey
----------

.. code-block:: python

    class Band(Table):
        manager = ForeignKey(Manager)

Integer
-------

.. code-block:: python

    class Band(Table):
        popularity = Integer()

Timestamp
---------

.. code-block:: python

    class Band(Table):
        created = Timestamp()

Boolean
-------

.. code-block:: python

    class Band(Table):
        has_drummer = Boolean()