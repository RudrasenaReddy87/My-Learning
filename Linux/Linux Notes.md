# Complete Linux Command Guide for DevOps

A single, practical, in-depth reference for every Linux command and topic you need for DevOps, SRE, sysadmin, and everyday development work. Every command below includes a **simple explanation**, **syntax**, **important options**, and **real examples**.

> 💡 Tip: You don't need to memorize everything. Bookmark this file, use `Ctrl+F`, and practice each command in a real terminal (a VM, WSL, or a Docker container is perfect for practice).

---

## 📚 Table of Contents

1. [Introduction to Linux](#1-introduction-to-linux)
2. [Linux Filesystem Hierarchy](#2-linux-filesystem-hierarchy)
3. [Shell & Terminal Basics](#3-shell--terminal-basics)
4. [Navigation Commands](#4-navigation-commands)
5. [File & Directory Operations](#5-file--directory-operations)
6. [Viewing & Editing Files](#6-viewing--editing-files)
7. [File Permissions & Ownership](#7-file-permissions--ownership)
8. [Text Processing & Filtering](#8-text-processing--filtering)
9. [Searching for Files & Content](#9-searching-for-files--content)
10. [Process Management](#10-process-management)
11. [Users & Group Management](#11-users--group-management)
12. [Package Management](#12-package-management)
13. [Disk & Storage Management](#13-disk--storage-management)
14. [Services & systemd](#14-services--systemd)
15. [Networking Commands](#15-networking-commands)
16. [Archiving & Compression](#16-archiving--compression)
17. [Environment Variables & Shell Configuration](#17-environment-variables--shell-configuration)
18. [Cron & Task Scheduling](#18-cron--task-scheduling)
19. [Logs & System Monitoring](#19-logs--system-monitoring)
20. [Shell Scripting Basics](#20-shell-scripting-basics)
21. [Useful DevOps Tips & Shortcuts](#21-useful-devops-tips--shortcuts)

---

## 1. Introduction to Linux

**Linux** is a free, open-source operating system kernel. Most "Linux" you use day to day is actually a **distribution** (distro) — the kernel plus tools, package manager, and system software bundled together.

### Common Distributions used in DevOps
| Distro | Package Manager | Common Use |
|---|---|---|
| Ubuntu / Debian | `apt` | Servers, cloud VMs, CI/CD runners |
| RHEL / CentOS / Rocky / Alma | `yum` / `dnf` | Enterprise servers |
| Amazon Linux | `yum` / `dnf` | AWS EC2 |
| Alpine | `apk` | Docker containers (lightweight) |

### Shell
The **shell** is the program that reads your commands and executes them. The most common shell is **bash** (Bourne Again Shell). Others: `sh`, `zsh`, `fish`.

Check your current shell:
```bash
echo $SHELL
```

### Terminal vs Shell vs Console
- **Terminal** — the window/app where you type.
- **Shell** — the program interpreting your commands.
- **Console** — a physical/virtual text-only screen (no GUI).

---

## 2. Linux Filesystem Hierarchy

Everything in Linux starts from a single root directory `/`. Understanding this is essential before running any command.

| Path | Meaning |
|---|---|
| `/` | Root — top of the entire filesystem |
| `/bin` | Essential user binaries (commands like `ls`, `cp`) |
| `/sbin` | System binaries (admin commands like `reboot`) |
| `/etc` | Configuration files (system-wide settings) |
| `/home` | Personal directories for each user (`/home/john`) |
| `/root` | Home directory of the `root` (admin) user |
| `/var` | Variable data — logs, caches, spool files (`/var/log`) |
| `/tmp` | Temporary files, cleared on reboot |
| `/usr` | User-installed programs and libraries |
| `/opt` | Optional/third-party software |
| `/dev` | Device files (hard disks, USB, terminals) |
| `/proc` | Virtual filesystem exposing kernel & process info |
| `/mnt` & `/media` | Mount points for external/temporary filesystems |
| `/boot` | Boot loader files, kernel images |
| `/lib` | Shared libraries needed by binaries in `/bin`, `/sbin` |

---

## 3. Shell & Terminal Basics

### `man` — manual pages
Shows the full manual/help for any command.
```bash
man ls
man -k network      # search man pages by keyword
```

### `--help`
Quick help for most commands:
```bash
ls --help
```

### `whoami`
Prints the current logged-in username.
```bash
whoami
```

### `clear`
Clears the terminal screen.
```bash
clear
```
Shortcut: `Ctrl + L`

### `history`
Shows previously run commands.
```bash
history          # show all history
history 10       # last 10 commands
!55               # re-run command number 55
!!                # re-run last command
```

### `exit`
Closes the current shell session.

### Command Structure
```
command  [options/flags]  [arguments]
ls       -la               /home/user
```
- Options usually start with `-` (short) or `--` (long), e.g. `-l` vs `--list`.
- Multiple short options can be combined: `ls -la` = `ls -l -a`.


---

## 4. Navigation Commands

### `pwd` — Print Working Directory
Shows the full path of the directory you're currently in.
```bash
pwd
```

### `cd` — Change Directory
Moves you between directories.
```bash
cd /var/log        # go to absolute path
cd ..               # go up one level
cd ~                # go to home directory
cd -                 # go to previous directory
cd                   # (no argument) also goes home
```

### `ls` — List directory contents
```bash
ls                  # list files/folders
ls -l               # long format (permissions, owner, size, date)
ls -a               # show hidden files (starting with .)
ls -la              # combine both
ls -lh              # human-readable sizes (K, M, G)
ls -R               # list recursively (subfolders too)
ls -t               # sort by modification time
ls -S               # sort by file size
ls -r               # reverse order
```

### `tree`
Shows directory structure as a tree (may need `apt install tree`).
```bash
tree
tree -L 2           # limit depth to 2 levels
```

---

## 5. File & Directory Operations

### `touch` — Create empty file / update timestamp
```bash
touch file.txt
touch file1.txt file2.txt      # multiple files
```

### `mkdir` — Make directory
```bash
mkdir myfolder
mkdir -p a/b/c        # create nested folders in one go (parents)
mkdir -v newdir        # verbose output
```

### `rmdir` — Remove empty directory
```bash
rmdir emptyfolder
```

### `rm` — Remove files/directories
```bash
rm file.txt
rm -r folder/          # remove directory recursively
rm -f file.txt          # force delete, no prompt/errors
rm -rf folder/          # force delete a folder and everything inside — ⚠️ DANGEROUS
rm -i file.txt          # ask for confirmation before deleting
```
> ⚠️ **Warning:** `rm -rf /` or `rm -rf *` can destroy your entire system. Always double-check the path before pressing Enter.

### `cp` — Copy files/directories
```bash
cp file.txt backup.txt
cp -r folder/ backup_folder/    # copy directory recursively
cp -v file.txt dest/             # verbose (shows what's copied)
cp -p file.txt dest/             # preserve permissions/timestamps
cp -u src.txt dest.txt           # copy only if source is newer
```

### `mv` — Move or rename files
```bash
mv oldname.txt newname.txt       # rename
mv file.txt /home/user/docs/     # move
mv -i file.txt dest/              # prompt before overwrite
```

### `ln` — Create links
```bash
ln source.txt hardlink.txt         # hard link (same inode, same data)
ln -s /path/target linkname        # symbolic (soft) link — like a shortcut
```
- **Hard link**: points directly to file's data; deleting original doesn't break it.
- **Soft link**: points to the file path; breaks if original is deleted/moved.

### `file`
Tells you the type of a file (text, binary, script, image, etc.).
```bash
file myscript.sh
```

### `stat`
Shows detailed metadata about a file (size, permissions, timestamps, inode).
```bash
stat file.txt
```

### `du` — Disk usage of files/folders
```bash
du -h file.txt          # human readable
du -sh folder/           # summary (total) size of a folder
du -sh *                 # size of everything in current dir
```

### `wc` — Word/line/byte count
```bash
wc file.txt              # lines, words, bytes
wc -l file.txt            # count lines only
wc -w file.txt            # count words only
```


---

## 6. Viewing & Editing Files

### `cat` — Concatenate & display file content
```bash
cat file.txt
cat file1.txt file2.txt > combined.txt   # merge files
cat -n file.txt                           # show line numbers
cat >> file.txt                           # append typed text (Ctrl+D to stop)
```

### `less` — View file page by page (recommended for big files)
```bash
less file.txt
```
Inside `less`: `q` quit, `/word` search, `n` next match, `g` go to top, `G` go to bottom.

### `more`
Older/simpler version of `less` (only scrolls forward).
```bash
more file.txt
```

### `head` — Show first lines of a file
```bash
head file.txt
head -n 20 file.txt      # first 20 lines
head -c 100 file.txt      # first 100 bytes
```

### `tail` — Show last lines of a file
```bash
tail file.txt
tail -n 50 file.txt        # last 50 lines
tail -f /var/log/syslog     # follow file in real time (great for live logs)
tail -f -n 100 app.log       # follow, starting from last 100 lines
```

### `echo` — Print text / write to files
```bash
echo "Hello World"
echo "text" > file.txt      # overwrite file with text
echo "text" >> file.txt     # append text to file
echo $HOME                   # print environment variable
```

### `nano` — Simple beginner-friendly text editor
```bash
nano file.txt
```
Shortcuts: `Ctrl+O` save, `Ctrl+X` exit, `Ctrl+K` cut line, `Ctrl+U` paste.

### `vim` / `vi` — Powerful modal text editor (very common on servers)
```bash
vim file.txt
```
Basics:
- `i` — enter Insert mode (start typing)
- `Esc` — go back to Normal mode
- `:w` — save
- `:q` — quit
- `:wq` or `ZZ` — save and quit
- `:q!` — quit without saving
- `dd` — delete a line
- `yy` — copy (yank) a line
- `p` — paste
- `/word` — search for "word"
- `u` — undo

### `diff` — Compare two files
```bash
diff file1.txt file2.txt
diff -u file1.txt file2.txt      # unified format (used in patches/git)
```

### `cmp`
Compares two files byte by byte, reports the first difference.
```bash
cmp file1.txt file2.txt
```

### `tee` — Write output to a file AND display it on screen
```bash
echo "hello" | tee file.txt
command | tee -a file.txt        # append instead of overwrite
ps aux | tee output.txt | grep nginx   # useful in pipelines
```


---

## 7. File Permissions & Ownership

Linux is a multi-user system, so every file/folder has an **owner**, a **group**, and **permissions** that decide who can read, write, or execute it.

### Understanding permission output
```bash
ls -l file.txt
-rwxr-xr-- 1 john devs 4096 Jul 10 10:00 file.txt
```
Breakdown: `- rwx r-x r--`
- First char: file type (`-`=file, `d`=directory, `l`=symlink)
- Next 3: **owner** permissions (`rwx`)
- Next 3: **group** permissions (`r-x`)
- Last 3: **others** permissions (`r--`)

`r` = read (4), `w` = write (2), `x` = execute (1)

### `chmod` — Change permissions
**Symbolic mode:**
```bash
chmod u+x script.sh        # add execute for owner (user)
chmod g-w file.txt          # remove write for group
chmod o=r file.txt           # set others to read-only
chmod a+x script.sh          # add execute for all (user, group, other)
```
**Numeric (octal) mode:** add up r(4)+w(2)+x(1) for each of owner/group/other
```bash
chmod 755 script.sh   # owner=rwx(7), group=r-x(5), other=r-x(5)
chmod 644 file.txt     # owner=rw-(6), group=r--(4), other=r--(4)
chmod -R 755 folder/   # apply recursively to all files/subfolders
```

### `chown` — Change file owner (and group)
```bash
chown john file.txt              # change owner to john
chown john:devs file.txt          # change owner AND group
chown -R john:devs folder/         # recursively for a whole folder
```

### `chgrp` — Change group only
```bash
chgrp devs file.txt
```

### `umask`
Sets the **default** permissions for newly created files/folders.
```bash
umask            # show current umask
umask 022         # common default (new files: 644, new dirs: 755)
```

### `getfacl` / `setfacl` — Advanced permissions (Access Control Lists)
Used when standard owner/group/other isn't flexible enough.
```bash
getfacl file.txt                       # view ACLs
setfacl -m u:jane:rw file.txt           # give user jane read+write
setfacl -m g:devs:rx file.txt            # give group devs read+execute
setfacl -x u:jane file.txt               # remove jane's ACL entry
```

### `sudo` — Run a command as another user (usually root/admin)
```bash
sudo apt update
sudo -i             # switch to an interactive root shell
sudo -u john ls      # run command as user 'john'
```

### `su` — Switch user
```bash
su john              # switch to user john (asks john's password)
su -                  # switch to root with root's environment
```


---

## 8. Text Processing & Filtering

These commands are the backbone of DevOps scripting — filtering logs, parsing output, transforming data.

### `grep` — Search text using patterns
```bash
grep "error" app.log                # find lines containing "error"
grep -i "error" app.log              # case-insensitive
grep -r "TODO" ./src                  # recursive search in a directory
grep -v "debug" app.log                # invert match (show lines NOT matching)
grep -c "error" app.log                 # count matching lines
grep -n "error" app.log                  # show line numbers
grep -E "error|fail" app.log              # extended regex (OR condition)
grep -w "cat" file.txt                     # match whole word only
grep -A 3 "Exception" app.log                # show 3 lines After match
grep -B 3 "Exception" app.log                # show 3 lines Before match
grep -l "error" *.log                          # only print filenames that match
```

### `sed` — Stream editor (find & replace, text transformation)
```bash
sed 's/foo/bar/' file.txt              # replace first "foo" with "bar" per line
sed 's/foo/bar/g' file.txt              # replace ALL occurrences per line
sed -i 's/foo/bar/g' file.txt            # edit file in-place (overwrite)
sed -n '5,10p' file.txt                   # print only lines 5-10
sed '3d' file.txt                          # delete line 3
sed -i '/pattern/d' file.txt                # delete all lines matching pattern
```

### `awk` — Pattern scanning and text processing (column-based)
```bash
awk '{print $1}' file.txt                  # print first column
awk '{print $1, $3}' file.txt               # print column 1 and 3
awk -F',' '{print $2}' data.csv              # use comma as delimiter
awk '{sum+=$2} END {print sum}' file.txt      # sum values in column 2
awk '/error/ {print $0}' app.log               # print full lines matching "error"
awk 'NR==5' file.txt                             # print only line number 5
```

### `cut` — Extract columns/fields from text
```bash
cut -d',' -f1 data.csv          # cut by comma delimiter, field 1
cut -d':' -f1 /etc/passwd        # get usernames from passwd file
cut -c1-5 file.txt                # cut characters 1 to 5
```

### `sort` — Sort lines of text
```bash
sort file.txt
sort -r file.txt          # reverse order
sort -n file.txt           # numeric sort
sort -k2 file.txt            # sort by 2nd column
sort -u file.txt              # sort and remove duplicates
sort -t',' -k2,2 data.csv       # sort CSV by 2nd field
```

### `uniq` — Remove/report duplicate lines (input must be sorted first)
```bash
sort file.txt | uniq            # remove duplicate lines
sort file.txt | uniq -c          # count occurrences of each line
sort file.txt | uniq -d           # show only duplicate lines
```

### `tr` — Translate or delete characters
```bash
echo "hello" | tr 'a-z' 'A-Z'         # convert to uppercase
tr -d ' ' < file.txt                    # delete all spaces
echo "hello world" | tr ' ' '_'          # replace spaces with underscores
```

### `xargs` — Build and run commands from piped input
```bash
find . -name "*.log" | xargs rm            # delete all found log files
echo "file1 file2" | xargs touch             # create multiple files
cat urls.txt | xargs -n1 curl -O               # download each URL one by one
find . -name "*.txt" | xargs -I{} cp {} backup/  # copy each match to backup/
```

### `wc`, `cat -n` — (see sections 5 & 6 above)

### `column`
Format text into aligned columns/table.
```bash
cat data.csv | column -s',' -t
```

### `paste`
Merge lines of files side by side.
```bash
paste file1.txt file2.txt
```

### Regular Expressions (regex) — quick reference
Used inside `grep`, `sed`, `awk`.
| Symbol | Meaning |
|---|---|
| `.` | any single character |
| `*` | zero or more of previous char |
| `+` | one or more (needs `-E` in grep) |
| `^` | start of line |
| `$` | end of line |
| `[abc]` | any one of a, b, c |
| `[^abc]` | any character except a, b, c |
| `\d` | digit (in some tools; use `[0-9]` in basic grep) |
| `\|` | OR (needs `-E`) |

---

## 9. Searching for Files & Content

### `find` — Search for files/directories by criteria
```bash
find /var/log -name "*.log"              # find by name
find . -type f                             # find files only
find . -type d                              # find directories only
find . -mtime -7                             # modified in last 7 days
find . -size +100M                            # files larger than 100MB
find . -name "*.tmp" -delete                    # find and delete
find . -name "*.sh" -exec chmod +x {} \;          # find and run a command on each result
find / -user john                                  # files owned by user john
find . -empty                                        # find empty files/folders
```

### `locate` — Fast file search using a pre-built index
```bash
locate file.txt
sudo updatedb        # refresh the search index (run occasionally)
```
> `locate` is much faster than `find` but relies on an index that may be outdated. `find` searches live.

### `which` — Show the path of an executable command
```bash
which python3
```

### `whereis` — Locate binary, source, and man page of a command
```bash
whereis ls
```

### `type`
Shows how a command would be interpreted (alias, builtin, or file).
```bash
type cd
type ls
```


---

## 10. Process Management

A **process** is any running program. Managing processes is a daily DevOps task — checking what's running, killing stuck processes, checking resource usage.

### `ps` — Snapshot of running processes
```bash
ps                  # processes in current shell
ps aux                # ALL processes, all users, detailed (most used)
ps -ef                 # similar, standard format (shows parent PID)
ps aux | grep nginx      # find a specific process
```
Key columns: `PID` (process ID), `%CPU`, `%MEM`, `STAT` (status), `CMD` (command).

### `top` — Real-time process/resource monitor
```bash
top
```
Inside `top`: `q` quit, `k` kill a process (enter PID), `M` sort by memory, `P` sort by CPU, `1` show per-core CPU.

### `htop` — Improved, colorful, interactive version of `top`
```bash
htop
```
(may require `apt install htop`) — supports mouse, scrolling, and easy kill (F9).

### `kill` — Terminate a process by PID
```bash
kill 1234              # send default signal (SIGTERM - graceful stop)
kill -9 1234             # SIGKILL - force kill immediately
kill -l                    # list all signal names
```

### `killall` — Kill process(es) by name
```bash
killall nginx
killall -9 firefox
```

### `pkill` — Kill processes matching a pattern
```bash
pkill -f "python app.py"
```

### `pgrep` — Find PID(s) by process name
```bash
pgrep nginx
pgrep -a nginx     # show PID + full command
```

### `nice` / `renice` — Set process priority
Priority ranges from **-20** (highest priority) to **19** (lowest).
```bash
nice -n 10 command          # start a command with lower priority
renice -n 5 -p 1234           # change priority of running PID 1234
```

### `jobs`, `bg`, `fg` — Manage background/foreground jobs in your shell
```bash
command &          # run in background
jobs                 # list background jobs
fg %1                 # bring job 1 to foreground
bg %1                  # resume job 1 in background
Ctrl+Z                  # suspend current foreground process
```

### `nohup` — Keep a process running after you log out
```bash
nohup ./myscript.sh &
nohup python app.py > output.log 2>&1 &
```

### `disown`
Detach a background job from the current shell so it survives shell exit.
```bash
command &
disown
```

### `uptime`
Shows how long the system has been running, plus load average.
```bash
uptime
```

### `free` — Show memory (RAM) usage
```bash
free -h        # human-readable (MB/GB)
```

### `vmstat` — Virtual memory / system performance stats
```bash
vmstat 2 5      # report every 2 seconds, 5 times
```

### `iostat` — CPU and disk I/O statistics
```bash
iostat -x 2      # extended stats every 2 seconds (needs sysstat package)
```

### `lsof` — List open files (and which process is using them)
```bash
lsof                     # all open files
lsof -i :8080              # find what's using port 8080
lsof -u john                 # files opened by user john
```


---

## 11. Users & Group Management

### Key files
- `/etc/passwd` — user account info (username, UID, home dir, shell)
- `/etc/shadow` — encrypted passwords
- `/etc/group` — group definitions

### `useradd` — Create a new user
```bash
sudo useradd john                     # create user (no home dir by default on some distros)
sudo useradd -m john                    # create user WITH home directory
sudo useradd -m -s /bin/bash john         # set home dir + default shell
```

### `passwd` — Set/change a password
```bash
sudo passwd john         # set password for john
passwd                     # change your own password
```

### `usermod` — Modify an existing user
```bash
sudo usermod -aG sudo john      # add john to the "sudo" group (-a = append, -G = group)
sudo usermod -s /bin/zsh john     # change default shell
sudo usermod -l newname oldname     # rename user
sudo usermod -L john                  # lock account (disable login)
sudo usermod -U john                   # unlock account
```

### `userdel` — Delete a user
```bash
sudo userdel john              # delete user (keeps home dir)
sudo userdel -r john             # delete user AND their home directory
```

### `groupadd` / `groupdel`
```bash
sudo groupadd developers
sudo groupdel developers
```

### `groups` — Show which groups a user belongs to
```bash
groups john
```

### `id` — Show UID, GID, and group memberships
```bash
id
id john
```

### `who` / `w` — Show who is logged in
```bash
who
w         # also shows what they're doing and CPU usage
```

### `last`
Shows login history.
```bash
last
```


---

## 12. Package Management

### Debian/Ubuntu — `apt`
```bash
sudo apt update                    # refresh package index (always run first)
sudo apt upgrade                     # upgrade all installed packages
sudo apt install nginx                 # install a package
sudo apt remove nginx                    # remove package (keep config files)
sudo apt purge nginx                       # remove package AND config files
sudo apt autoremove                          # remove unused dependencies
apt search nginx                                # search for a package
apt show nginx                                    # show package details
apt list --installed                                # list installed packages
```

### Low-level Debian tool — `dpkg`
```bash
sudo dpkg -i package.deb        # install a local .deb file
dpkg -l                            # list installed packages
dpkg -L nginx                        # list files installed by nginx package
```

### RHEL/CentOS/Fedora — `yum` / `dnf` (dnf is the modern replacement for yum)
```bash
sudo yum update                       # or: sudo dnf update
sudo yum install nginx                  # or: sudo dnf install nginx
sudo yum remove nginx                     # or: sudo dnf remove nginx
yum search nginx                            # search
yum info nginx                                # show details
yum list installed                              # list installed packages
```

### Low-level RPM tool — `rpm`
```bash
sudo rpm -ivh package.rpm      # install
rpm -qa                          # list all installed packages
rpm -qi nginx                      # show info about installed package
```

### Alpine (common in Docker images) — `apk`
```bash
apk update
apk add curl
apk del curl
```

### Universal/modern package formats
```bash
sudo snap install code          # Snap packages
flatpak install <app>              # Flatpak packages
```

---

## 13. Disk & Storage Management

### `df` — Disk Free (shows filesystem space usage)
```bash
df -h        # human readable (GB/MB) — most commonly used
df -i         # show inode usage instead of space
```

### `du` — Disk Usage (already covered in section 5, repeated here for context)
```bash
du -sh /var/log     # total size of a directory
du -sh /* 2>/dev/null | sort -rh | head -10   # top 10 biggest folders
```

### `mount` / `umount`
```bash
mount                             # show all mounted filesystems
sudo mount /dev/sdb1 /mnt/data      # mount a device to a folder
sudo umount /mnt/data                 # unmount
```

### `lsblk` — List block devices (disks/partitions) in a tree view
```bash
lsblk
lsblk -f     # also show filesystem type and UUID
```

### `fdisk` — Partition a disk (classic MBR/GPT tool)
```bash
sudo fdisk -l              # list all disks and partitions
sudo fdisk /dev/sdb          # interactive partitioning (careful!)
```

### `blkid`
Shows UUID and filesystem type of block devices.
```bash
sudo blkid
```

### `mkfs` — Create (format) a filesystem
```bash
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.xfs /dev/sdb1
```

### `fsck` — Check and repair a filesystem
```bash
sudo fsck /dev/sdb1
```

### `/etc/fstab`
Config file that defines which filesystems mount automatically at boot.

---

## 14. Services & systemd

**systemd** is the modern init system that manages services (daemons) on most Linux distros.

### `systemctl` — Control systemd services
```bash
sudo systemctl start nginx          # start a service
sudo systemctl stop nginx             # stop a service
sudo systemctl restart nginx            # restart
sudo systemctl reload nginx               # reload config without full restart
sudo systemctl status nginx                 # check current status
sudo systemctl enable nginx                   # start automatically on boot
sudo systemctl disable nginx                    # don't start on boot
systemctl list-units --type=service                # list all active services
systemctl is-active nginx                             # quick check: active/inactive
systemctl is-enabled nginx                              # quick check: enabled/disabled
sudo systemctl daemon-reload                              # reload systemd config files after editing unit files
```

### `service` — Older/simpler wrapper (still works on many systems)
```bash
sudo service nginx restart
```

### Unit files
Service definitions live in `/etc/systemd/system/` or `/lib/systemd/system/` (files ending in `.service`).


---

## 15. Networking Commands

### `ip` — Modern tool for network configuration (replaces `ifconfig`)
```bash
ip addr show          # show IP addresses (or: ip a)
ip link show             # show network interfaces
sudo ip addr add 192.168.1.10/24 dev eth0    # assign an IP
sudo ip link set eth0 up                        # bring interface up
ip route show                                     # show routing table
```

### `ifconfig` — Legacy tool (still common, may need `net-tools` package)
```bash
ifconfig
ifconfig eth0
```

### `ping` — Check connectivity to a host
```bash
ping google.com
ping -c 4 google.com     # send only 4 packets then stop
```

### `curl` — Transfer data / test APIs from the command line
```bash
curl https://example.com                    # GET request, print response
curl -o file.html https://example.com          # save response to a file
curl -O https://example.com/file.zip             # save with original filename
curl -I https://example.com                        # headers only (HEAD request)
curl -X POST -d '{"key":"value"}' -H "Content-Type: application/json" https://api.example.com
curl -X POST url -d 'name=john'                      # send form data
curl -u user:pass https://example.com                  # basic auth
curl -s https://example.com                              # silent (no progress bar)
curl -v https://example.com                                # verbose (debug mode)
curl -L https://example.com                                  # follow redirects
```

### `wget` — Download files from the web
```bash
wget https://example.com/file.zip
wget -O newname.zip https://example.com/file.zip     # save with custom name
wget -c https://example.com/file.zip                    # resume a partial download
wget -r https://example.com                                # recursive download (mirror site)
```

### `ssh` — Secure Shell (remote login)
```bash
ssh user@192.168.1.10
ssh -p 2222 user@host           # connect on custom port
ssh -i ~/.ssh/id_rsa user@host    # use a specific private key
ssh -L 8080:localhost:80 user@host  # local port forwarding (tunnel)
```

### `scp` — Secure copy files over SSH
```bash
scp file.txt user@host:/remote/path/        # upload
scp user@host:/remote/file.txt ./              # download
scp -r folder/ user@host:/remote/path/           # copy directory recursively
scp -P 2222 file.txt user@host:/path/              # custom port (capital P)
```

### `rsync` — Efficient file sync (only transfers changes)
```bash
rsync -avz source/ user@host:/dest/       # a=archive, v=verbose, z=compress
rsync -avz --delete source/ dest/            # mirror exactly, deleting extras in dest
rsync -avzP source/ dest/                      # show progress too
```

### `ssh-keygen` — Generate SSH key pairs
```bash
ssh-keygen -t rsa -b 4096 -C "you@example.com"
ssh-keygen -t ed25519            # modern, recommended key type
```

### `ssh-copy-id` — Copy your public key to a remote server (passwordless login)
```bash
ssh-copy-id user@host
```

### `netstat` — Network connections, routing, interface stats (legacy, still widely used)
```bash
netstat -tulnp     # t=tcp, u=udp, l=listening, n=numeric, p=show process
netstat -a           # all connections
```

### `ss` — Modern replacement for `netstat` (faster)
```bash
ss -tulnp          # show listening TCP/UDP ports and processes
ss -s                # summary statistics
```

### `dig` — DNS lookup tool (detailed)
```bash
dig example.com
dig example.com MX          # mail server records
dig +short example.com        # short output, just the IP
```

### `nslookup` — Simple DNS lookup
```bash
nslookup example.com
```

### `host`
Simple DNS lookup utility.
```bash
host example.com
```

### `traceroute` — Trace the network path (hops) to a destination
```bash
traceroute example.com
```

### `mtr`
Combines `ping` + `traceroute` in one live, continuously-updating tool.
```bash
mtr example.com
```

### `telnet` — Test if a specific port is open (basic connectivity test)
```bash
telnet example.com 80
```

### `nc` (netcat) — "Swiss army knife" for networking
```bash
nc -zv example.com 80        # check if a port is open
nc -l 1234                     # listen on port 1234
echo "hello" | nc example.com 1234    # send data to a port
```

### `hostname`
Shows or sets the machine's hostname.
```bash
hostname
hostname -I      # show IP addresses
```

### Firewall — `ufw` (Ubuntu simple firewall)
```bash
sudo ufw status
sudo ufw allow 22            # allow SSH
sudo ufw allow 80/tcp          # allow HTTP
sudo ufw deny 23                 # deny telnet
sudo ufw enable
sudo ufw disable
```

### Firewall — `iptables` (advanced, low-level, used under the hood by many tools)
```bash
sudo iptables -L                                  # list current rules
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # allow port 22
sudo iptables -A INPUT -p tcp --dport 80 -j DROP       # block port 80
```

### Firewall — `firewalld` (common on RHEL/CentOS)
```bash
sudo firewall-cmd --state
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```


---

## 16. Archiving & Compression

### `tar` — Bundle multiple files into a single archive (Tape ARchive)
```bash
tar -cvf archive.tar folder/          # Create an archive (c=create, v=verbose, f=filename)
tar -xvf archive.tar                    # eXtract an archive
tar -tvf archive.tar                      # List contents without extracting
tar -czvf archive.tar.gz folder/            # Create AND gzip-compress (z=gzip)
tar -xzvf archive.tar.gz                      # Extract a .tar.gz file
tar -cjvf archive.tar.bz2 folder/               # Create with bzip2 compression (j)
tar -xzvf archive.tar.gz -C /target/dir/          # extract into a specific directory
```
Memory trick: **c**reate, e**x**tract, **t**able-of-contents, **v**erbose, **f**ile, **z**gzip.

### `gzip` / `gunzip`
```bash
gzip file.txt            # compress (creates file.txt.gz, removes original)
gunzip file.txt.gz         # decompress
gzip -k file.txt             # keep the original file too
```

### `zip` / `unzip`
```bash
zip archive.zip file1.txt file2.txt
zip -r archive.zip folder/          # zip a whole folder recursively
unzip archive.zip
unzip -l archive.zip                  # list contents without extracting
unzip archive.zip -d /target/dir/       # extract to specific directory
```

### `bzip2` / `xz`
Alternative compression tools, generally better compression ratio, slower:
```bash
bzip2 file.txt
xz file.txt
```

---

## 17. Environment Variables & Shell Configuration

### What are environment variables?
Named values stored in memory that programs use for configuration (e.g., `PATH` tells the shell where to find commands).

### `env` — Show all environment variables
```bash
env
printenv                 # same thing
printenv PATH              # show a specific variable
```

### `echo $VAR` — Print a specific variable
```bash
echo $HOME
echo $PATH
echo $USER
```

### `export` — Create/set an environment variable for the session
```bash
export MY_VAR="hello"
export PATH=$PATH:/opt/myapp/bin      # add a directory to PATH
```
> Variables set with `export` only last for the current terminal session unless saved to a config file.

### `unset` — Remove a variable
```bash
unset MY_VAR
```

### Common important variables
| Variable | Meaning |
|---|---|
| `$HOME` | Current user's home directory |
| `$PATH` | Directories searched for executable commands |
| `$USER` | Current username |
| `$SHELL` | Path to current shell |
| `$PWD` | Current working directory |
| `$?` | Exit status of the last command (0 = success) |
| `$0` | Name of the current script/shell |
| `$$` | PID of the current shell |

### Shell startup / config files
| File | When it runs |
|---|---|
| `~/.bashrc` | Every new **interactive** non-login shell (most common place for aliases) |
| `~/.bash_profile` / `~/.profile` | Login shells |
| `/etc/environment` | System-wide environment variables |
| `/etc/profile` | System-wide, runs for all users at login |

To apply changes without restarting the terminal:
```bash
source ~/.bashrc
# or
. ~/.bashrc
```

### `alias` — Create shortcuts for commands
```bash
alias ll='ls -la'
alias gs='git status'
unalias ll                # remove an alias
```
Add these lines to `~/.bashrc` to make them permanent.

### `which`, `type` — check where a command is coming from
(covered in section 9)


---

## 18. Cron & Task Scheduling

### `crontab` — Schedule recurring jobs
```bash
crontab -e            # edit your personal crontab (opens in editor)
crontab -l              # list your current cron jobs
crontab -r                # remove all your cron jobs
sudo crontab -u john -e     # edit another user's crontab
```

### Cron syntax
```
*  *  *  *  *  command_to_run
│  │  │  │  │
│  │  │  │  └── day of week (0-7, 0 and 7 = Sunday)
│  │  │  └───── month (1-12)
│  │  └──────── day of month (1-31)
│  └─────────── hour (0-23)
└────────────── minute (0-59)
```

**Examples:**
```bash
# Run every day at 2:30 AM
30 2 * * * /home/user/backup.sh

# Run every 5 minutes
*/5 * * * * /home/user/check.sh

# Run every Monday at 9 AM
0 9 * * 1 /home/user/report.sh

# Run at the start of every hour
0 * * * * /home/user/hourly.sh

# Run on the 1st of every month
0 0 1 * * /home/user/monthly.sh
```

### System-wide cron
Instead of editing crontab, you can place scripts directly in:
```
/etc/cron.d/
/etc/cron.daily/
/etc/cron.hourly/
/etc/cron.weekly/
/etc/cron.monthly/
```

### `at` — Run a one-time scheduled job (not recurring)
```bash
at 10:00 PM
at> /home/user/script.sh
at> <Ctrl+D>            # finish input

atq       # list pending 'at' jobs
atrm 3     # remove job number 3
```

### systemd timers (modern alternative to cron)
```bash
systemctl list-timers            # list active timers
```
Timers are defined with a paired `.timer` and `.service` unit file — more powerful than cron (logging via journalctl, dependency management), but more setup.

---

## 19. Logs & System Monitoring

### `journalctl` — View systemd logs (the modern standard)
```bash
journalctl                        # view all logs
journalctl -u nginx                 # logs for a specific service (unit)
journalctl -f                         # follow logs in real time (like tail -f)
journalctl --since "1 hour ago"         # logs from last hour
journalctl --since today                  # logs from today
journalctl -p err                           # only errors and above
journalctl -k                                 # kernel messages only
journalctl -n 100                               # last 100 lines
journalctl --disk-usage                           # how much space logs are using
sudo journalctl --vacuum-time=7d                    # delete logs older than 7 days
```

### Traditional log files (`/var/log/`)
| File | Contains |
|---|---|
| `/var/log/syslog` or `/var/log/messages` | General system logs |
| `/var/log/auth.log` or `/var/log/secure` | Authentication/login attempts |
| `/var/log/kern.log` | Kernel messages |
| `/var/log/dmesg` | Boot-time kernel ring buffer |
| `/var/log/apache2/` or `/var/log/nginx/` | Web server logs |

### `dmesg` — Kernel ring buffer messages (hardware, boot, driver issues)
```bash
dmesg
dmesg | tail -20
dmesg -w         # follow live (watch mode)
```

### Monitoring commands recap
```bash
top / htop         # live process & resource monitor
free -h              # RAM usage
df -h                 # disk space
du -sh *                # folder sizes
vmstat 2 5                # system performance snapshots
iostat -x 2                 # disk I/O stats
uptime                        # load average
lsof -i :PORT                  # what's using a port
netstat -tulnp / ss -tulnp       # listening ports
```

### `watch` — Repeatedly run a command and show live updates
```bash
watch -n 2 df -h            # run `df -h` every 2 seconds
watch -n 1 'ps aux | grep nginx'
```


---

## 20. Shell Scripting Basics

A shell script is just a text file containing a sequence of commands, run automatically.

### The Shebang line
Every script should start with this line, which tells the OS which interpreter to use:
```bash
#!/bin/bash
```

### Making a script executable
```bash
chmod +x script.sh
./script.sh          # run it (must have ./ or full path unless in $PATH)
bash script.sh          # or run it directly with bash, no chmod needed
```

### Variables
```bash
name="John"
echo "Hello, $name"
echo "Hello, ${name}"     # curly braces recommended for clarity
```
> No spaces around `=` when assigning a variable in bash.

### Reading user input
```bash
read -p "Enter your name: " name
echo "Hi $name"
```

### Command-line arguments
```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
```

### Conditionals — `if / elif / else`
```bash
#!/bin/bash
num=10

if [ $num -gt 5 ]; then
    echo "Greater than 5"
elif [ $num -eq 5 ]; then
    echo "Equal to 5"
else
    echo "Less than 5"
fi
```

**Common comparison operators:**
| Numbers | Meaning | Strings | Meaning |
|---|---|---|---|
| `-eq` | equal | `=` | equal |
| `-ne` | not equal | `!=` | not equal |
| `-gt` | greater than | `-z` | string is empty |
| `-lt` | less than | `-n` | string is not empty |
| `-ge` | greater or equal | | |
| `-le` | less or equal | | |

**File test operators:**
```bash
[ -f file.txt ]     # true if file exists
[ -d folder ]         # true if directory exists
[ -x script.sh ]        # true if file is executable
[ -e path ]               # true if path exists (file or dir)
```

### Loops
**For loop:**
```bash
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

for file in *.txt; do
    echo "Found: $file"
done

for i in {1..10}; do
    echo $i
done
```

**While loop:**
```bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done
```

**Until loop:**
```bash
count=1
until [ $count -gt 5 ]; do
    echo $count
    count=$((count + 1))
done
```

### Functions
```bash
greet() {
    echo "Hello, $1!"
}

greet "World"     # calling the function with an argument
```

### Exit codes
```bash
exit 0      # success
exit 1      # generic error
echo $?      # check the exit code of the LAST command run
```

### Arithmetic
```bash
result=$((5 + 3))
echo $result

# or using expr (older style)
result=$(expr 5 + 3)
```

### Case statement
```bash
read -p "Enter a fruit: " fruit
case $fruit in
    apple) echo "It's an apple" ;;
    banana) echo "It's a banana" ;;
    *) echo "Unknown fruit" ;;
esac
```

### Practical DevOps script example
```bash
#!/bin/bash
# Simple backup script

SOURCE="/var/www/html"
DEST="/backup/website_$(date +%Y%m%d_%H%M%S).tar.gz"

if [ -d "$SOURCE" ]; then
    tar -czf "$DEST" "$SOURCE"
    echo "Backup completed: $DEST"
else
    echo "Source directory not found!"
    exit 1
fi
```


---

## 21. Useful DevOps Tips & Shortcuts

### Keyboard shortcuts (bash)
| Shortcut | Action |
|---|---|
| `Ctrl + C` | Kill the current running command |
| `Ctrl + Z` | Suspend current command (move to background, paused) |
| `Ctrl + D` | Exit shell / end input (EOF) |
| `Ctrl + L` | Clear screen |
| `Ctrl + R` | Search command history |
| `Ctrl + A` | Move cursor to start of line |
| `Ctrl + E` | Move cursor to end of line |
| `Ctrl + U` | Clear the line before the cursor |
| `Ctrl + K` | Clear the line after the cursor |
| `Tab` | Auto-complete command/filename |
| `Tab Tab` | Show all possible completions |

### Piping and redirection
```bash
command1 | command2        # pipe: output of command1 becomes input of command2
command > file.txt            # redirect stdout, OVERWRITE file
command >> file.txt             # redirect stdout, APPEND to file
command 2> error.log              # redirect stderr only
command > out.log 2>&1              # redirect both stdout AND stderr to same file
command < input.txt                   # use file as input
command1 && command2                    # run command2 ONLY IF command1 succeeds
command1 || command2                      # run command2 ONLY IF command1 fails
command1 ; command2                         # run both, regardless of success/failure
command &                                     # run in background
```

### Chaining examples used daily in DevOps
```bash
# Find and kill a process using a port
lsof -i :8080 | grep LISTEN
kill -9 $(lsof -t -i:8080)

# Check disk space and alert if root is over 90%
df -h / | awk 'NR==2 {print $5}'

# Find largest 10 files in a directory
find . -type f -exec du -h {} + | sort -rh | head -10

# Tail multiple logs at once
tail -f /var/log/nginx/access.log /var/log/nginx/error.log

# Count how many times an IP appears in access logs
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head

# One-liner health check loop
while true; do curl -s -o /dev/null -w "%{http_code}\n" https://example.com; sleep 5; done
```

### Checking system info
```bash
uname -a          # kernel + system info
hostnamectl         # hostname, OS, kernel details (systemd systems)
cat /etc/os-release   # OS name and version
lscpu                  # CPU details
lsusb                    # list USB devices
lspci                     # list PCI devices
```

### SSH config shortcut (`~/.ssh/config`)
Instead of typing long ssh commands, define hosts:
```
Host myserver
    HostName 192.168.1.10
    User john
    Port 2222
    IdentityFile ~/.ssh/id_rsa
```
Then simply run:
```bash
ssh myserver
```

### Quick reference: exit status
```bash
echo $?     # 0 = success, non-zero = some kind of error
```

### Combining `find` + `xargs` + `grep` (classic DevOps trio)
```bash
find . -name "*.log" | xargs grep -l "ERROR"
```

---

## 📌 Final Notes

- Practice is everything — spin up a free VM (or use Docker/WSL) and try each command.
- Always double-check destructive commands (`rm -rf`, `dd`, `mkfs`) before running them.
- `man <command>` and `<command> --help` are your best friends when you forget an option.
- This guide covers the 80-90% of Linux commands used daily in real DevOps, SRE, and sysadmin work. For niche/advanced topics (SELinux, LVM, kernel tuning, advanced networking with `tc`/`nftables`), dive deeper once you're comfortable with everything above.

**Happy learning! 🐧**

---

## 22. Special Permissions (SUID, SGID, Sticky Bit)

Beyond basic read/write/execute, Linux has three special permission bits that control advanced behavior.

### SUID (Set User ID) — `4000`
When set on an **executable**, the program runs with the **file owner's** privileges, not the user running it. Classic example: `/usr/bin/passwd` runs as root so any user can change their own password.
```bash
chmod u+s file          # add SUID (symbolic)
chmod 4755 file           # add SUID (numeric, leading 4)
ls -l file                  # SUID shows as 's' in owner execute spot: -rwsr-xr-x
```

### SGID (Set Group ID) — `2000`
On an **executable**: runs with the file's group privileges.
On a **directory**: all new files/folders created inside inherit the directory's group (very useful for shared team folders).
```bash
chmod g+s folder/       # add SGID (symbolic)
chmod 2775 folder/        # add SGID (numeric, leading 2)
```

### Sticky Bit — `1000`
On a **directory**: only the file's owner (or root) can delete/rename files inside it, even if others have write access. Classic example: `/tmp` has the sticky bit set.
```bash
chmod +t folder/         # add sticky bit
chmod 1777 folder/         # add sticky bit (numeric, leading 1)
ls -ld /tmp                  # sticky bit shows as 't' in others execute spot: drwxrwxrwt
```

### Combined numeric permissions
```bash
chmod 4755 file      # SUID + rwxr-xr-x
chmod 2755 folder/     # SGID + rwxr-xr-x
chmod 1777 folder/       # Sticky + rwxrwxrwx
```

> ⚠️ SUID/SGID on scripts (not compiled binaries) is often ignored by the kernel for security reasons, and having SUID root binaries lying around is a common security risk — audit them with `find / -perm -4000 -type f 2>/dev/null`.

---

## 23. Disk Cloning, Checksums & Data Integrity

### `dd` — Low-level copy of raw data (disk cloning, ISO writing, wiping disks)
```bash
sudo dd if=/dev/sda of=/dev/sdb bs=4M status=progress    # clone entire disk sda to sdb
sudo dd if=image.iso of=/dev/sdb bs=4M status=progress      # write an ISO to a USB drive
sudo dd if=/dev/zero of=/dev/sdb bs=1M count=100               # wipe first 100MB of a disk
dd if=/dev/sda of=backup.img bs=4M                                # backup a disk to an image file
```
- `if=` input file, `of=` output file, `bs=` block size (bigger = faster, up to a point), `status=progress` shows live progress.
> ⚠️ `dd` is called "disk destroyer" for a reason — mixing up `if` and `of`, or the wrong device name, can silently wipe the wrong disk. Always double/triple-check `if=` and `of=`.

### Checksums — verify file integrity (e.g., after downloading an ISO)
```bash
md5sum file.iso                     # generate MD5 checksum
sha1sum file.iso                      # generate SHA1 checksum
sha256sum file.iso                      # generate SHA256 checksum (most common today)
sha256sum -c checksums.txt                # verify against a checksums file
echo "abc123... file.iso" | sha256sum -c    # verify a single expected checksum
```

---

## 24. Swap Space Management

**Swap** is disk space used as overflow "virtual RAM" when physical memory is full.

```bash
free -h                            # check current swap usage
swapon --show                        # list active swap devices
sudo swapon /swapfile                  # enable a swap file/partition
sudo swapoff /swapfile                   # disable swap

# Create a new swap file (e.g., 2GB)
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```
To make it permanent, add a line to `/etc/fstab`:
```
/swapfile none swap sw 0 0
```

### Swappiness
Controls how aggressively the kernel uses swap (0-100, lower = prefer RAM more).
```bash
cat /proc/sys/vm/swappiness
sudo sysctl vm.swappiness=10       # temporary change
```

---

## 25. LVM (Logical Volume Manager)

LVM lets you resize storage dynamically by adding a flexible layer between physical disks and filesystems: **Physical Volume (PV) → Volume Group (VG) → Logical Volume (LV)**.

```bash
# Create a physical volume from a disk/partition
sudo pvcreate /dev/sdb1
pvdisplay                          # show physical volume info

# Create a volume group from one or more physical volumes
sudo vgcreate myvg /dev/sdb1
vgdisplay                            # show volume group info

# Create a logical volume from the volume group
sudo lvcreate -L 10G -n mylv myvg
lvdisplay                             # show logical volume info

# Format and mount it like any normal partition
sudo mkfs.ext4 /dev/myvg/mylv
sudo mount /dev/myvg/mylv /mnt/data

# Extend a logical volume (grow storage without downtime)
sudo lvextend -L +5G /dev/myvg/mylv
sudo resize2fs /dev/myvg/mylv          # resize the ext4 filesystem to match (use xfs_growfs for XFS)
```

---

## 26. RAID Basics

RAID combines multiple disks for redundancy and/or performance. Software RAID on Linux uses `mdadm`.

```bash
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1   # create RAID 1 (mirroring)
cat /proc/mdstat                     # check RAID status
sudo mdadm --detail /dev/md0            # detailed info about the RAID array
```
Common RAID levels: **RAID 0** (striping, speed, no redundancy), **RAID 1** (mirroring, redundancy), **RAID 5** (striping + parity, needs 3+ disks), **RAID 10** (mirror + stripe).

---

## 27. Filesystem Types (Quick Comparison)

| Filesystem | Notes |
|---|---|
| `ext4` | Most common default on Linux, stable, journaling |
| `xfs` | Default on RHEL/CentOS, great for large files, easy to grow (not shrink) |
| `btrfs` | Modern, supports snapshots, built-in RAID-like features |
| `ntfs` | Windows filesystem, read/write support via `ntfs-3g` |
| `fat32`/`exfat` | Used for USB drives, cross-platform compatibility |
| `tmpfs` | Lives in RAM, very fast, cleared on reboot (used for `/tmp` on some systems) |


---

## 28. Boot Process & GRUB

Understanding what happens when a Linux machine starts is useful for troubleshooting servers that won't boot.

### Boot sequence (simplified)
1. **BIOS/UEFI** — hardware powers on, runs firmware self-check (POST).
2. **Bootloader (GRUB)** — loads the Linux kernel into memory.
3. **Kernel initialization** — kernel starts, mounts root filesystem, starts `init`.
4. **init/systemd** — the first process (`PID 1`), starts all other services in order.
5. **Targets/runlevels reached** — system is fully up (multi-user, graphical, etc.).

### GRUB (GRand Unified Bootloader)
Config file: `/etc/default/grub` (edit this, not the generated one).
```bash
sudo update-grub                 # regenerate GRUB config (Debian/Ubuntu)
sudo grub2-mkconfig -o /boot/grub2/grub.cfg    # regenerate on RHEL/CentOS
```

### systemd targets (replacement for old "runlevels")
| Target | Old Runlevel | Meaning |
|---|---|---|
| `poweroff.target` | 0 | Shutdown |
| `rescue.target` | 1 | Single-user/rescue mode |
| `multi-user.target` | 3 | Multi-user, no GUI (typical for servers) |
| `graphical.target` | 5 | Multi-user with GUI |
| `reboot.target` | 6 | Reboot |

```bash
systemctl get-default                    # show current default target
sudo systemctl set-default multi-user.target   # set default boot target
sudo systemctl isolate rescue.target         # switch to a target right now
sudo systemctl rescue                          # boot into rescue mode
sudo systemctl emergency                        # emergency mode (minimal, for repairs)
```

### Reboot / Shutdown commands
```bash
sudo reboot
sudo shutdown -h now          # halt immediately
sudo shutdown -r now            # reboot immediately
sudo shutdown -h +10              # shutdown in 10 minutes
sudo shutdown -c                    # cancel a scheduled shutdown
sudo poweroff
sudo halt
```

---

## 29. Kernel Modules

Kernel modules are pieces of code that can be loaded/unloaded into the kernel at runtime (drivers, filesystems, etc.) without rebooting.

```bash
lsmod                              # list currently loaded modules
modinfo <module_name>                # show details about a module
sudo modprobe <module_name>            # load a module (handles dependencies automatically)
sudo modprobe -r <module_name>           # remove/unload a module
sudo insmod /path/module.ko                # insert a module directly (no dependency resolution)
sudo rmmod <module_name>                     # remove a module directly
```
Modules that should load automatically at boot are listed in `/etc/modules` (Debian/Ubuntu) or files in `/etc/modules-load.d/`.

---

## 30. Kernel Parameters (sysctl) & the /proc Filesystem

### `/proc` — a virtual filesystem exposing live kernel and process information
```bash
cat /proc/cpuinfo          # CPU details
cat /proc/meminfo            # memory details
cat /proc/version              # kernel version
cat /proc/uptime                 # system uptime in seconds
ls /proc/1234                      # info about process with PID 1234
cat /proc/1234/status                # detailed status of that process
```

### `sysctl` — view and change kernel parameters at runtime
```bash
sysctl -a                              # list ALL kernel parameters (huge output)
sysctl vm.swappiness                     # check a specific parameter
sudo sysctl -w net.ipv4.ip_forward=1       # change a parameter temporarily (until reboot)
```
To make changes **permanent**, add them to `/etc/sysctl.conf` or a file in `/etc/sysctl.d/`, then run:
```bash
sudo sysctl -p       # reload sysctl settings from config files
```
**Common DevOps-relevant parameters:**
| Parameter | Purpose |
|---|---|
| `net.ipv4.ip_forward` | Enable packet forwarding (routing, needed for Docker/VPN) |
| `vm.swappiness` | How aggressively the kernel swaps |
| `fs.file-max` | Max number of open file handles system-wide |
| `net.core.somaxconn` | Max queued connections for a socket (important for high-traffic servers) |

---

## 31. Resource Limits (ulimit)

Controls how many resources (open files, processes, memory) a user/process can consume — important for tuning servers running many connections (databases, web servers).

```bash
ulimit -a                  # show all current limits
ulimit -n                    # show max open file descriptors
ulimit -n 4096                 # set max open files for current session (soft limit)
ulimit -u                        # show max number of user processes
ulimit -Hn                         # show HARD limit for open files
```
Permanent limits are set in `/etc/security/limits.conf`:
```
john    soft    nofile    4096
john    hard    nofile    8192
```


---

## 32. Date, Time & NTP

### `date` — show or set the system date/time
```bash
date                                 # show current date/time
date +"%Y-%m-%d"                       # custom format: 2026-07-11
date +"%Y-%m-%d %H:%M:%S"                # with time
date -d "2 days ago"                       # relative date calculation
date -d "next monday"                        # next Monday's date
sudo date -s "2026-07-11 10:00:00"             # manually set system date/time
```
**Common format codes:** `%Y` year, `%m` month, `%d` day, `%H` hour(24h), `%M` minute, `%S` second.

### `cal` — display a calendar
```bash
cal
cal 2026            # show whole year
```

### `timedatectl` — manage system time, timezone, and NTP sync (systemd)
```bash
timedatectl                           # show current date, time, timezone, sync status
timedatectl list-timezones              # list all available timezones
sudo timedatectl set-timezone Asia/Kolkata   # change timezone
sudo timedatectl set-ntp true                  # enable automatic time sync (NTP)
```

### `hwclock` — hardware (BIOS) clock
```bash
sudo hwclock --show          # show hardware clock time
sudo hwclock --systohc          # sync hardware clock FROM system clock
```

### NTP services
Modern systems use `chrony` or `systemd-timesyncd` to keep clocks in sync with internet time servers — critical for logs, certificates, and distributed systems (clock drift breaks TLS and clustering).
```bash
sudo systemctl status chronyd     # check chrony service status
chronyc tracking                    # show sync status/drift
chronyc sources                       # show configured NTP sources
```

---

## 33. DNS & Name Resolution Files

### `/etc/hosts` — manual hostname-to-IP mappings (checked before DNS)
```
127.0.0.1    localhost
192.168.1.50 myserver.local myserver
```
Editing this file lets you override DNS locally — very common for testing.

### `/etc/resolv.conf` — configures which DNS servers the system uses
```
nameserver 8.8.8.8
nameserver 1.1.1.1
```
> On many modern systems this file is auto-generated (by NetworkManager or systemd-resolved) — manual edits may get overwritten.

### `/etc/nsswitch.conf` — controls the ORDER of name resolution sources
```
hosts: files dns
```
This means: check `/etc/hosts` first, then fall back to DNS.

### `resolvectl` / `systemd-resolve` — modern DNS query/status tool
```bash
resolvectl status                 # show DNS configuration per interface
resolvectl query example.com         # resolve a hostname
```

---

## 34. Advanced Bash Scripting

### Arrays
```bash
fruits=("apple" "banana" "cherry")
echo ${fruits[0]}          # apple (first element)
echo ${fruits[@]}            # all elements
echo ${#fruits[@]}              # array length (3)
fruits+=("mango")                  # append an element
for f in "${fruits[@]}"; do echo $f; done   # loop over array
```

### String manipulation
```bash
str="Hello World"
echo ${#str}              # length of string: 11
echo ${str:0:5}             # substring from position 0, length 5 → "Hello"
echo ${str/World/Bash}        # replace first match → "Hello Bash"
echo ${str^^}                    # convert to UPPERCASE
echo ${str,,}                      # convert to lowercase
name=""
echo ${name:-"default"}              # use "default" if name is empty/unset
```

### Command substitution
Capture the output of a command into a variable.
```bash
current_date=$(date +%Y-%m-%d)
echo "Today is $current_date"

files=$(ls *.txt)     # older backtick style also works: files=`ls *.txt`
```

### Here Documents (heredoc) — feed multi-line text into a command
```bash
cat << EOF > config.txt
server=myserver
port=8080
env=production
EOF
```

### Process substitution
```bash
diff <(ls dir1) <(ls dir2)      # compare output of two commands as if they were files
```

### `trap` — catch signals inside a script (cleanup on exit/interrupt)
```bash
#!/bin/bash
trap 'echo "Script interrupted!"; exit 1' SIGINT SIGTERM

trap 'rm -f /tmp/tempfile' EXIT     # always clean up on exit, even on error
```

### Debugging scripts
```bash
bash -x script.sh          # run with debug trace (shows every command executed)
set -x                        # turn ON debug mode inside a script
set +x                          # turn OFF debug mode
set -e                            # exit script immediately if any command fails
set -u                              # error out if using an undefined variable
set -o pipefail                       # catch failures inside a pipeline (not just the last command)
```
> Combining `set -euo pipefail` at the top of scripts is a common DevOps best practice for safer automation.

### Special bash parameters (extra ones not covered earlier)
| Variable | Meaning |
|---|---|
| `$!` | PID of the last background process |
| `$_` | Last argument of the previous command |
| `$-` | Current shell option flags |
| `$*` | All positional arguments as a single string |

### Functions with return values
```bash
add() {
    local result=$(( $1 + $2 ))
    echo $result
}
sum=$(add 5 3)
echo "Sum: $sum"
```


---

## 35. Security Basics: SELinux, AppArmor, chroot

### SELinux (Security-Enhanced Linux) — used on RHEL/CentOS/Fedora
Adds an extra, mandatory access control layer on top of normal permissions.
```bash
sestatus                          # check if SELinux is enabled and its mode
getenforce                          # show current mode (Enforcing/Permissive/Disabled)
sudo setenforce 0                     # set to Permissive (log only, don't block) - temporary
sudo setenforce 1                       # set to Enforcing
ls -Z file.txt                            # view SELinux context/labels on a file
sudo chcon -t httpd_sys_content_t file.html   # change SELinux context/type
```
Config file: `/etc/selinux/config`.

### AppArmor — used on Ubuntu/Debian (alternative to SELinux)
```bash
sudo aa-status                    # show AppArmor status and loaded profiles
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx   # enforce a profile
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx    # set profile to complain-only (log, don't block)
```

### `chroot` — change the apparent root directory for a process
Used to isolate a process/environment (an early ancestor of container technology).
```bash
sudo chroot /mnt/newroot /bin/bash
```

---

## 36. Process States & Signals (Deeper Dive)

### Process states (seen in `ps` / `top` STAT column)
| Code | Meaning |
|---|---|
| `R` | Running or runnable (on run queue) |
| `S` | Sleeping (waiting for an event, interruptible) |
| `D` | Uninterruptible sleep (usually waiting on disk I/O) |
| `T` | Stopped (suspended, e.g. via `Ctrl+Z`) |
| `Z` | Zombie — process finished but parent hasn't collected its exit status yet |
| `<` | High priority process |
| `N` | Low priority (niced) process |

### Common signals
| Signal | Number | Meaning |
|---|---|---|
| `SIGHUP` | 1 | Hangup — often used to tell a daemon to reload its config |
| `SIGINT` | 2 | Interrupt — same as pressing `Ctrl+C` |
| `SIGKILL` | 9 | Force kill — cannot be caught or ignored by the process |
| `SIGTERM` | 15 | Graceful termination request (default signal of `kill`) |
| `SIGSTOP` | 19 | Pause a process (cannot be caught/ignored) |
| `SIGCONT` | 18 | Resume a paused process |

```bash
kill -HUP 1234           # ask process to reload config
kill -SIGTERM 1234         # ask nicely to stop (default)
kill -SIGKILL 1234           # force stop, no cleanup
```
> Always try `SIGTERM` before `SIGKILL` — it gives the process a chance to close files, save state, and shut down cleanly. `SIGKILL` gives it none.

### Zombie processes
A "zombie" is a finished process still listed in the process table because its parent hasn't read its exit status. They use no resources but a large number of them may indicate a buggy parent application. They **cannot be killed directly** — you must fix or restart the parent process.
```bash
ps aux | grep 'Z'      # find zombie processes
```

### Orphan processes
A process whose parent has terminated. It gets automatically "adopted" by `init`/`systemd` (PID 1).

---

## ✅ Summary of Everything Covered

This guide now includes **36 topics**: Linux basics, filesystem hierarchy, shell fundamentals, navigation, file/directory operations, viewing/editing files, permissions (basic + special bits), text processing, searching, process management, users/groups, package management, disk/storage (+ LVM, RAID, swap), services/systemd, networking (+ DNS files), archiving/compression, environment variables, cron scheduling, logging/monitoring, shell scripting (basic + advanced), boot process/GRUB, kernel modules, kernel tuning (sysctl/proc), resource limits, date/time/NTP, security basics (SELinux/AppArmor/chroot), and process states/signals — everything needed for real-world DevOps, SRE, and sysadmin work on Linux.

**Happy learning! 🐧**
