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
    STRING_SESSION = "1BVtsOHEBuxQrlmg9ZvZElDkDe-dE-c3Y8nETWhpBPo_hVOugO64MY0W6CepOUc8VNtiFoO9z5RqEcSka0fR8R5ev3s-YAzG67eHCSds3iZobZbsWi3Yi_hHV46V_2cYBItnhKC5Lvn_kv_d9184pcJf02XVit675b8FY77CjkNKmtAJr9z6woPPKtb56hFlU_NKQh7Olvg9dfmUaKsAnhDcR-dbweQ5UPGB9w3y8B54-TNflHMptY_IW6J3qnLc1u6gXxWrsyrO7v9OD1tfZ15_VgKLdpkwNc4qEgHkxnIAUiOsVXezd_clPw1-evSxfSfL4p42eyVelxAOaNJwK_p-vkkdNJy4="
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
