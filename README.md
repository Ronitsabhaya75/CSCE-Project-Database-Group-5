# CSCE-Project-Database-Group-5

# Auto Company Database System - Team [Insert Team Number]

This repository contains the source code, database schema, and documentation for our CSCE 4350 Database Systems project. We are building a unified Command-Line Interface (CLI) backed by a PostgreSQL database hosted on the UNT CELL machine.

## 👥 Team Roles & Responsibilities

To ensure we hit our April 19th deadline, work is divided into four distinct domains. **Check the README in your assigned folder for your specific UI features.**

* **[Your Name] (Integration & Marketing Lead)**
    * **Folder:** `src/marketing/`
    * **Duties:** Repo setup, master database connection script, Master Login Menu, and the Marketing OLAP CLI features.
* **[Name 2] (Customer Interface Developer)**
    * **Folder:** `src/customer/`
    * **Duties:** Building the Online Customer CLI to search inventory and process mock purchases.
* **[Name 3] (Dealer Interface Developer)**
    * **Folder:** `src/dealer/`
    * **Duties:** Building the Vehicle Locator CLI for dealers to check local/global stock and process sales.
* **[Name 4] (Project Manager & DBA)**
    * **Folder:** `sql/`
    * **Duties:** Managing the `auto_company_db` on the CELL machine, writing complex test queries, handling concurrency, and formatting final checkpoint submissions.

---

## 📅 Development Schedule (Target: April 19)

| Date | Phase | Task | Assignee |
| :--- | :--- | :--- | :--- |
| **Apr 8** | Checkpoint 2 | Submit relational schema, UI plans, and schedule. | [Name 4] |
| **Apr 9** | Setup | Repo setup, DB connection class, and basic UI menus. | [Your Name] |
| **Apr 10-11** | Dev Phase 1 | Build Marketing & Customer Interfaces. | [Your Name] & [Name 2] |
| **Apr 12** | CP3 Check-in | Test the two compiled interfaces for CP3. | [Name 4] |
| **Apr 13** | Checkpoint 3 | Submit updated schedule and two executables. | [Name 4] |
| **Apr 14-15** | Dev Phase 2 | Build Dealer Interface & final purchase logic. | [Name 3] & [Name 2] |
| **Apr 16** | Integration | Bring all CLI menus into one `main` program. | Entire Team |
| **Apr 17-18** | Bug Squashing | Fix broken queries, update E-R diagram, final tests. | Entire Team |
| **Apr 19** | Final Delivery | Submit `Project-Team#.zip` to Blackboard. | [Name 4] |

---

## 🌿 Git Workflow (Important!)

We are using a `dev` branch system to prevent code conflicts.
1. **Never push directly to `main`.** `main` is only for code that is 100% finished and ready for the professor.
2. **Pull from `dev` daily:** Always make sure you have the latest code.
3. **Create your own branches:** When working on your interface, create a branch off of `dev` (e.g., `git checkout -b feature-customer-menu`).
4. **Merge to `dev`:** When your feature works, open a Pull Request to merge your branch into `dev`.
