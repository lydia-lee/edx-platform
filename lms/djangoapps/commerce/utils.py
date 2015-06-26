from collections import OrderedDict
import logging


log = logging.getLogger(__name__)


def audit_log(name, **kwargs):
    """DRY helper used to emit an INFO-level log message.

    Messages logged with this function are used to construct an audit trail. Log messages
    should be emitted immediately after the event they correspond to has occurred and, if
    applicable, after the database has been updated. These log messages use a verbose
    key-value pair syntax to make it easier to extract fields when parsing the application's
    logs.

    This function is variadic, accepting a variable number of keyword arguments.

    Arguments:
        name (str): The name of the message to log. For example, 'payment_received'.

    Keyword Arguments:
        Indefinite. Keyword arguments are strung together as comma-separated key-value
        pairs alphabetically ordered by key in the resulting log message.

    Returns:
        None
    """
    d = OrderedDict(sorted(kwargs.items(), key=lambda i: i[0]))

    # Joins keys and values from the sorted dictionary above with an "=", wraps each value
    # in quotes, and separates each pair with a comma and a space.
    payload = u', '.join(['{k}="{v}"'.format(k=k, v=v) for k, v in d.iteritems()])
    message = u'{name}: {payload}'.format(name=name, payload=payload)

    log.info(message)
