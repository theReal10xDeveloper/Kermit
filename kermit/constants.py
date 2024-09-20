from pathlib import Path
import kermit


def get_metagpt_package_root():
    """Get the root directory of the installed package."""
    package_root = Path(kermit.__file__).parent.parent
    for i in (".git", ".project_root", ".gitignore"):
        if (package_root / i).exists():
            break
    else:
        package_root = Path.cwd()

    # logger.info(f"Package root set to {str(package_root)}")
    return package_root


CONFIG_ROOT = Path.home() / ".kermit"
PACKAGE_ROOT = get_metagpt_package_root()
DEFAULT_WORKSPACE_ROOT = Path.home() / "kermit"
