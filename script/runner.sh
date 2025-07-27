#!/usr/bin/env bash

COLOR_RED='\033[1;31m'
COLOR_BLUE='\033[1;34m'
COLOR_NC='\033[0m'

base_name="${0##*/}"
script_dir=$(
  cd $(dirname "$0") || exit 1
  pwd
)

source "${script_dir}"/functions.sh

work_dir=$(
  cd "${script_dir}"/.. || exit 1
  pwd
)

usage() {
  printf "Usage: %s\n \
    -d <Set debug mode.> \n \
    -h <Set http proxy port.> \n \
    -g <Set grpc port.> \n \
    -e <Set run environment, such as dev or prod. default is dev> \n \
    -t <Set http tls enable> \n \
    " "${base_name}"
}

env=dev
tls=false

# For macos`s getopt, reference: https://formulae.brew.sh/formula/gnu-getopt
while getopts ":dth:g:e:" o; do
  case "${o}" in
  t)
    tls=true
    ;;
  d)
    debug_param='--debug'
    ;;
  h)
    http_port=${OPTARG}
    ;;
  g)
    grpc_port=${OPTARG}
    ;;
  e)
    env=${OPTARG}
    ;;
  *)
    usage
    ;;
  esac
done
shift $((OPTIND - 1))

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

# 设置 base_id
base_id=${http_port}

index=1
printf "\n"
echo -e "step $index -- This is going to start interviewer under ${COLOR_BLUE} ${env} ${COLOR_NC} environment. [$(date)]"
echo "work dir=${work_dir}, http port=${http_port}, grpc port=${grpc_port}"

run_dir=${work_dir}/run
python_script=${work_dir}/script/load_template.py
password_file=${run_dir}/password
cert_dir=${run_dir}/cert

src_conf_dir=${work_dir}/config
src_resource_dir=${work_dir}/resource/${env}

des_conf_dir=${run_dir}/config
des_log_dir=${run_dir}/log
identity_file=${run_dir}/interviewer.id

if [ ! -d "${run_dir}" ]; then
  mkdir -p "${run_dir}"
fi

if [ ! -d "${des_log_dir}" ]; then
  mkdir -p "${des_log_dir}"
fi

if [ ! -d "${des_conf_dir}" ]; then
  mkdir -p "${des_conf_dir}"
fi

if [ ! -f "${des_conf_dir}/config.toml" ]; then
  cp -rf "${src_conf_dir}"/config.toml "${des_conf_dir}/"
fi

if [ ! -d "${src_resource_dir}" ]; then
  mkdir -p "${src_resource_dir}"
fi
if [ ! -f "${identity_file}" ]; then
  echo -e "${COLOR_RED} ${identity_file} is necessary. ${COLOR_NC}"
  exit 2
fi

index=$((index+1))
printf "\n"
echo -e "step $index -- kill process if these exist"
# 定义保存进程ID的文件路径
pid_file=${run_dir}/pid.txt
kill_process_with_pid_file "${pid_file}" true

if [ -d "venv" ]; then
  source "venv/bin/activate"
elif [ -d ".venv"  ]; then
  source ".venv/bin/activate"
fi

if ! python_module_check_by_pip3 Jinja2 ; then
  echo -e "${COLOR_RED}You have to install python module(Jinja2) manually firstly. ${COLOR_NC}"
  exit 1
fi
envoy_array=("/usr/bin/envoy" "/usr/local/bin/envoy")
envoy_bin=$(get_string_by_os "${envoy_array[@]}")
envoy_config=""
if [ "$tls" = true ]; then
    envoy_config="envoy.tls.yaml"
else
    envoy_config="envoy.yaml"
fi
python3 "${python_script}" \
  "${src_conf_dir}/${envoy_config}" "${des_conf_dir}/envoy.yaml" "${cert_dir}" "${http_port}" "${grpc_port}"

cd "${run_dir}" || exit 1

read -r -s -p "Please Enter Identity Password: " IDENTITY_PASSWORD

# 将密码写入文件，macos不支持echo命令的-n选项，为了避免写入文件存在换行符，使用printf替代。
printf "%s" "${IDENTITY_PASSWORD}" >"${password_file}"
printf "\n"

PYTHONPATH="${PYTHONPATH}:${work_dir}"
export PYTHONPATH

index=$((index+1))
printf "\n"
echo -e "step $index -- start interviewer service"
if [ "${env}" == "dev" ]; then
  bin_file="${work_dir}/interviewer/runner.py"
  command="python3 ${bin_file}"
  if [ ! -f "${bin_file}" ]; then
    command=interviewer
  fi

  nohup ${command} ${debug_param} \
    --port "${grpc_port}" \
    --identityFile "${identity_file}" \
    --password "${password_file}" \
    --certDir "${cert_dir}" > "${des_log_dir}/start.log" 2>&1  &
else
  nohup interviewer ${debug_param} \
    --port "${grpc_port}" \
    --identityFile "${identity_file}" \
    --password "${password_file}" \
    --certDir "${cert_dir}" > "${des_log_dir}/start.log" 2>&1 &
fi
echo $! >> "${pid_file}"

index=$((index+1))
printf "\n"
echo -e "step $index -- check grpc port of interviewer"
if check_service_port 10 1 "$grpc_port"; then
  echo "grpc[port: ${grpc_port}] of interviewer started successfully."
else
  echo -e "${COLOR_RED}grpc[prot: ${grpc_port}] of interviewer Not started yet. ${COLOR_NC}"
fi

if [ -f "${password_file}" ]; then
  rm -rf "${password_file}"
fi

index=$((index+1))
printf "\n"
echo -e "step $index -- start envoy proxy"
# 启动代理，为了确保一台机器上运行多个envoy实例，需要使用不同base-id参数
nohup "${envoy_bin}" --base-id "${base_id}" -c "${des_conf_dir}/envoy.yaml" > "${des_log_dir}/envoy.log" 2>&1 &
echo $! >> "${pid_file}"


echo "interviewer startup operation finished. [$(date)]"
