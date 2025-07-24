import jinja2
import sys
import os

# 获取命令行参数
args = sys.argv

src_config = args[1]
des_config = args[2]
cert_dir = args[3]
http_port = args[4]
grpc_port = args[5]

# 从模板文件加载模板
src_directory = os.path.dirname(src_config)
src_filename = os.path.basename(src_config)
env = jinja2.Environment(loader=jinja2.FileSystemLoader(src_directory))
template = env.get_template(src_filename)

# 渲染模板并传入参数
rendered_yaml = template.render(cert_dir=cert_dir, http_port=http_port, grpc_port=grpc_port)

# 将渲染后的内容写入文件
with open(des_config, 'w') as file:
    file.write(rendered_yaml)
