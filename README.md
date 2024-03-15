# SQLFluff Where-Clause Validator Plugin

This SQLFluff plugin extends the capabilities of SQLFluff to detect UPDATE and DELETE SQL statements that do not include a WHERE clause. The absence of a WHERE clause in such statements can lead to unintentional bulk updates or deletions, potentially causing data integrity issues. This plugin aims to mitigate such risks by enforcing the presence of a WHERE clause, promoting safer SQL practices.

## Installation

The plugin can be installed via pip (or pipenv, if you prefer). Ensure you have SQLFluff installed in your environment before installing this plugin.
Using pip

```bash

pip install sqlfluff-where-clause-validator
```

Using pipenv

```bash
pipenv install sqlfluff-where-clause-validator
```

## Usage

Once installed, the plugin is automatically recognized by SQLFluff, and its rules are applied during linting operations. To lint your SQL files:

```bash

sqlfluff lint path/to/your/sql_files
```
If an UPDATE or DELETE statement without a WHERE clause is detected, SQLFluff will report a linting error, indicating the file, line number, and nature of the issue.

## Configuration

No additional configuration is needed to enable the plugin after installation. It seamlessly integrates with SQLFluff's existing linting process.

## Contributing

Contributions to the plugin are welcome! Whether it's reporting issues, submitting fixes, or proposing new features, your input is valuable. Please refer to the project's contribution guidelines for more information on how to contribute.
Reporting Issues

Please use the GitHub issue tracker to report bugs or suggest enhancements.
## Submitting Pull Requests

1. Fork the repository and create your branch from main.
    - If you've added code, add tests that cover your changes.
1. Ensure your code passes existing tests and linting checks.
1. Submit your pull request.

## License

This plugin is distributed under the MIT License, allowing for both personal and commercial use.
Support

If you encounter any problems or have questions, please file an issue on GitHub. For more detailed inquiries or suggestions, feel free to contact the maintainers directly via email.
