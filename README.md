# About role
Ansible role for automated install `docker-ce` on the instance.

# Using variables
| **Inventory**               | **Description**             |
| --------------------------- | --------------------------- |
| `url_script_docker` | URL-address the script for install `docker-ce`. (Default: `https://get.docker.com`) |
| `path_to_script_docker_install` | Path the script installing `docker-ce`. (Default: `/tmp/install_docker.sh`) |

# Example playbook
```yaml
---
- name: Start playbook
  hosts: all
  tasks:
    - name: Include ansible role "kotofeych.ansible_docker"
      include_role:
        name: kotofeych.ansible_docker
```


# Supported OS
Any OS that has a `systemd` service.

Tested on distributions:
- Ubuntu 18.04
- Centos 7

Enjoy it!


## License

BSD
