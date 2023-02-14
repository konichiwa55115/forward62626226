from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5881051237:AAH5Qqr32s1Rq7FOLJPoTKJd9OU0tQj17gc"  # Your bot API key
    OWNER_ID = 1234567890  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [5763484201]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001742976120]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
