import requests
import re
import os
import glob
from guldcfg import GuldConfig, BLOCKTREE
cfg = GuldConfig

def get_interfaces_simple(iname=None, include_external=False):
    inames = []
    if iname:
        inames.append({
            'mac': netifaces.ifaddresses(iname)[netifaces.AF_LINK][0]['addr'],
            'ip': netifaces.ifaddresses(iname)[netifaces.AF_INET][0]['addr'],
            'ip6': netifaces.ifaddresses(iname)[netifaces.AF_INET6][0]['addr']
        })
    else:
        for i in INTERFACES:
            inames.append({
                'mac': netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'],
                'ip': netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'],
                'ip6': netifaces.ifaddresses(i)[netifaces.AF_INET6][0]['addr']
            })
    if include_external:
        xip = get_external_addr()
        if xip:
            inames.append({
                'ip': xip
            })
    return inames

def get_hosts(iname=None, include_external=True):
    hosts = ""
    ifs = get_interfaces_simple(iname, include_external)
    for i in ifs:
        if 'ip' in i:
            hosts = "%s%s\t%s\n" % (hosts, i['ip'], cfg.hostname)
        if 'ip6' in i:
            hosts = "%s%s\t%s\n" % (hosts, i['ip6'], cfg.hostname)
    return hosts

def get_external_addr():
    resp = requests.get('https://api.ipify.org')
    if resp.status_code == requests.codes.ok:
        return resp.text

def get(name=None):
    got = []
    with open('/etc/hosts', 'r') as f:
        for line in f.readlines():
            if (name is None and re.match('[\w.:]+\s+[\w.]+$', line)) or re.match('[\w.:]+\s+[\w.]*%s$' % name, line):
                # got.append(re.match('^[1234567890abcdef.:]*', line).group(0))
                got.append(line.strip())
    return got

def generate():
    allhosts = glob.glob(os.path.join(BLOCKTREE, '**', 'devices', '**', 'etc/device-hosts'))
    hostcont = ""
    for host in allhosts:
        with open(host, 'r') as h:
            hostcont = hostcont + h.read()
    hosts = open(os.path.join(BLOCKTREE, cfg.admin, 'devices', cfg.devicename, 'etc/hosts'), 'w')
    hosts.write(hostcont)
    hosts.close()
    return hostcont

def generate_device(include_external=True):
    hosts = get_hosts(include_external=include_external)
    with open(os.path.join(BLOCKTREE, cfg.admin, 'devices', cfg.devicename, 'etc/device-hosts'), 'w') as myhosts:
        myhosts.write(hosts)
        myhosts.close()
    return hosts

