# 夜莺面试官 (Yeying Interviewer)

## 快速开始

### 1. 依赖安装

```bash
# 安装 Python 依赖
pip install -r requirements.txt
```

### 2. 配置说明

主配置文件 `config.toml` 包含以下重要配置：

```toml
[server]
grpc_port = 9401    # gRPC服务端口（开发环境）
http_port = 8741    # HTTP服务端口（开发环境）

[database]
type = "sqlite"
name = "data/interviewer.db"

[log]
filename = "log/interviewer.log"
level = "INFO"
```

### 3. 启动服务

#### 方式一：使用启动脚本（推荐）

```bash
# 开发环境启动（默认端口：gRPC=9401, HTTP=8741）
./scripts/runner.sh -e dev

# 生产环境启动（默认端口：gRPC=9402, HTTP=8742）
./scripts/runner.sh -e prod

# 自定义端口启动
./scripts/runner.sh -e dev -g 9500 -h 8500

# 启用调试模式
./scripts/runner.sh -d -e dev
```

#### 方式二：直接运行 Python

```bash
# 基础启动
PYTHONPATH=. python interview/runner.py --config config.toml --env dev

# 指定端口启动
PYTHONPATH=. python interview/runner.py \
  --config config.toml \
  --grpc-port 9401 \
  --http-port 8741 \
  --env dev

# 启用调试模式
PYTHONPATH=. python interview/runner.py --debug --config config.toml --env dev
```

### 4. 停止服务

```bash
# 正常停止服务
./scripts/stop.sh

# 强制停止所有相关进程
./scripts/stop.sh -f

# 停止指定进程
./scripts/stop.sh -p <PID>
```

### 5. 服务验证

启动后可以通过以下方式验证服务状态：

```bash
# 检查 gRPC 端口
netstat -ln | grep 9401

# 检查 HTTP 端口  
netstat -ln | grep 8741

# 查看服务日志
tail -f run/log/start.log
```

## 测试

### 运行全部测试

```bash
# 运行所有测试
python -m pytest test/ -v

# 运行特定测试文件
python -m pytest test/test_config.py -v

# 运行测试并显示覆盖率
python -m pytest test/ -v --cov=interview
```

### 测试说明

- `test_config.py`：配置系统测试
- `test_database.py`：数据库连接和迁移测试  
- `test_models.py`：数据模型测试
