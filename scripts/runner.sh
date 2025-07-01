#!/usr/bin/env bash

# =================颜色定义=================
# 定义控制台输出颜色，用于增强可读性
COLOR_RED='\033[1;31m'      # 红色（错误信息）
COLOR_BLUE='\033[1;34m'     # 蓝色（环境标识）
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
    -d <Set debug mode.> \n \
    -g <Set gRPC server port.> \n \
    -h <Set HTTP server port.> \n \
    -e <Set run environment, such as dev or prod. default is dev> \n \
    " "${base_name}"
}

# =================默认配置=================
env=dev  # 默认运行环境为开发环境

# =================命令行参数解析=================
# 使用getopts解析命令行选项
while getopts ":dg:h:e:" o; do
  case "${o}" in
  d)
    # -d 参数：启用调试模式
    debug_param='--debug'
    ;;
  g)
    # -g 参数：设置gRPC服务器端口
    grpc_port=${OPTARG}
    ;;
  h)
    # -h 参数：设置HTTP服务器端口
    http_port=${OPTARG}
    ;;
  e)
    # -e 参数：设置运行环境
    env=${OPTARG}
    ;;
  *)
    # 无效参数：显示用法并退出
    usage
    exit 1
    ;;
  esac
done
shift $((OPTIND - 1))  # 移除已处理的参数

# =================环境配置=================
# 根据运行环境设置默认端口
if [ "${env}" == "dev" ]; then
  if [ -z "${http_port}" ]; then
    http_port=8741
  fi

  if [ -z "${grpc_port}" ]; then
    grpc_port=9401
  fi
elif [ "${env}" == "prod" ]; then
  if [ -z "${http_port}" ]; then
    http_port=8742
  fi

  if [ -z "${grpc_port}" ]; then
    grpc_port=9402
  fi
else
  echo "Not support environment parameter!"
  usage
  exit 1
fi

# =================启动信息显示=================
index=1
printf "\n"
echo -e "step $index -- This is going to start interviewer service under ${COLOR_BLUE} ${env} ${COLOR_NC} environment. [$(date)]"
echo "work dir=${work_dir}, grpc port=${grpc_port}, http port=${http_port}"

# =================目录结构设置=================
# 定义运行时需要的各个目录
run_dir=${work_dir}/run                    # 运行时目录
src_conf_dir=${work_dir}/config           # 源配置目录
des_conf_dir=${run_dir}/config            # 目标配置目录
des_log_dir=${run_dir}/log                # 日志目录

# 创建必要的目录结构
if [ ! -d "${run_dir}" ]; then
  mkdir -p "${run_dir}"
fi

if [ ! -d "${des_log_dir}" ]; then
  mkdir -p "${des_log_dir}"
fi

if [ ! -d "${des_conf_dir}" ]; then
  mkdir -p "${des_conf_dir}"
fi

# =================配置文件准备=================
# 如果运行目录中没有配置文件，则从源目录复制
if [ ! -f "${des_conf_dir}/config.toml" ]; then
  cp -rf "${src_conf_dir}"/config.toml "${des_conf_dir}/"
fi

# =================清理已有进程=================
index=$((index+1))
printf "\n"
echo -e "step $index -- kill existing processes if any"

# 定义PID文件路径
pid_file=${run_dir}/pid.txt

# 杀死已存在的进程
if [ -f "${pid_file}" ]; then
  # 逐行读取PID文件中的进程ID
  while read -r pid; do
    # 检查进程是否存在且非空
    if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
      echo "Killing process $pid"
      kill "$pid"              # 优雅终止进程
      sleep 1
      # 如果进程仍然存在，强制杀死
      if kill -0 "$pid" 2>/dev/null; then
        echo "Force killing process $pid"
        kill -9 "$pid"         # 强制终止进程
      fi
    fi
  done < "${pid_file}"
  rm -f "${pid_file}"          # 删除PID文件
fi

# =================Python环境准备=================
# 激活虚拟环境（如果存在）
if [ -d "venv" ]; then
  source "venv/bin/activate"
elif [ -d ".venv"  ]; then
  source ".venv/bin/activate"
fi

# =================依赖检查=================
# 检查Python依赖是否已安装
python3 -c "import toml, peewee, pydantic" 2>/dev/null
if [ $? -ne 0 ]; then
  echo -e "${COLOR_RED}You need to install required Python modules first: ${COLOR_NC}"
  echo "pip install toml peewee pydantic grpcio grpcio-tools"
  exit 1
fi

# 切换到运行目录
cd "${run_dir}" || exit 1

# =================Python路径设置=================
# 将工作目录添加到Python路径中
PYTHONPATH="${PYTHONPATH}:${work_dir}"
export PYTHONPATH

# =================启动服务=================
index=$((index+1))
printf "\n"
echo -e "step $index -- start interviewer service"

if [ "${env}" == "dev" ]; then
  # 开发环境：直接运行Python脚本
  bin_file="${work_dir}/interview/runner.py"
  command="python3 ${bin_file}"

  # 使用nohup在后台运行服务，并重定向输出到日志文件
  nohup ${command} ${debug_param} \
    --config "${des_conf_dir}/config.toml" \
    --grpc-port "${grpc_port}" \
    --http-port "${http_port}" \
    --env "${env}" > "${des_log_dir}/start.log" 2>&1 &
else
  # 生产环境：假设已安装包，使用命令行工具
  nohup interviewer ${debug_param} \
    --config "${des_conf_dir}/config.toml" \
    --grpc-port "${grpc_port}" \
    --http-port "${http_port}" \
    --env "${env}" > "${des_log_dir}/start.log" 2>&1 &
fi

# 将新启动的进程PID保存到文件
echo $! >> "${pid_file}"

# =================服务状态检查=================
index=$((index+1))
printf "\n"
echo -e "step $index -- check service port"

# 检查服务端口是否已打开的函数
check_service_port() {
  local max_attempts=$1    # 最大尝试次数
  local interval=$2        # 检查间隔（秒）
  local port=$3           # 要检查的端口

  # 循环检查端口状态
  for ((i=1; i<=max_attempts; i++)); do
    # 使用多种方法检查端口是否开放
    if netstat -ln 2>/dev/null | grep -q ":${port} " || \
       ss -ln 2>/dev/null | grep -q ":${port} " || \
       lsof -i ":${port}" >/dev/null 2>&1; then
      return 0  # 端口已开放
    fi
    sleep $interval  # 等待指定间隔
  done
  return 1  # 端口检查失败
}

# 检查服务是否成功启动（最多尝试10次，每次间隔1秒）
if check_service_port 10 1 "$grpc_port"; then
  echo "Interviewer service [gRPC port: ${grpc_port}] started successfully."
else
  echo -e "${COLOR_RED}Interviewer service [gRPC port: ${grpc_port}] failed to start. ${COLOR_NC}"
  echo "Check log file: ${des_log_dir}/start.log"
fi

# =================完成信息=================
printf "\n"
echo "Interviewer service startup operation finished. [$(date)]"
echo "Log file: ${des_log_dir}/start.log"
echo "PID file: ${pid_file}"