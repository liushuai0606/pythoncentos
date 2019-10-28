import os
import re

ifconfig_result = os.popen('ifconfig ' + 'ens33').read()

ip = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
netmask = re.findall(r'netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
broadcast = re.findall(r'broadcast (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
mac = re.findall(r'ether ([A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2}\:[A-Fa-f0-9]{2})',
                 ifconfig_result)[0]

ip_split = ip.split('.')

ip_split[3] = '1'

gw_ip = '.'.join(ip_split)

format_str1 = '{0:<10} : {1:<50}'

print('=' * 80)
print(format_str1.format('ipv4_add', ip))
print(format_str1.format('netmask', netmask))
print(format_str1.format('broadcase', broadcast))
print(format_str1.format('mac_addr', mac))
print('=' * 80)

ping = os.popen('ping ' + gw_ip + ' -c 4').read()

ping_result = re.findall(r'\d\s+packets\s+transmitted,\s+(\d)\s+received', ping)[0]

print('假设网关IP地址最后一位为1，因此\n')

if ping_result:
    print('网关: {0} ;  {1} 次可达'.format(gw_ip, ping_result))
else:
    print('{0} 网关不可达'.format(gw_ip))
print('=' * 80)
