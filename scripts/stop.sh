#!/usr/bin/env bash

# =================颜色定义=================
# 定义控制台输出颜色，用于增强可读性
COLOR_RED='\033[1;31m'      # 红色（错误信息）
COLOR_GREEN='\033[1;32m'    # 绿色（成功信息）
COLOR_BLUE='\033[1;34m'     # 蓝色（环境标识）
COLOR_YELLOW='\033[1;33m'   # 黄色（警告信息）
COLOR_NC='\033[0m'          # 无颜色（重置）

# =================路径变量=================
# 获取脚本自身的名称（去掉路径）
base_name="${0##*/}"

# 获取脚本所在目录的绝对路径
script_dir=$(
  cd $(dirname "$0") || exit 1
  pwd
)

# 获取工作目录（脚本目录的上级目录）
work_dir=$(
  cd "${script_dir}"/.. || exit 1
  pwd
)

# =================帮助信息=================
usage() {
  printf "Usage: %s\n \
    -f <Force kill all interviewer processes.> \n \
    -p <Kill specific process by PID.> \n \
    -h <Show this help message.> \n \
    " "${base_name}"
}

# =================默认配置=================
force_kill=false
specific_pid=""

# =================命令行参数解析=================
# 使用getopts解析命令行选项
while getopts ":fp:h" o; do
  case "${o}" in
  f)
    # -f 参数：强制杀死所有进程
    force_kill=true
    ;;
  p)
    # -p 参数：杀死指定PID的进程
    specific_pid=${OPTARG}
    ;;
  h)
    # -h 参数：显示帮助信息
    usage
    exit 0
    ;;
  *)
    # 无效参数：显示用法并退出
    usage
    exit 1
    ;;
  esac
done
shift $((OPTIND - 1))  # 移除已处理的参数

# =================停止信息显示=================
printf "\n"
echo -e "${COLOR_BLUE}Stopping interviewer service... [$(date)]${COLOR_NC}"
echo "Work directory: ${work_dir}"

# =================目录定义=================
run_dir=${work_dir}/run
pid_file=${run_dir}/pid.txt
log_dir=${run_dir}/log

# =================特定PID停止=================
if [ -n "${specific_pid}" ]; then
  echo -e "${COLOR_YELLOW}Attempting to stop process with PID: ${specific_pid}${COLOR_NC}"
  
  # 检查进程是否存在
  if kill -0 "${specific_pid}" 2>/dev/null; then
    echo "Sending TERM signal to process ${specific_pid}..."
    kill "${specific_pid}"
    
    # 等待进程优雅退出
    for i in {1..10}; do
      if ! kill -0 "${specific_pid}" 2>/dev/null; then
        echo -e "${COLOR_GREEN}Process ${specific_pid} stopped successfully.${COLOR_NC}"
        exit 0
      fi
      sleep 1
    done
    
    # 如果优雅退出失败，强制杀死
    echo -e "${COLOR_YELLOW}Process ${specific_pid} did not stop gracefully, force killing...${COLOR_NC}"
    kill -9 "${specific_pid}" 2>/dev/null
    
    if ! kill -0 "${specific_pid}" 2>/dev/null; then
      echo -e "${COLOR_GREEN}Process ${specific_pid} force killed successfully.${COLOR_NC}"
    else
      echo -e "${COLOR_RED}Failed to kill process ${specific_pid}.${COLOR_NC}"
      exit 1
    fi
  else
    echo -e "${COLOR_YELLOW}Process ${specific_pid} is not running.${COLOR_NC}"
  fi
  exit 0
fi

# =================PID文件停止=================
if [ -f "${pid_file}" ]; then
  echo "Found PID file: ${pid_file}"
  
  # 读取PID文件中的所有进程ID
  pids_killed=0
  pids_not_found=0
  
  while read -r pid; do
    # 跳过空行
    if [ -z "$pid" ]; then
      continue
    fi
    
    echo "Processing PID: $pid"
    
    # 检查进程是否存在
    if kill -0 "$pid" 2>/dev/null; then
      echo "  Sending TERM signal to process $pid..."
      kill "$pid" 2>/dev/null
      
      # 等待进程优雅退出（最多5秒）
      grace_period=5
      for ((i=1; i<=grace_period; i++)); do
        if ! kill -0 "$pid" 2>/dev/null; then
          echo -e "  ${COLOR_GREEN}Process $pid stopped gracefully.${COLOR_NC}"
          pids_killed=$((pids_killed + 1))
          break
        fi
        sleep 1
      done
      
      # 如果进程仍然存在，强制杀死
      if kill -0 "$pid" 2>/dev/null; then
        echo -e "  ${COLOR_YELLOW}Process $pid did not stop gracefully, force killing...${COLOR_NC}"
        kill -9 "$pid" 2>/dev/null
        
        # 再次检查是否成功杀死
        sleep 1
        if ! kill -0 "$pid" 2>/dev/null; then
          echo -e "  ${COLOR_GREEN}Process $pid force killed.${COLOR_NC}"
          pids_killed=$((pids_killed + 1))
        else
          echo -e "  ${COLOR_RED}Failed to kill process $pid.${COLOR_NC}"
        fi
      fi
    else
      echo -e "  ${COLOR_YELLOW}Process $pid is not running.${COLOR_NC}"
      pids_not_found=$((pids_not_found + 1))
    fi
  done < "${pid_file}"
  
  # 删除PID文件
  rm -f "${pid_file}"
  echo -e "${COLOR_GREEN}PID file removed.${COLOR_NC}"
  
  # 显示统计信息
  echo "Processes killed: ${pids_killed}"
  echo "Processes not found: ${pids_not_found}"
  
else
  echo -e "${COLOR_YELLOW}No PID file found at: ${pid_file}${COLOR_NC}"
fi

# =================强制停止所有相关进程=================
if [ "${force_kill}" = true ]; then
  echo -e "${COLOR_YELLOW}Force killing all interviewer processes...${COLOR_NC}"
  
  # 查找所有相关的Python进程
  interviewer_pids=$(pgrep -f "interviewr.*runner\.py" 2>/dev/null || true)
  
  if [ -n "${interviewer_pids}" ]; then
    echo "Found interviewer processes: ${interviewer_pids}"
    
    # 逐个杀死进程
    for pid in ${interviewer_pids}; do
      echo "Force killing process: $pid"
      kill -9 "$pid" 2>/dev/null || true
    done
    
    # 等待一下然后验证
    sleep 2
    remaining_pids=$(pgrep -f "interviewr.*runner\.py" 2>/dev/null || true)
    
    if [ -z "${remaining_pids}" ]; then
      echo -e "${COLOR_GREEN}All interviewer processes killed successfully.${COLOR_NC}"
    else
      echo -e "${COLOR_RED}Some processes may still be running: ${remaining_pids}${COLOR_NC}"
    fi
  else
    echo -e "${COLOR_YELLOW}No interviewer processes found.${COLOR_NC}"
  fi
fi

# =================端口检查=================
echo ""
echo "Checking if service ports are still in use..."

# 检查默认端口是否还在使用
check_port_usage() {
  local port=$1
  local port_name=$2
  
  # 使用多种方法检查端口使用情况
  if netstat -ln 2>/dev/null | grep -q ":${port} " || \
     ss -ln 2>/dev/null | grep -q ":${port} " || \
     lsof -i ":${port}" >/dev/null 2>&1; then
    echo -e "${COLOR_YELLOW}Warning: ${port_name} port ${port} is still in use.${COLOR_NC}"
    
    # 显示占用端口的进程
    if command -v lsof >/dev/null 2>&1; then
      echo "Process using port ${port}:"
      lsof -i ":${port}" 2>/dev/null || true
    fi
    return 1
  else
    echo -e "${COLOR_GREEN}${port_name} port ${port} is free.${COLOR_NC}"
    return 0
  fi
}

# 检查开发环境端口
check_port_usage 9401 "gRPC (dev)"
check_port_usage 8741 "HTTP (dev)"

# 检查生产环境端口
check_port_usage 9402 "gRPC (prod)"
check_port_usage 8742 "HTTP (prod)"

# =================清理临时文件=================
echo ""
echo "Cleaning up temporary files..."

# 清理运行时目录中的临时文件
if [ -d "${run_dir}" ]; then
  # 清理日志文件（可选，保留最近的）
  if [ -d "${log_dir}" ]; then
    # 只删除超过7天的日志文件
    find "${log_dir}" -name "*.log" -type f -mtime +7 -delete 2>/dev/null || true
    echo "Old log files cleaned up."
  fi
  
  # 清理其他临时文件
  rm -f "${run_dir}"/*.tmp 2>/dev/null || true
  rm -f "${run_dir}"/*.lock 2>/dev/null || true
  
  echo "Temporary files cleaned up."
else
  echo "No run directory found."
fi

# =================完成信息=================
printf "\n"
echo -e "${COLOR_GREEN}Interviewer service stop operation completed. [$(date)]${COLOR_NC}"

# 如果有日志目录，提示查看日志
if [ -d "${log_dir}" ]; then
  echo "Log directory: ${log_dir}"
fi

printf "\n"