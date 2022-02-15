from datetime import datetime
from pathlib import Path
from subprocess import check_output
from tempfile import TemporaryDirectory

VENDOR_DIR = Path(__file__).parent.parent / "pyswot" / "vendor"


def clone_repo(*, target_dir, repo="git@github.com:JetBrains/swot.git"):
    check_output(["git", "clone", "--depth", "1", repo, target_dir])
    process = check_output(["git", "rev-parse", "--short", "HEAD"], cwd=target_dir)
    return f"{repo}@{process.decode('utf-8')}"


def create_set(*, src, dest, varname, commit_id):
    with open(src) as f:
        var = [v for v in f.read().splitlines() if v]

    with open(dest, "w") as f:
        f.write(f"# Updated {datetime.now().isoformat()} from {commit_id}\n")
        f.write(f"{varname} = frozenset({repr(sorted(var))})\n")


def _get_key(rel_path):
    parts = list(rel_path.parts)

    # Strip txt
    parts[-1] = parts[-1][:-4]
    parts.reverse()

    return "." + ".".join(parts)


def create_dict(*, src, dest, varname, commit_id):
    var = {}
    domains = sorted(src.rglob("*.txt"))

    for domain in domains:
        with open(domain, "rb") as f:
            lines = f.read().splitlines()

        school_info = []
        for line in lines:
            if line:
                try:
                    i = line.decode("utf-8")
                except UnicodeDecodeError:
                    i = None
                school_info.append(i)

        var[_get_key(domain.relative_to(src))] = school_info

    with open(dest, "w") as f:
        f.write(f"# Updated {datetime.now().isoformat()} from {commit_id}\n")
        f.write("from typing import Dict, List, Optional\n")
        f.write(f"{varname}: Dict[str, List[Optional[str]]] = {repr(var)}\n")


if __name__ == "__main__":
    with TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        commit_id = clone_repo(target_dir=tmp_path)
        create_set(
            src=tmp_path / "lib" / "domains" / "stoplist.txt",
            dest=VENDOR_DIR / "stoplist.py",
            varname="STOPLIST",
            commit_id=commit_id,
        )
        create_set(
            src=tmp_path / "lib" / "domains" / "tlds.txt",
            dest=VENDOR_DIR / "tlds.py",
            varname="TLDS",
            commit_id=commit_id,
        )
        create_dict(
            src=tmp_path / "lib" / "domains",
            dest=VENDOR_DIR / "domains.py",
            varname="DOMAINS",
            commit_id=commit_id,
        )
