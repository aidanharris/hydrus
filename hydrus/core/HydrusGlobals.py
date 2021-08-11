import collections
import threading

controller = None
client_controller = None
server_controller = None
test_controller = None
view_shutdown = False
model_shutdown = False

server_action = 'start'

no_daemons = False
db_journal_mode = 'WAL'
no_db_temp_files = False

boot_debug = False

db_cache_size = 200
db_transaction_commit_period = 30

# if this is set to 1, transactions are not immediately synced to the journal so multiple can be undone following a power-loss
# if set to 2, all transactions are synced, so once a new one starts you know the last one is on disk
# corruption cannot occur either way, but since we have multiple ATTACH dbs with diff journals, let's not mess around when power-cut during heavy file import or w/e
db_synchronous = 2

import_folders_running = False
export_folders_running = False

profile_mode = False

db_profile_min_job_time_ms = 16
callto_profile_min_job_time_ms = 5
server_profile_min_job_time_ms = 5
menu_profile_min_job_time_ms = 16
pubsub_profile_min_job_time_ms = 5
ui_timer_profile_min_job_time_ms = 5

query_planner_mode = False

query_planner_start_time = 0
query_planner_query_count = 0
profile_start_time = 0
profile_slow_count = 0
profile_fast_count = 0
profile_counter_lock = threading.Lock()

db_ui_hang_relief_mode = False
callto_report_mode = False
db_report_mode = False
file_report_mode = False
media_load_report_mode = False
gui_report_mode = False
shortcut_report_mode = False
cache_report_mode = False
subprocess_report_mode = False
subscription_report_mode = False
hover_window_report_mode = False
file_import_report_mode = False
phash_generation_report_mode = False
network_report_mode = False
pubsub_report_mode = False
daemon_report_mode = False
force_idle_mode = False
no_page_limit_mode = False
thumbnail_debug_mode = False
currently_uploading_pending = False

do_idle_shutdown_work = False
shutdown_complete = False
restart = False

twisted_is_broke = False

dirty_object_lock = threading.Lock()
client_busy = threading.Lock()
server_busy = threading.Lock()
