> **This course focuses on the management of files and processes on the operating system running on your device.**

# Operating System

An **Operating System (OS)** is the software that manages everything that happens on a computer. It acts as an interface between the user, applications, and the computer's hardware.

Some of the responsibilities of an operating system include:

- Reading, writing, modifying, and deleting files from the hard drive or other storage devices.
- Managing how applications, programs, and processes start, interact with one another, and eventually terminate.
- Allocating and managing memory between different running processes.
- Handling how network packets are sent and received.
- Managing hardware resources such as the CPU, memory, storage devices, and input/output peripherals.


## Components of an Operating System

An operating system consists of two main parts:

### 1. Kernel

The **kernel** is the core part of the operating system. It:

- Communicates directly with the computer's hardware.
- Manages the system's resources, including the CPU, memory, storage devices, and network interfaces.
- Schedules and manages running processes.
- Handles device drivers.
- Ensures that multiple applications can safely share hardware resources.

> The kernel runs with the highest level of system privileges and is responsible for the overall stability of the operating system.

### 2. User Space

**User space** refers to everything outside the kernel. It contains all the software that users interact with directly.
Examples include:

- Applications
- Programs
- Graphical User Interfaces (GUI)
- Command-line tools
- Utilities

Programs running in user space cannot directly access hardware. Instead, they communicate with the kernel through **system calls** whenever they need hardware resources or operating system services.

Some OS include Windows (Microsoft), MacOS (Apple but some of its kernel and user-space tools come from Unix's BSD), Linux (open-source but originally developed by Linus Torvalds) and Unix (Bell Labs).

## Linux

Linux is one of the most important operating systems in modern computing.

Some of its key characteristics include:
- Widely used in business infrastructure and enterprise servers.
- Powers the majority of web servers and many supercomputers.
- Based on Unix design principles.
- Completely open-source.
- Available in many different versions called **distributions (distros)**, each packaged and maintained by different organizations.
- Highly customizable, stable, and secure.

Some popular Linux distributions include:
- Ubuntu
- Debian
- Red Hat
- Fedora
- Arch Linux
- ChromeOS

> **Android** also runs on a modified Linux kernel.

### Why Python?
Python is a **cross-platform language**. Since it is cross-platform, we can use the same Python code to get to our goal on any operating system whether the goal is opening files, processing text or managing running processes.

<br>

# Setup (Windows)
### 1. Check if Python is Installed

Open **Command Prompt (cmd)** and run:

```bash
python --version
```

If Python is installed, it should display the installed version.

### 2. Install the Requests Library

If Python is not installed, download and install it first. During installation, make sure to enable **Add Python to PATH**.

Then install the Requests library by running:

```bash
python -m pip install requests
```

### 3. Test Requests

After the installation is complete, start the Python interpreter by running:

```bash
python
```

To verify that the **Requests** library has been installed successfully, enter the following commands (output should be as said):

```python
>>> import requests
>>> response = requests.get("https://httpbin.org/get")
>>> response.status_code
200
```
To exit simply type the following and you'll be back to the terminal as it was:

```python
exit()
```