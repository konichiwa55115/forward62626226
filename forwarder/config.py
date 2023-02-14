from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5936802228:AAFwW7cZlF8waTYTyVe8m3nUYhJg5EF9Eso"  # Your bot API key
    OWNER_ID = 1227193881  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [1227193881]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001739160183]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
