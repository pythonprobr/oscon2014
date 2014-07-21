"""
A client with name and e-mail:

    >>> jack = Customer('John Robinson', 'jack@rob.org')
    >>> jack.full_email()
    'John Robinson <jack@rob.org>'

A client with blank e-mail:

    >>> joe = Customer('Joseph Blow', '')
    >>> joe.full_email()
    'Joseph Blow <>'

"""

class Customer:

    def __init__(self, name, email, fidelity=0):
        self.name = name
        self.email = email
        self.fidelity = fidelity

    def full_email(self):
        return '{name} <{email}>'.format(**vars(self))
