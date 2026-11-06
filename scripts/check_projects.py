"""检查依赖边界并逐项目运行 Python 3.10 测试，保留真实退出码。"""
import ast
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ['packages/solver', 'packages/vision', 'packages/devices', 'apps/ec26e']
failed = False
for project in PROJECTS:
    root = ROOT / project
    if project.startswith('packages/'):
        owner = 'ariadne_' + root.name
        for path in (root / 'src').rglob('*.py'):
            for node in ast.walk(ast.parse(path.read_text())):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or ''] if isinstance(node, ast.ImportFrom) else []
                for name in names:
                    top = name.split('.')[0]
                    if top == 'ec_26_e' or (top.startswith('ariadne_') and top != owner) or top == 'tests':
                        raise SystemExit(f'{path}: forbidden dependency {name}')
    python = root / '.venv/bin/python'
    subprocess.run([str(python), '-c', 'import sys; assert sys.version_info[:2] == (3,10), sys.version'], check=True)
    result = subprocess.run([str(python), '-m', 'pytest', '-q'], cwd=root)
    failed |= result.returncode != 0
sys.exit(int(failed))
