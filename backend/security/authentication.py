from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from security.models import Token


class UserTokenAuthentication(BaseAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    messages = {
        "no_credentials": "Invalid token header. No credentials provided.",
        "invalid_format": "Invalid token header. Token string should not contain spaces.",
        "invalid_token": "Invalid token.",
    }

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b"token":
            raise AuthenticationFailed(self.messages["no_credentials"])

        if len(auth) == 1:
            raise AuthenticationFailed(self.messages["no_credentials"])

        elif len(auth) > 2:
            raise AuthenticationFailed(self.messages["invalid_format"])

        return self.authenticate_credentials(auth[1].decode("utf-8"))

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed(self.messages["invalid_token"])

        return token.user, token

    def authenticate_header(self, request):
        return "Token"
