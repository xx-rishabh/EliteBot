from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1817429
    API_HASH = "0032867a279f1803b6de52c3f829b5b6"
    # the name to display in your alive message
    ALIVE_NAME = "𝚁𝙸𝚂𝙷𝙰𝙱𝙷"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://meulqdou:5nqRNNtiBQGQaiyAMn6bzAPkxEkWznDa@silly.db.elephantsql.com/meulqdou"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHEBu2_9BKw-c2xr2An8aHx_3Q77V4X3ClXPd7tW33yIpWPuPgcy10MSwOj6tCfTibdJT-9c7qW7fcZkT8iig98owFBxlTPvF712suNUH-1-CHp5ZRSCcXEMs4ZK5WtJa5vCI9x9yjWFA6t-TB1ffJgV3lXo2uJmMkfb45D_pFeF3HTgJ7CDssCN-baznzAxtQ4zJJWh62UUyPTrSaKEpVbZA5vu3Le8i9kwSQsNb_x6JKDfT7Ml2nLgn60dAI0u4buB8AYr_hadhi36LIezb1PzxwX7QYPdECAYlm-X49naCJY2i1-oEGXXayqJ6dT0zOnsgT5laHX5jT47R9B3GJTPovo="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5908818425:AAEPQ2JNwrxG5T4KYbsIKI92YtljbF3bQZE"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001576068466
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO =  "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
