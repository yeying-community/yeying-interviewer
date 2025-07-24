#!/bin/sh

# 安装interviewer到系统中
# before running the script on macos, you should install protobuf with command `brew install protobuf`

script_dir=$(
  cd $(dirname "$0") || exit 1
  pwd
)

work_dir=$(
  cd "${script_dir}"/.. || exit 1
  pwd
)

usage() {
  printf "Usage: %s\n \
    -e <Set the environment, such as dev or prod.> \n \
    " "${0##*/}"
}

# For macos`s getopt, reference: https://formulae.brew.sh/formula/gnu-getopt
while getopts ":e:" o; do
  case "${o}" in
  e)
    env=${OPTARG}
    ;;
  *)
    usage
    ;;
  esac
done
shift $((OPTIND - 1))

if [ -z "${env}" ]; then
  usage
fi

source "${work_dir}"/config/config.toml

echo "database=${dbname}, user=${user}"
echo "The work directory=${work_dir}, environment=${env}"
python_package=${work_dir}/yeying-interviewer-${version}.whl

# 如果用到了匹配字符，这里不能对python_package变量加引号
# shellcheck disable=SC2086
pip3 uninstall -y yeying-interviewer
pip3 install "${python_package}"
runner=${script_dir}/runner.sh
${runner} -e "${env}"
