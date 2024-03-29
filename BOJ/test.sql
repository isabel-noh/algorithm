CREATE TABLE TEAM(
    TEAM_ID CHAR(3) NOT NULL,
    REGION_NAME VARCHAR(8) NOT NULL,
    TEAM_NAME VARCHAR(40), NOT NULL 
    E_TEAM_NAME VARCHAR(50),
    ORIG_YYY CHAR(4),
    STADIUM_ID CHAR(4) NOT NULL,
    CONSTRAINT TEAM_PK PRIMARY KEY (TEAM_ID),
    CONSTRAINT TEAM_FK FOREIGN KEY (STADIUM_ID) REFERENCES STADIUM (STADIUM_ID)
);

ALTER TABLE TEAM ALTER COLUMN ORIG_YYYY VARCHAR2(8) DEFAULT '20020129'  NOT NULL;