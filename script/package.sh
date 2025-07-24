#!/usr/bin/env bash

script_dir=$(
  cd $(dirname "$0") || exit 1
  pwd
)

work_dir=$(
  cd "${script_dir}"/.. || exit 1
  pwd
)

version=1.0.0

if [ ! -z "$1" ]; then
  version="$1"
fi

source "${script_dir}"/functions.sh


index=1
echo -e "\nstep $index -- This is going to generate package for yeying-interviewer"
output_dir=${work_dir}/output
if [ -d "${output_dir}" ]; then
  rm -rf "${output_dir}"
fi


index=$((index+1))
echo -e "\nstep $index -- prepare package files under directroy: ${output_dir}"
package_name=yeying-interviewer-${version}
file_name=$package_name.tar.gz
interviewer_dir=${output_dir}/${package_name}
mkdir -p "${interviewer_dir}"


index=$((index+1))
echo -e "\nstep $index -- copy necessary file to  ${interviewer_dir}"
# 拷贝安装脚本
cp -rf "${work_dir}"/script "${interviewer_dir}"/

# 拷贝配置文件
cp -rf "${work_dir}"/config "${interviewer_dir}"/

# 拷贝资源
cp -rf "${work_dir}"/resource "${interviewer_dir}"/

# 清理、打包并拷贝
if [ -d "${work_dir}"/dist ]; then
  rm -rf "${work_dir}"/dist
fi

if ! python_module_check_by_pip3 build ; then
  echo -e "${COLOR_RED}You have to install python module(build) manually firstly. ${COLOR_NC}"
  exit 1
fi
sed -i "s/version = .*/version = ${version}/g" setup.cfg
python3 -m build
cp "${work_dir}"/dist/*.whl "${interviewer_dir}"/


sleep 1
index=$((index+1))
echo -e "\nstep $index -- generate package file"
pushd "${output_dir}" || exit 2
tar -zcf "${file_name}" "${package_name}"
rm -rf "${package_name}"
popd  || exit 2


index=$((index+1))
echo -e "\nstep $index -- package : ${file_name} under [ ${output_dir} ] is ready. $(date)"