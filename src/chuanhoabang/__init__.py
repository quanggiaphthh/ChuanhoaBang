"""ChuanhoaBang offline DOCX table analyzer (technical preview)."""
from .core import (TableError, audit, propose, propose_header, propose_unclip_row_height,
                   apply, available_profiles, POLICY_VERSION)

__all__ = ["TableError", "audit", "propose", "propose_header", "propose_unclip_row_height",
           "apply", "available_profiles", "POLICY_VERSION"]
__version__ = "0.1.0.dev0"
