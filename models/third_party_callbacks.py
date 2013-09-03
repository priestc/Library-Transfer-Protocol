from giotto import get_config
from models import Library, StorageEngine
from giotto_google.models import get_google_flow

def dropbox_api_callback(user, access_token):
    """
    Handles the request that the user makes given by the dropbox API as part of
    the oauth process. This is the callback used in oauth1.
    """
    session = get_config('db_session')
    library = Library.get(username=user.username)
    at = {'key': access_token.key, 'secret': access_token.secret}
    engine = StorageEngine(name="dropbox", connection_data=at, library=library)
    session.add(engine)
    session.commit()

    return "/manage/%s" % user.username

def google_api_callback(user, credentials):
    """
    After authenticating with the Google API Auth server, it redirects the user
    back to this program, where `code` is exchanged for an auth token, and
    then stored.
    """
    session = get_config('db_session')
    library = Library.get(username=user.username)
    engine = StorageEngine(name="googledrive", connection_data=credentials, library=library)
    session.add(engine)
    session.commit()

    return '/manage/%s' % user.username