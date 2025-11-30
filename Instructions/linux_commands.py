LINUX_COMMANDS = """
# Linux Commands

## File and Directory Commands
- `ls`: List directory contents
- `cd <directory>`: Change directory
- `pwd`: Print working directory
- `mkdir <directory>`: Create new directory
- `rmdir <directory>`: Remove empty directory
- `rm <file>`: Remove file
- `rm -r <directory>`: Remove directory and its contents
- `cp <source> <destination>`: Copy file or directory
- `mv <source> <destination>`: Move or rename file or directory
- `touch <file>`: Create a new empty file
- `cat <file>`: Display file contents
- `nano <file>`: Edit file using nano editor
- `chmod <permissions> <file>`: Change file permissions
- `chown <user>:<group> <file>`: Change file owner and group
- `ln -s <target> <link>`: Create symbolic link to a file

## System Information
- `uname -a`: Display all system information
- `top`: Display active processes
- `htop`: Interactive process viewer
- `df -h`: Display disk space usage
- `du -sh <directory>`: Show disk usage of a directory
- `free -h`: Display free and used memory
- `uptime`: Show system uptime
- `whoami`: Display current user

## File Permissions
- `chmod 755 <file>`: Assign read, write, execute permissions to owner and read, execute to others
- `chmod 644 <file>`: Assign read, write permissions to owner and read-only to others

## Networking
- `ifconfig`: Display network interfaces and IP addresses
- `ping <hostname or IP>`: Ping a remote host
- `curl <URL>`: Transfer data from or to a server
- `wget <URL>`: Download files from the web
- `ssh <user>@<hostname>`: Connect to remote host via SSH
- `scp <file> <user>@<hostname>:<directory>`: Secure copy files over SSH

## Process Management
- `ps aux`: Display all running processes
- `kill <PID>`: Kill process by ID
- `killall <process_name>`: Kill process by name
- `bg`: Resume suspended jobs in background
- `fg`: Bring background job to foreground
- "`kill -9 `ps aux | grep <keyword> | grep -v grep | awk '{print $2}'`" : Kill all process at once

## Disk Management
- `fdisk -l`: List disk partitions
- `mount <device> <directory>`: Mount a device
- `umount <device or directory>`: Unmount a device

## Package Management (Debian-based)
- `apt update`: Update package list
- `apt upgrade`: Upgrade installed packages
- `apt install <package>`: Install a package
- `apt remove <package>`: Remove a package
- `dpkg -i <package.deb>`: Install a Debian package file

## Searching and Filtering
- `grep <pattern> <file>`: Search for a pattern in a file
- `find <directory> -name <file>`: Find files and directories by name
- `locate <file>`: Locate file by name
- `tail -f <file>`: Continuously read a file
- `ls -1 | wc -l` : Count the Number of Files in Current Directory

## Users and Groups
- `adduser <username>`: Add a new user
- `deluser <username>`: Delete a user
- `usermod -aG <group> <user>`: Add user to a group
- `groupadd <groupname>`: Add a new group

## Compression
- `tar -czvf <archive.tar.gz> <directory>`: Compress directory into a tar.gz archive
- `tar -xzvf <archive.tar.gz>`: Extract tar.gz archive
- `zip <archive.zip> <file>`: Create a zip archive
- `unzip <archive.zip>`: Extract zip archive

## System Monitoring
- `dmesg`: Print kernel ring buffer messages
- `journalctl`: Query the systemd journal
- `iostat`: Report CPU and I/O statistics
"""
