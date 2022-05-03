

from models import *




jv1 = JobVar(
    var_id=1,
    display_name='Interface',
    slug='interface',
    description='switchport interface',
    input_type='text'
)

jv2 = JobVar(
    var_id=2,
    display_name='Description',
    slug='description',
    description='Interface description value. Use format: hn=xxxapp01n;if=fixme;tg=mgmt1,reserved;jr=NET-1111',
    input_type='text'
)

jv3 = JobVar(
    var_id=3,
    display_name='interface',
    slug='interface',
    description='switchport interface',
    input_type='text'
)


r1 = Role(
    role_id = 1,
    display_name = 'interfaces',
    description = 'this is the interfaces role',
    slug = 'interfaces'
)