import re

r = re.compile(r'[0-9a-zA-z\_\.]{0,20}@[0-9a-zA-z]{0,10}\.[a-z]{0,5}')
def is_valid_email(addr):
    if r.match(addr):
        return True
    else:
        return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')