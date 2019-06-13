is_aws_server = False
if is_aws_server:
    EMBEDDING_MODEL_PATH = '/pretrain_files/5_million_sentences'
    BIGRAMMER_PATH = '/pretrain_files/5_million_bigrammer.pickle.pickle'
    TRIGRAMMER_PATH = '/pretrain_files/5_million_trigrammer.pickle'
else:
    EMBEDDING_MODEL_PATH = 'D:/UnFound/Datesets/Word2Vec/models/5_million_sentences'
    BIGRAMMER_PATH = 'D:/UnFound/Datesets/Word2Vec/Unfound_trained_vectiors/5_million_bigrammer.pickle.pickle'
    TRIGRAMMER_PATH = 'D:/UnFound/Datesets/Word2Vec/Unfound_trained_vectiors/5_million_trigrammer.pickle'

EXTRACTION_SERVER = "http://172.16.60.38:8080"            # local server ip
# EXTRACTION_SERVER = "http://13.232.215.32:8080"         # dev server ip
ELMO_SERVER = "http://13.233.231.175:8080"                # dev elmo service
# EXTRACTION_SERVER = "http://13.127.90.101:8080"             # prod server ip
# ELMO_SERVICE = 'http://13.126.103.91:8080/elmo/embedding'   # prod elmo

# Extraction Service Auth credentials
EXTRACTION_SERVER_USERNAME = 'alpha'
EXTRACTION_SERVER_PASSWORD = 'unfound'

EXTRACTION_SERVICE_AUTH = (EXTRACTION_SERVER_USERNAME, EXTRACTION_SERVER_PASSWORD)


# ranking
DEFAULT_RANK = 0.1
OVERLAP_WEIGHTAGE = 0.5
COSINE_WEIGHTAGE = 0.5

# Priority Filtering
ALPHA = 0.5
BETA = 0.5

# Vectorization
EMBEDDING_LENGTH = 300

# Number of Suggestions
TOP_N = 1
DIVERSIFY = False
num_url = 100
