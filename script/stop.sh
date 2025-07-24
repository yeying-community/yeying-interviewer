#!/usr/bin/env bash

COLOR_RED='\033[1;31m'
COLOR_NC='\033[0m'

script_dir=$(
  cd $(dirname "$0") || exit 1
  pwd
)

source "${script_dir}"/functions.sh

work_dir=$(
  cd "${script_dir}"/.. || exit 1
  pwd
)

# 定义保存进程ID的文件路径
run_dir=${work_dir}/run
if kill_process_with_pid_file "${run_dir}/pid.txt" true; then
  echo "Stop interviewer successfully!"
  rm -rf "${run_dir}/pid.txt"
else
  echo -e "${COLOR_RED}Fail to stop interviewer, Please check it!${COLOR_NC}"
fi
