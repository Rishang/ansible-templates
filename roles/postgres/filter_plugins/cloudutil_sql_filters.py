"""Expose the role's schema gateway as Ansible filters."""

from pathlib import Path
import sys
from typing import Any

# Role plugins are not Python packages when Ansible loads them, so add the
# sibling schema directory before importing its standalone gateway module.
schemas_path = str((Path(__file__).parent.parent / "schemas").resolve())
if schemas_path not in sys.path:
    sys.path.insert(0, schemas_path)

from cloudutil_sql import sql_config, sql_config_file  # noqa: E402


class FilterModule:
    def filters(self) -> dict[str, Any]:
        return {
            "sql_config": sql_config,
            "sql_config_file": sql_config_file,
        }
