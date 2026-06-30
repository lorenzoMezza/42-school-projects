*This project has been created as part of the 42 curriculum by lmezzaba.*

# Born2beRoot

## Description

Born2beRoot is a system administration project from the 42 curriculum. Its goal is to set up a secure minimal Linux server inside a virtual machine.

For this project, I installed Debian GNU/Linux 13 in VirtualBox without a graphical desktop environment. The server is configured with encrypted storage, LVM logical volumes, SSH access, a firewall, AppArmor, a strong password policy, sudo auditing, and an automatic monitoring script.

The virtual machine hostname is:

```text
lmezzaba42
```

The main non-root user is:

```text
lmezzaba
```

This user belongs to the `sudo` and `user42` groups.

## Instructions

### Start the virtual machine

Open VirtualBox and start the Born2beRoot virtual machine.

At startup, Debian asks for the LUKS encryption passphrase before mounting the encrypted system volume.

Log in locally with the `lmezzaba` user or root user.

### Connect through SSH

SSH is available on port `4242`.

From the host machine:

```bash
ssh -p 4242 lmezzaba@localhost
```

Root login through SSH is disabled:

```bash
ssh -p 4242 root@localhost
```

This command must fail with `Permission denied`.

### Monitoring script

The monitoring script is located at:

```text
/usr/local/bin/monitoring.sh
```

It can be executed manually with:

```bash
sudo /usr/local/bin/monitoring.sh
```

It is also started automatically by cron:

```cron
@reboot /usr/local/bin/monitoring.sh
*/10 * * * * /usr/local/bin/monitoring.sh
```

The first rule runs it once at system startup. The second rule runs it every ten minutes.

## Technical Choices

### Operating system

Debian GNU/Linux 13 was chosen because it is stable, widely documented, and suitable for learning Linux system administration. It provides a minimal installation and integrates well with tools required by this project, such as AppArmor, UFW, OpenSSH, PAM, cron, and LVM.

No graphical environment, X.org, Wayland, or desktop environment was installed.

### Storage layout

The disk is organized as follows:

```text
/dev/sda1                  ext4     /boot
/dev/sda2                  LUKS2 encrypted container
└── /dev/mapper/sda2_crypt LVM physical volume
    ├── LVMGroup-root      /
    ├── LVMGroup-swap      [SWAP]
    ├── LVMGroup-home      /home
    ├── LVMGroup-var       /var
    ├── LVMGroup-srv       /srv
    ├── LVMGroup-tmp       /tmp
    └── LVMGroup-var-log   /var/log
```

`/boot` must remain outside the encrypted container because the bootloader needs access to the kernel and initial ramdisk before the encrypted volume can be unlocked.

The rest of the system is stored inside a LUKS encrypted container. LVM is used inside that encrypted container to create separate logical volumes for important directories.

This separation improves organization and limits the impact of a directory filling the disk. For example, excessive logs in `/var/log` cannot directly fill the root filesystem.

### Security policy

AppArmor is enabled and started automatically at boot. It is a mandatory access control system that can restrict what protected applications are allowed to access.

UFW is enabled with a default-deny policy for incoming connections. Only TCP port `4242` is allowed for SSH.

SSH is configured to listen on port `4242`. Direct SSH access as root is disabled with:

```text
PermitRootLogin no
```

### Password policy

Password expiration is configured with:

```text
PASS_MAX_DAYS 30
PASS_MIN_DAYS 2
PASS_WARN_AGE 7
```

Passwords must:

* contain at least 10 characters;
* contain an uppercase letter;
* contain a lowercase letter;
* contain a digit;
* not contain the user name;
* not contain more than three consecutive identical characters.

The policy is enforced through PAM and `pam_pwquality`.

### Sudo configuration

The `lmezzaba` user is part of the `sudo` group.

Sudo is configured to:

* allow only three incorrect password attempts;
* display a custom message after an incorrect password;
* log commands, input, and output;
* store logs in `/var/log/sudo/`;
* require a terminal with `requiretty`;
* use a restricted secure path.

The main sudo log file is:

```text
/var/log/sudo/sudo.log
```

### Services installed

The server uses only the services required for the mandatory part:

* `openssh-server` for remote SSH access;
* `ufw` for firewall rules;
* `apparmor` for mandatory access control;
* `cron` for scheduled tasks;
* `sudo` for controlled administrative commands;
* `libpam-pwquality` for password-quality rules.

## Comparisons

### Debian vs Rocky Linux

Debian and Rocky Linux are both stable Linux distributions suitable for servers.

Debian uses the APT package manager and packages are commonly installed with `apt`. It has a large community, extensive documentation, and is often easier for beginners.

Rocky Linux is compatible with Red Hat Enterprise Linux. It uses RPM packages and the DNF package manager. It is common in enterprise environments where RHEL compatibility is important.

For this project, Debian was chosen because it is easier to configure for a first system administration project and uses AppArmor by default.

### AppArmor vs SELinux

AppArmor and SELinux are both mandatory access control systems.

AppArmor uses path-based profiles. A profile specifies which files, capabilities, and resources a program can access. Its configuration is usually easier to read and manage for beginners.

SELinux uses labels attached to files, processes, ports, and other objects. Policies are generally more detailed and powerful, but are also more complex to understand and configure.

Debian uses AppArmor for this project, while Rocky Linux requires SELinux.

### UFW vs firewalld

UFW and firewalld are both firewall management tools.

UFW is a simple command-line interface designed to manage firewall rules easily. It is commonly used on Debian and Ubuntu systems.

Firewalld manages rules dynamically through zones and services. It is commonly used on Rocky Linux and other Red Hat-based distributions.

For this project, UFW is used to deny incoming traffic by default and allow only SSH traffic on TCP port `4242`.

### VirtualBox vs UTM

VirtualBox and UTM are virtualization applications.

VirtualBox is cross-platform and works on Linux, Windows, and macOS. It provides a graphical interface for configuring virtual machines, virtual disks, networking, and port forwarding.

UTM is mainly used on macOS and is especially useful on Apple Silicon computers. It is based on QEMU and can emulate or virtualize different CPU architectures.

VirtualBox was chosen because it is available on the host system and supports the required VM, virtual disk, NAT networking, and SSH port forwarding configuration.

## Useful Commands

### Check the disk layout

```bash
lsblk -f
pvs
vgs
lvs
```

### Check SSH

```bash
systemctl status ssh
ss -tulnp | grep 4242
```

### Check firewall

```bash
sudo ufw status numbered
```

### Check AppArmor

```bash
sudo aa-status
systemctl is-enabled apparmor
```

### Check password aging

```bash
chage -l lmezzaba
chage -l root
```

### Check sudo configuration

```bash
sudo visudo -c
sudo cat /var/log/sudo/sudo.log
```

### Check cron jobs

```bash
sudo crontab -l
systemctl status cron
```

## Resources

* 42 Born2beRoot subject.
* Debian documentation.
* Debian manual pages: `man apt`, `man ssh`, `man sshd_config`, `man sudoers`, `man ufw`, `man cron`, `man crontab`, `man wall`, `man lvm`, and `man cryptsetup`.
* OpenSSH documentation.
* UFW documentation.
* AppArmor documentation.
* PAM and `pam_pwquality` documentation.
* VirtualBox documentation.

## AI Usage

AI was used as a learning and documentation assistant during this project.

It was used to:

* explain Linux concepts such as LUKS, LVM, SSH, UFW, AppArmor, PAM, sudo, cron, terminals, and `wall`;
* help interpret command output and verify configuration choices;
* clarify the meaning of configuration directives;



