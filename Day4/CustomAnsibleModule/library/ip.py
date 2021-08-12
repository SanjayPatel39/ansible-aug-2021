
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'TekTutor'}

DOCUMENTATION = '''
---
module: ip  
version_added: 2.9 
short_description: Just returns IP Address of the ansible node 
description:
   - On success, return IP Address of the Ansible node 
'''

from ansible.module_utils.basic import AnsibleModule
import socket

def getIP():
    return socket.gethostbyname(socket.gethostname()) 

def main():
    module = AnsibleModule(
        argument_spec=dict(
            greeting_msg=dict(type='str')
        )
    )

    result = dict(
        output= getIP( )
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
