# 夜莺面试官 (Yeying Interviewer)

## 项目简介

夜莺面试官是一个基于 DDD（领域驱动设计）架构的智能面试系统，支持面试管理、RAG 问答、数字人交互等功能，采用 gRPC 微服务架构。

## 目录结构

```
yeying-interviewer/
├── interview/              # 业务主代码（DDD架构）
│   ├── application/        # 应用服务层
│   │   ├── resume/         # 简历管理服务
│   │   ├── room/           # 面试间管理服务
│   │   └── session/        # 面试会话服务
│   ├── domain/             # 领域模型层
│   │   ├── models.py       # 数据模型定义
│   │   ├── resume/         # 简历领域仓储
│   │   ├── room/           # 面试间领域仓储
│   │   └── session/        # 会话领域仓储
│   ├── infrastructure/     # 基础设施层
│   │   ├── database/       # 数据库连接和迁移
│   │   ├── auth.py         # 认证服务
│   │   ├── logger.py       # 日志服务
│   │   └── exceptions.py   # 异常处理
│   ├── interfaces/         # 接口层（gRPC服务等）
│   │   ├── interview_server.py  # 面试服务
│   │   ├── rag_server.py        # RAG服务
│   │   ├── digital_server.py    # 数字人服务
│   │   └── interceptors.py      # gRPC拦截器
│   ├── config/             # 配置管理
│   │   └── config.py       # 配置加载与管理
│   └── runner.py           # 启动主程序
├── config.toml             # 主配置文件
├── scripts/                # 项目脚本
│   ├── runner.sh           # Linux/macOS 启动脚本
│   ├── stop.sh             # 停止脚本
│   ├── generate_proto.sh   # 生成 gRPC proto 文件
│   └── functions.sh        # 通用函数库
├── test/                   # 测试代码
│   ├── test_config.py      # 配置测试
│   ├── test_database.py    # 数据库测试
│   └── test_models.py      # 模型测试
├── run/                    # 运行时目录（脚本自动创建）
│   ├── log/                # 日志文件
│   ├── config/             # 运行时配置
│   └── pid.txt             # 进程ID文件
├── data/                   # 数据目录
│   └── interviewer.db      # SQLite数据库
└── requirements.txt        # Python依赖包
```

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

## 端口配置

### 开发环境 (dev)
- gRPC 端口：9401
- HTTP 端口：8741

### 生产环境 (prod)
- gRPC 端口：9402
- HTTP 端口：8742

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

所有测试都通过表示系统基础架构运行正常。

## 开发说明

### 架构特点

- **DDD架构**：清晰的分层设计，业务逻辑集中在领域层
- **gRPC微服务**：支持高性能的跨语言通信
- **多数据库支持**：SQLite（开发）、PostgreSQL/MySQL（生产）
- **配置管理**：基于 TOML 的配置文件，支持环境变量覆盖
- **日志管理**：轮转日志，支持不同级别

### 当前状态

项目目前处于基础架构完成阶段：

- ✅ 配置系统完整
- ✅ 数据库架构和迁移
- ✅ 基础模型定义
- ✅ 日志和异常处理
- 🔄 应用服务层开发中
- 🔄 gRPC接口实现中
- 🔄 protobuf定义待完成

### 扩展开发

1. **添加新的业务模型**：在 `interview/domain/models.py` 中定义
2. **实现应用服务**：在 `interview/application/` 对应模块中实现
3. **添加gRPC接口**：在 `interview/interfaces/` 中实现服务端
4. **编写测试**：在 `test/` 目录中添加相应测试

## 故障排除

### 常见问题

1. **端口已被占用**
   ```bash
   # 查看端口占用
   lsof -i :9401
   # 停止服务后重试
   ./scripts/stop.sh -f
   ```

2. **模块导入错误**
   ```bash
   # 确保设置了 PYTHONPATH
   export PYTHONPATH=.
   ```

3. **数据库权限问题**
   ```bash
   # 检查数据目录权限
   ls -la data/
   # 确保有读写权限
   chmod 755 data/
   ```

4. **日志文件权限**
   ```bash
   # 检查日志目录
   ls -la run/log/
   # 查看详细错误
   cat run/log/start.log
   ```

## 脚本参考

### runner.sh 参数

```bash
Usage: runner.sh
    -d <Set debug mode.>
    -g <Set gRPC server port.>
    -h <Set HTTP server port.>
    -e <Set run environment, such as dev or prod. default is dev>
```

### stop.sh 参数

```bash
Usage: stop.sh
    -f <Force kill all interviewer processes.>
    -p <Kill specific process by PID.>
    -h <Show this help message.>
```

## 代码质量

- **测试覆盖**：核心功能都有对应的单元测试
- **代码注释**：所有核心代码都有详细的中文注释
- **类型提示**：使用 Pydantic 进行数据验证
- **错误处理**：完善的异常处理机制
- **日志记录**：详细的日志记录便于调试

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/新功能`)
3. 提交更改 (`git commit -am '添加新功能'`)
4. 推送到分支 (`git push origin feature/新功能`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

如需扩展业务、接入新服务或有其它问题，欢迎随时联系维护者。 