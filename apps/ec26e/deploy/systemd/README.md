# 服务部署

从应用目录执行 `poetry run python deploy/render.py --output /tmp/ec26e-deploy`，核对生成的解释器、工作目录、GPIO和配置目录后再手工安装用户服务。生成器不安装、不启动服务。
