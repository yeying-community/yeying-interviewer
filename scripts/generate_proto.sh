#!/bin/sh
# before running the script on macos, you should install protobuf with command `brew install protobuf`
base_name="${0##*/}"
current_directory=$(
  cd "$(dirname "$0")" || exit 1
  pwd
)

usage() {
  printf "Usage: %s\n \
    -d <You can specify the directory of yeying-idl, default third_party/yeying-idl\n \
    " "${base_name}"
}

cd "${current_directory}"/.. || exit 1
runtime_directory=$(pwd)

idl_dir=${runtime_directory}/third_party/yeying-idl

# For macos`s getopt, reference: https://formulae.brew.sh/formula/gnu-getopt
while getopts ":d:" o; do
  case "${o}" in
  d)
    idl_dir=${OPTARG}
    ;;
  *)
    usage
    ;;
  esac
done
shift $((OPTIND - 1))

language=python
app_type=server

output_dir=${idl_dir}/target/${app_type}/${language}/yeying
tool=${idl_dir}/script/compiler.sh
echo "${tool}"

# initialize the dependency library
# git submodule update --init
# git submodule foreach git pull origin main
# git submodule foreach git submodule update --init --depth=1

if [ -d "venv" ]; then
  source "venv/bin/activate"
fi

# generate code
if ! sh "${tool}" -t server -m common,rag -l "${language}"; then
  echo "Fail to compile proto file for interviewer!"
  exit 1
fi

target_dir=${runtime_directory}/yeying
if [ -d "${target_dir}/api" ]; then
  rm -rvf "${target_dir}"/api/*
fi

mkdir -p "${target_dir}"
cp -rvf "${output_dir}"/* "${target_dir}"/