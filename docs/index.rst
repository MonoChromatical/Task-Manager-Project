.. conf.py documentation master file, created by
   sphinx-quickstart on Tue Apr  7 15:16:19 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Task Manager Documentation
==========================

Task Manager is a simple Python application for managing tasks. This documentation includes detailed information about functions, classes, and usage examples.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Modules

   task_manager_project

Examples
--------

Below is a simple example using Task Manager functions:

.. code-block:: python

    from task_manager import add_task, remove_task

    tasks = []
    add_task(tasks, "Finish Sprint Assignment")
    remove_task(tasks, "Finish Sprint Assignment")
    print(tasks)