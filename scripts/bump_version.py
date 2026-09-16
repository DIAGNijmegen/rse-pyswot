import re
from pathlib import Path

PYPROJECT = Path(__file__).parent.parent / "pyproject.toml"

VERSION_PATTERN = re.compile(
    r'^(?P<prefix>version\s*=\s*")(?P<version>\d+\.\d+\.\d+)(?P<suffix>")',
    flags=re.MULTILINE,
)


def bump_patch_version(*, version: str) -> str:
    major, minor, patch = version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


def bump_pyproject_patch_version(*, path: Path = PYPROJECT) -> str:
    contents = path.read_text()

    match = VERSION_PATTERN.search(contents)
    if match is None:
        raise ValueError(f"No version found in {path}")

    new_version = bump_patch_version(version=match.group("version"))

    updated = VERSION_PATTERN.sub(
        rf"\g<prefix>{new_version}\g<suffix>", contents, count=1
    )
    path.write_text(updated)

    return new_version


def main() -> int:
    new_version = bump_pyproject_patch_version()
    print(new_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
