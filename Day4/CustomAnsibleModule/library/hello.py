
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'TekTutor'}

DOCUMENTATION = '''
---
module: hello 
version_added: 2.9 
short_description: Just returns a greeting message, given a string 
description:
   - A trivial test module, this module always returns Welcome to user_string on successful
options:
  greeting_msg:
    description:
      -  You may supply DevOps.
    type: str
'''

from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return "Welcome to " + msg + " !"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            greeting_msg=dict(type='str')
        )
    )

    result = dict(
        output= sayHello( module.params['greeting_msg'] )
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
