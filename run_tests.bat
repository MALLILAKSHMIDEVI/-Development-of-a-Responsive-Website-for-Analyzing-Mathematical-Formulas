@echo off

rem Run tests
pytest test_app.py

rem Check if tests passed
if %errorlevel% equ 0 (
    echo Tests passed. Proceeding with additional steps.

    rem Additional steps (replace with your own actions)
    rem e.g., deploy, generate documentation, etc.

) else (
    echo Tests failed. Fix the issues before proceeding.
)
