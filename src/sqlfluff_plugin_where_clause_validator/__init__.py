"""An example of a custom rule implemented through the plugin system.

This uses the rules API supported from 0.4.0 onwards.
"""

from typing import List, Type

from sqlfluff.core.config import ConfigLoader
from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules import BaseRule


@hookimpl
def get_rules() -> List[Type[BaseRule]]:
    """Get plugin rules.

    NOTE: It is much better that we only import the rule on demand.
    The root module of the plugin (i.e. this file which contains
    all of the hook implementations) should have fully loaded before
    we try and import the rules. This is partly for performance
    reasons - but more because the definition of a BaseRule requires
    that all of the get_configs_info() methods have both been
    defined _and have run_ before so all the validation information
    is available for the validation steps in the meta class.
    """
    # i.e. we DO recommend importing here:
    from sqlfluff_plugin_where_clause_validator.rules import (
        Rule_WhereClauseValidator_L001,
    )  # noqa: F811

    return [Rule_WhereClauseValidator_L001]


@hookimpl
def load_default_config() -> dict:
    """Loads the default configuration for the plugin."""
    return ConfigLoader.get_global().load_config_resource(
        package="sqlfluff_plugin_where_clause_validator",
        file_name="plugin_default_config.cfg",
    )


@hookimpl
def get_configs_info() -> dict:
    """Get rule config validations and descriptions."""
    return {}
