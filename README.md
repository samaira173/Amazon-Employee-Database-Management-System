# Amazon Employee Database Management System

A menu-driven command-line Human Resource Management System (HRMS) built using Python and MySQL to handle corporate staff records, hierarchical reporting structures, and payroll processing.

## Key Features
- **Relational Schema Design:** Maps out database integrity across two connected tables (personal details and manager/salary tracks) utilizing primary key constraints.
- **Data Integration & Cleaning:** Built custom Python logic for data parsing, string validation, data sanitization, and text-based regular expression lookups for live filtering.
- **Automated State Recovery:** Implemented robust exception handling (`try-except` blocks) to build a self-recovering sync mechanism that aligns the local Python runtime state with the active backend MySQL database upon application boot.
- **Advanced Data Operations:** Written custom sorting and multi-criteria searching algorithms directly into the terminal interface for seamless record updates and tracking.

## Tech Stack
- **Language:** Python 3
- **Database System:** MySQL
- **Interface/Connectivity:** MySQL Connector for Python
