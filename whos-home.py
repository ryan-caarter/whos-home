from fritzconnection.lib.fritzhosts import FritzHosts

def whos_home(fh):
    hosts = fh.get_hosts_info()
    result = []
    for index, host in enumerate(hosts, start=1):
        status = 'active' if host['status'] else  '-'
        ip = host['ip'] if host['ip'] else '-'
        mac = host['mac'] if host['mac'] else '-'
        hn = host['name']
        if host['status']:
            result.append(host['name'])
            print(f'{index:>3}: {ip:<16} {hn:<28} {mac:<17}   {status}')

if __name__ == '__main__':
    password = 'Password69420'
    fh = FritzHosts(address='192.168.178.1', password=password)
    whos_home(fh)
