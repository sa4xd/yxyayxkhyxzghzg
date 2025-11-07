FROM python:3.10-slim

# 安装必要依赖（uvloop、cryptography、PySocks）
RUN pip install --no-cache-dir \
    uvloop \
    cryptography \
    PySocks

# 设置 Python 绑定低端端口权限（如 443）
RUN apt-get update && apt-get install --no-install-recommends -y libcap2-bin \
    && setcap cap_net_bind_service=+ep /usr/local/bin/python3.10 \
    && apt-get purge -y --auto-remove libcap2-bin \
    && rm -rf /var/lib/apt/lists/*

# 创建非 root 用户
RUN useradd -m -u 10000 tgproxy

USER tgproxy
WORKDIR /home/tgproxy/

# 拷贝代码并设置权限
COPY --chown=tgproxy:tgproxy mtprotoproxy.py config.py ./

# 使用更现代的启动方式
CMD ["python3", "-X", "utf8", "mtprotoproxy.py"]
