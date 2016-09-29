===============================
op_mon
===============================

Oracle Python Monitor


Quickstart
----------

First, set your app's secret key as an environment variable. For example,
add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export OP_MON_SECRET='something-really-secret'

Before running shell commands, set the ``FLASK_APP`` and ``FLASK_DEBUG``
environment variables ::

    export FLASK_APP=/path/to/autoapp.py
    export FLASK_DEBUG=1

Then run the following commands to bootstrap your environment ::

    git clone https://github.com/joyider/op_mon
    cd op_mon
    pip install -r requirements/dev.txt
    bower install
    flask run

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    flask run


Deployment
----------

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProdConfig`` is used.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.

Create Oracle User
------------------
To set up the user you need to add this schema using the following grants. ::

    CREATE USER OP_MON IDENTIFIED BY DEFAULT TABLESPACE SYSTEM TEMPORARY TABLESPACE TEMP PROFILE DEFAULT ACCOUNT UNLOCK;
    GRANT CONNECT TO OP_MON;
    GRANT RESOURCE TO OP_MON;
    ALTER USER OP_MON DEFAULT ROLE ALL;
    GRANT SELECT ANY TABLE TO OP_MON;
    GRANT CREATE SESSION TO OP_MON;
    GRANT SELECT ANY DICTIONARY TO OP_MON;
    GRANT UNLIMITED TABLESPACE TO OP_MON;
    GRANT SELECT ANY DICTIONARY TO OP_MON;
    GRANT SELECT ON V_$SESSION TO OP_MON;
    GRANT SELECT ON V_$SYSTEM_EVENT TO OP_MON;
    GRANT SELECT ON V_$EVENT_NAME TO OP_MON;
    GRANT SELECT ON V_$RECOVERY_FILE_DEST TO OP_MON;
