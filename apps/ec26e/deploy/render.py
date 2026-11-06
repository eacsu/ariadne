"""生成部署配置，不安装或启动服务。"""
import argparse
from pathlib import Path
import sys
p=argparse.ArgumentParser()
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
for source in (root/'deploy').rglob('*'):
    if source.suffix not in {'.desktop','.service'}: continue
    dest=a.output/source.relative_to(root/'deploy')
    dest.parent.mkdir(parents=True,exist_ok=True)
    text=source.read_text().replace('@APP_ROOT@',str(root)).replace('@PYTHON@',sys.executable).replace('@USER_HOME@',str(Path.home()))
    dest.write_text(text)
