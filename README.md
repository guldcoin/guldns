# guld name service (guldns)

__A decentralized replacement for DNS using the guld filesystem__

Each device on the guld network keeps a linux style `hosts` file, typically located at `/etc/hosts`. This is a python script for managing the `hosts` file.

### CLI

```
usage: gns [-h] [-n NAME] [-x] [-X] {get,get_hosts,gen_machine,gen}

positional arguments:
  {get,get_hosts,gen_machine,gen}

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  The full or top level name to use.
  -x, --include-external
                        Include external IP address as reported by ipify.
  -X, --exclude-external
                        Exclude external IP address.
```

