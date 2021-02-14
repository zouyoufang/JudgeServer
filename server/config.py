import os
import pwd

import grp

QDUOJ_HOME = '/home/oj/qduoj/'
QDUOJ_UNAME = 'oj'
QDUOJ_UGROUP = 'oj'
QDUOJ_DATA_HOME = '/home/oj/qduoj/OnlineJudge/data/'


JUDGER_WORKSPACE_BASE = QDUOJ_HOME + "run"
LOG_BASE = QDUOJ_HOME + "log"

COMPILER_LOG_PATH = os.path.join(LOG_BASE, "compile.log")
JUDGER_RUN_LOG_PATH = os.path.join(LOG_BASE, "judger.log")
SERVER_LOG_PATH = os.path.join(LOG_BASE, "judge_server.log")

RUN_USER_UID = pwd.getpwnam(QDUOJ_UNAME).pw_uid
RUN_GROUP_GID = grp.getgrnam(QDUOJ_UGROUP).gr_gid

COMPILER_USER_UID = pwd.getpwnam(QDUOJ_UNAME).pw_uid
COMPILER_GROUP_GID = grp.getgrnam(QDUOJ_UGROUP).gr_gid

SPJ_USER_UID = pwd.getpwnam(QDUOJ_UGROUP).pw_uid
SPJ_GROUP_GID = grp.getgrnam(QDUOJ_UGROUP).gr_gid

TEST_CASE_DIR = QDUOJ_DATA_HOME + "test_case"
SPJ_SRC_DIR =  QDUOJ_DATA_HOME + "spj"
SPJ_EXE_DIR = QDUOJ_DATA_HOME + "spj"
