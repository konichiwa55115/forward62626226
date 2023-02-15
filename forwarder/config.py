from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5881051237:AAGS8hiOBdxPxgiYu9GOQn07uI6qBrft6f0"  # Your bot API key
    OWNER_ID = 1227193881  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [1227193881, 6297395845]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001866642464]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
