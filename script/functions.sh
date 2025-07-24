#!/bin/bash

# 函数里面的变量一定要定义成local，否则会成为全局变量，有可能会覆盖函数脚本外面的变量
function get_os() {
  local os_string_array=("${@}")
  local os_type=$(uname)
  case "$os_type" in
  Linux*) echo "linux" ;;
  Darwin*) echo "macos" ;;
  CYGWIN* | MINGW32* | MSYS* | MINGW*) echo "window" ;;
  *) echo "Unknown operating system" ;;
  esac
}

function get_string_by_os() {
  local os_string_array=("${@}")
  local os_type=$(uname)
  case "$os_type" in
  Linux*) echo "${os_string_array[0]}" ;;
  Darwin*) echo "${os_string_array[1]}" ;;
  CYGWIN* | MINGW32* | MSYS* | MINGW*) echo "${os_string_array[2]}" ;;
  *) echo "Unknown operating system" ;;
  esac
}

function check_service_port() {
  # 检查lsof命令是否存在
  command -v lsof >/dev/null 2>&1 || {
    echo >&2 "lsof命令未安装，无法检查端口"
    exit 1
  }

  # 循环等待文件存在或超时
  local WAIT_TIME=$1      # 最大等待时间，单位：秒
  local CHECK_INTERVAL=$2 # 检查间隔，单位：秒
  local PORT=$3
  local elapsed_time=0 # 已经等待的时间
  while [ $elapsed_time -lt "${WAIT_TIME}" ] && ! lsof -Pi :"${PORT}" -sTCP:LISTEN -t >/dev/null; do
    echo "Starting..."
    sleep "${CHECK_INTERVAL}"                       # 等待一段时间
    elapsed_time=$((elapsed_time + CHECK_INTERVAL)) # 更新已经等待的时间
  done
  if [ $elapsed_time -ge "$WAIT_TIME" ]; then return 1; else return 0; fi
}

# 检查进程是否启动成功的函数
function check_process {
  # 循环等待文件存在或超时
  local WAIT_TIME=$1      # 最大等待时间，单位：秒
  local CHECK_INTERVAL=$2 # 检查间隔，单位：秒
  local PROCESS=$3
  local elapsed_time=0 # 已经等待的时间
  while [ $elapsed_time -lt "${WAIT_TIME}" ] && ! kill -0 "$PROCESS" > /dev/null 2>&1; do
    echo "Starting..."
    sleep "${CHECK_INTERVAL}"                       # 等待一段时间
    elapsed_time=$((elapsed_time + CHECK_INTERVAL)) # 更新已经等待的时间
  done
  if [ $elapsed_time -ge "$WAIT_TIME" ]; then return 1; else return 0; fi
}

function module_check_and_install() {
  local version=$(pip show "$1" | grep -c "Version:")
  if [ "${version}" -eq 0 ]; then
    echo "Try to install $1 module"
    pip3 install "$1" --break-system-packages
  else
    echo "The $1 module has been installed, $(pip show "$1" | grep "Version:")"
  fi
}


function python_module_check_by_pip3() {
  local module_name=$(pip3 show "$1" |  grep Name | cut -d : -f 2 2>&1)
  trimmed_module_name=$(echo "$module_name" | xargs)
  trimmed_input=$(echo "$module_name" | xargs)
  if [[ "${module_name}" -eq "$trimmed_input" ]]; then
    echo "The python module [ $1 ] has been installed."
    return 0
  else
    return 1
  fi
}

function kill_process_with_pid_file() {
  # 如果pid文件存在，则读取其中的进程ID并杀死这些进程
  pid_file=$1
  kill_children=$2
  echo "kill ${pid_file} with parameter=${kill_children}"
  if [[ ! -f "${pid_file}" ]]; then
    echo "There is no pid file=$1"
    return 0
  fi

  while read -r pid; do
    if [ -z "${pid}" ]; then
      continue
    fi

    children=$(pgrep -P "${pid}")
    if [[ -n "${children}" && "${kill_children}" == true ]]; then
      echo "Kill the children=${children} of parent=${pid}"
      echo "${children}" | xargs kill -9
    fi
    echo "Killing process with ID: ${pid}"
    kill -9 "${pid}"
  done <"${pid_file}"

  # 清空pid文件内容
  cat /dev/null >"${pid_file}"
}
