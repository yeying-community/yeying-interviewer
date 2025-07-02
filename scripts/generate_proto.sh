#!/bin/bash

# 设置路径
PROTO_DIR="app/apis/proto"
OUTPUT_DIR="app/apis/generated"
PROJECT_ROOT=$(dirname $(dirname $(realpath $0)))

cd "$PROJECT_ROOT"

echo "🔧 开始生成gRPC代码..."

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 生成Python gRPC代码
python -m grpc_tools.protoc \
    --proto_path="$PROTO_DIR" \
    --python_out="$OUTPUT_DIR" \
    --grpc_python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/rag.proto"

echo "✅ gRPC代码生成完成！"
echo "生成文件："
echo "  - $OUTPUT_DIR/rag_pb2.py"
echo "  - $OUTPUT_DIR/rag_pb2_grpc.py"

# 修复导入路径
sed -i 's/import rag_pb2/from . import rag_pb2/' "$OUTPUT_DIR/rag_pb2_grpc.py"

# 创建__init__.py文件
echo "# Generated gRPC code" > "$OUTPUT_DIR/__init__.py"

echo "🎉 完成！"