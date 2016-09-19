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