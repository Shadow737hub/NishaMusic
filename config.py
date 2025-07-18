import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID","20536100"))
API_HASH = getenv("API_HASH","5e3694deb111a38fe4aba250eb37af6a")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN","7408662813:AAFVjRXCtR3xxzRqLo43MS6jB2Lrt07zCjU")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","LOKI")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "@vicasobot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , ".")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "LOKIASSISTANT")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1002501608775"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", "7952111348"))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/BUG-MUSIX/NishaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/L0KIlIl")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+m63eJ-Mc_jpjMzll")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION",  "1BVtsOKEBuz-PFyX3eMjRVBZh3qKnDeGYSGR4IQXJWXhGvB526KXSE0MBjKvG52xv92r-eS_IB_7yoWg1gSW3qcRXstoIhugbUQaecB1vlHM5-Ex__FpQqZNIPZeykEAeoeoLXbU8WxLVWLO_IeI44QjMh8Pk8XKuxrSevxmKE4juB3XiEAMhjcY5rUVr_0Ubg-uAqKqLpkPCU2rEuFOMWSB89AImEKACFbn-VKdyAH-HVaHu1enHAD7INzbm0_kGVSQFcJIhAtIhWx8VlY6o7SF3egYiT6ACNKw-3-kLE6_zQ4_qYweUgjO-VF-0pKuIdfrzA03o5o8OyRNcP_20aMoed_sGi1c=")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/33fbec85bcf06dccc7c25-d3a85fd8fe85a3aab4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/6a28372052c507342afd5-2266b394b39148041b.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/13afb9ee5c5da17930f1e.png"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/13afb9ee5c5da17930f1e.png"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
