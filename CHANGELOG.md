# Unreleased
### Add
- Support for other tabulate table formats when listing
- Support for different date formats (in configuration)
- Support for tags
- Date configuring: configure when a date is green, yellow or red (threshold values)
- Configure colouring for priority levels

# 1.0.3
### Added
- Seperated usage information and options for each command into its own help command (eg. `pytd help add`)

### Changed
- Changed the main `pytd help` text

# 1.0.2
### Added
- Can now remove due dates from tasks with `pytd edit 'name' -d remove`

# 1.0.1
### Changed
- Made date format consistent in info
- Made info say 'Due Date: None' instead of printing the stored due date when year is -1 (no due date)
- Made description not print in info if empty
