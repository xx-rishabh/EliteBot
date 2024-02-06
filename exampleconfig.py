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
    STRING_SESSION = "1BVtsOHEBuyF-cnWimtl8f4E64sjEoArPdH8WVme38GPadLhGRZFtC-be8Tm4ZTVY046J4xhbQya3ZRkS2IAzbAWwNuJHrLojm2Hq8a5qjuwQbBRvxYR5qsO3D4XT-0Qg-IIOWCEcTAfqUoO3oa-xcN5uQ8f46ayhbLdYxHeOq5FfIPwn40SDSKvPq94nqe4bB4R-FHzRwWduHnEIE4McNJsh8V_Ql6Rh4-yKZ8p-Cwew-nhDxP1urZa8gjIbqUe5iDrjUJaM7tN2QB6fMET5tjowApplZ_vbwkjDJQX_TVz7Gz_wOtXIZWZDwv2ojarFQXjr3A0dGCSHgZtTIXYfudEFv3TrpGE="
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
