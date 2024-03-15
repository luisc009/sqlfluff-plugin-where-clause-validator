from sqlfluff.core.rules import (
    BaseRule,
    LintResult,
    RuleContext,
)

from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_WhereClauseValidator_L001(BaseRule):
    """All UPDATE and DELETE statements must have a WHERE clause."""

    name = "where_clause_validator_L001"
    description = "All UPDATE and DELETE statements must have a WHERE clause."
    groups = ("all",)
    crawl_behaviour = SegmentSeekerCrawler({"update_statement", "delete_statement"})
    is_fix_compatible = False
    enabled = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _eval(self, context: RuleContext):
        if not self.enabled:
            return None
        types = ["update_statement", "delete_statement"]
        if context.segment.type in types:
            if "where_clause" not in [d.type for d in context.segment.segments]:
                return LintResult(
                    anchor=context.segment,
                    description=f"{context.segment.type.upper()} statement missing WHERE clause.",
                )
