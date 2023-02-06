from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'udacity',
    'start_date': datetime(2022, 1, 8),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'email_on_retry': False,
    'max_active_runs': 1
}

dag = DAG('udac_example_dag',
          default_args = default_args,
          description = 'Load and transform data in Redshift with Airflow',
          schedule_interval = '0 * * * *'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id = 'Stage_events',
    dag = dag,
    redshift_connection_id = 'redshift',
    aws_credentials_id = 'aws_credentials',
    table = 'public.staging_events',
    s3_bucket = 'udacity-dend',
    s3_key = 'log_data',
    region = 'us-west-2',
    file_format = 'JSON',
    
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id = 'Stage_songs',
    dag = dag,
    redshift_connection_id = 'redshift',
    aws_credentials_id = 'aws_credentials',
    table = 'public.staging_songs',
    s3_bucket = 'udacity-dend',
    s3_key = 'song_data'
)

load_songplays_table = LoadFactOperator(
    task_id = 'Load_songplays_fact_table',
    dag = dag,
    redshift_connection_id = 'redshift',
    table = 'public.songplays',
    sql_query = SqlQueries.songplay_table_insert
)

load_user_dimension_table = LoadDimensionOperator(
    task_id = 'Load_user_dim_table',
    dag = dag,
    redshift_connection_id = 'redshift',
    table = 'public.users',
    sql_query = SqlQueries.user_table_insert,
    truncate_table = True
    
)

load_song_dimension_table = LoadDimensionOperator(
    task_id = 'Load_song_dim_table',
    dag = dag,
    redshift_connection_id = 'redshift',
    table = 'public.songs',
    sql_query = SqlQueries.song_table_insert,
    truncate_table = True
    
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id = 'Load_artist_dim_table',
    dag = dag,
    redshift_connection_id = 'redshift'
    table = 'public.artists', 
    sql_query = SqlQueries.artist_table_insert,
    truncate_table = True
)

load_time_dimension_table = LoadDimensionOperator(
    task_id = 'Load_time_dim_table',
    dag = dag,
    redshift_connection_id = 'redshift',
    table = 'public.time',
    sql_query = SqlQueries.time_table_insert,
    truncate_table = True
)

run_quality_checks = DataQualityOperator(
    task_id = 'Run_data_quality_checks',
    dag = dag,
    redshift_connection_id = 'redshift'
    tables = ['songplays', 'users', 'songs', 'artists', 'time']
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


# Diagram
start_operator >> [stage_events_to_redshift, stage_songs_to_redshift] >> load_songplays_table >> [load_user_dimension_table, load_song_dimension_table, load_artist_dimension_table, load_time_dimension_table] >> run_quality_checks >> end_operator


# The above is equivalent to the workflows below

#start_operator >> stage_events_to_redshift
#start_operator >> stage_songs_to_redshift

#stage_events_to_redshift >> load_songplays_table
#stage_songs_to_redshift >> load_songplays_table

#load_songplays_table >> load_user_dimension_table
#load_songplays_table >> load_song_dimension_table
#load_songplays_table >> load_artist_dimension_table
#load_songplays_table >> load_time_dimension_table

#load_user_dimension_table >> run_quality_checks
#load_song_dimension_table >> run_quality_checks
#load_artist_dimension_table >> run_quality_checks
#load_time_dimension_table >> run_quality_checks

#run_quality_checks >> end_operator