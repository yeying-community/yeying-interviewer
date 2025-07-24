#!/usr/bin/env bash

COLOR_RED='\033[1;31m'
COLOR_BLUE='\033[1;34m'
COLOR_NC='\033[0m'

function check_port_status() {
  # 检查lsof命令是否存在
  command -v lsof >/dev/null 2>&1 || {
    echo >&2 "command 'lsof' Cannot be found"
    exit 1
  }

  # 循环等待文件存在或超时
  local WAIT_TIME=$1      # 最大等待时间，单位：秒
  local CHECK_INTERVAL=$2 # 检查间隔，单位：秒
  local PORT=$3
  local elapsed_time=0 # 已经等待的时间
  while [ $elapsed_time -lt "${WAIT_TIME}" ] ; do
    check_process=$(lsof -Pi :"${PORT}" -sTCP:LISTEN -t)
    if [[ "$check_process" =~ ^[0-9]+$ ]] && [ "$check_process" -gt 0 ]; then
      echo -e "port ${COLOR_BLUE}[${PORT}]${COLOR_NC} runs well with process ${COLOR_BLUE}[${check_process}]${COLOR_NC}"
      return "${check_process}"
    else
      sleep "${CHECK_INTERVAL}"
      echo -e "wait ${CHECK_INTERVAL} seconds to check again"
    fi
    elapsed_time=$((elapsed_time + CHECK_INTERVAL)) 
  done
  return 0
}


script_dir=$(
  cd $(dirname "$0") || exit 1
  pwd
)

work_dir=$(
  cd "${script_dir}"/.. || exit 1
  pwd
)


config_file_envoy_yaml=${work_dir}/run/config/envoy.yaml
if [ ! -f "${config_file_envoy_yaml}" ]; then
  echo -e "${COLOR_RED}Cannot find file: ${config_file_envoy_yaml}  ${COLOR_NC}"
  exit 1
fi

ports=$(sed -n '/port_value/p' "$config_file_envoy_yaml"|cut -d ':' -f 2)

IFS=$'\n' read -r -d '' -a port_array <<< "$ports"
echo -e "going to check ports: " "${port_array[@]}"

for each_port in "${port_array[@]}"; do
  port="${each_port#"${each_port%%[![:space:]]*}"}"
  port="${port%"${port##*[![:space:]]}"}"
  echo -e "check port: ----$port----"
  check_port_status 10 1 "$port"
  process_value=$?
  if [ "$process_value" -eq 0 ]; then
    echo -e "${COLOR_RED}[prot: ${port}] of interviewer Not started yet. ${COLOR_NC}"
  fi
done


echo "interviewer health check finished. [$(date)]"
