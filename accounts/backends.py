from django.contrib.auth.models import User
from django.db.models import Q

class CaseInsensitiveAuth:
    """
    Authenticate a user by via a case insensitive query which checks the
    combination of the inputted username and password
    """
    def authenticate(self, username_or_email=None, password=None):
        """
        Get an instance of User using the supplied username
        or email (case insensitive) and verify the password
        Then filter all users by searching for a match by username/ email.
        """
        users = User.objects.filter(Q(username__iexact=username_or_email) |
                                    Q(email__iexact=username_or_email))
        if not users:
            return None

        """
        Then get the first result of the query (the user).
        """
        user = users[0]
        """
        If the password is correct, return user object
        """
        if user.check_password(password):
            return user

        return None