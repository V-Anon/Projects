# You can create more variables according to your project. The following are the basic variables that have been provided to you

DB_PATH = "/home/Assignment/Lead_Scoring_data_pipeline/"

DB_FILE_NAME = 'utils_output.db'

UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'

DATA_DIRECTORY = '/home/Assignment/Lead_Scoring_data_pipeline/data/'

INTERACTION_MAPPING = '/home/Assignment/Lead_Scoring_data_pipeline/mapping/interaction_mapping.csv'

INDEX_COLUMNS = [
    "created_date",
    "city_tier",
    "first_platform_c",
    "first_utm_medium_c",
    "first_utm_source_c",
    "total_leads_droppped",
    "referred_lead",
    "app_complete_flag",
]

LEADSCORING_CSV_PATH = f"{DATA_DIRECTORY}leadscoring.csv"
