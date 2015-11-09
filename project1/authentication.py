"""This module provides functions for authenticating users."""

def login(username, password):
    """Log the user in."""
    try:
        return [username, password] in users
    except IOError:
        print "I can't authentication you."
        return False