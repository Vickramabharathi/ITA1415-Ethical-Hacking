import ipaddress
IN_SCOPE = ["172.16.0.0/24", "10.10.5.0/25"]
EXCLUDED = ["172.16.0.128/26"] # production analyser network - never touch
def in_scope(ip):
"""Returns True only if ip is inside an in-scope block and outside every excluded block."""
addr = ipaddress.ip_address(ip)
# TODO 1: Return False if addr lies in any EXCLUDED network; otherwise return True
# if it lies in any IN_SCOPE network, and False if it lies in none of them
pass # replace this line with your code
for ip in ["172.16.0.10", "172.16.0.130", "172.16.0.200", "10.10.5.100", "10.10.5.200", "192.168.1.1"]:
print(f"{ip:15} {'IN SCOPE' if in_scope(ip) else 'OUT OF SCOPE'}")