#Third Party Modules
'''
pip install modules_name
python -m pip show faker
'''

from faker import Faker

fake=Faker()
print(fake.name())
print(fake.name_nonbinary())
print(fake.email())




