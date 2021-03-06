import os.path

# CA hostname
# If you create your own server... change this line
# Note: the server certificate must be trusted in order to avoid
# further modifications to the client
ACME_SERVER = "letsencrypt-demo.org"
# Apache server root directory
SERVER_ROOT = "/etc/apache2/"
# Configuration file directory for letsencrypt
CONFIG_DIR = "/etc/letsencrypt/"
# Working directory for letsencrypt
WORK_DIR = "/var/lib/letsencrypt/"
# Directory where configuration backups are stored
BACKUP_DIR = os.path.join(WORK_DIR, "backups/")
# Replaces MODIFIED_FILES, directory where temp checkpoint is created
TEMP_CHECKPOINT_DIR = os.path.join(WORK_DIR, "temp_checkpoint/")
# Directory used before a permanent checkpoint is finalized
IN_PROGRESS_DIR = os.path.join(BACKUP_DIR, "IN_PROGRESS/")
# Directory where all certificates/keys are stored - used for easy revocation
CERT_KEY_BACKUP = os.path.join(WORK_DIR, "keys-certs/")
# Where all keys should be stored
KEY_DIR = os.path.join(SERVER_ROOT, "ssl/")
# Certificate storage
CERT_DIR = os.path.join(SERVER_ROOT, "certs/")

# Contains standard Apache SSL directives
OPTIONS_SSL_CONF = os.path.join(CONFIG_DIR, "options-ssl.conf")
# Let's Encrypt SSL vhost configuration extension
LE_VHOST_EXT = "-le-ssl.conf"
# Temporary file for challenge virtual hosts
APACHE_CHALLENGE_CONF = os.path.join(CONFIG_DIR, "le_dvsni_cert_challenge.conf")

# Byte size of S and Nonce
S_SIZE = 32
NONCE_SIZE = 16

# Key Sizes
RSA_KEY_SIZE = 2048

# bits of hashcash to generate
DIFFICULTY = 23

# Let's Encrypt cert and chain files
CERT_PATH = CERT_DIR + "cert-letsencrypt.pem"
CHAIN_PATH = CERT_DIR + "chain-letsencrypt.pem"

# Invalid Extension
INVALID_EXT = ".acme.invalid"

# Challenge Preferences Dict for currently supported challenges
CHALLENGE_PREFERENCES = ["dvsni", "recoveryToken"]

# Mutually Exclusive Challenges - only solve 1
EXCLUSIVE_CHALLENGES = [frozenset(["dvsni", "simpleHttps"])]

# These are challenges that must be solved by a Configurator object
CONFIG_CHALLENGES = frozenset(["dvsni", "simpleHttps"])

# Rewrite rule arguments used for redirections to https vhost
REWRITE_HTTPS_ARGS = [
    "^.*$", "https://%{SERVER_NAME}%{REQUEST_URI}", "[L,R=permanent]"]
