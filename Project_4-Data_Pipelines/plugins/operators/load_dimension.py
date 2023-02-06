from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = '', 
                 table = '',
                 sql_query = '',
                 truncate_table = '',
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_query = sql_query
        self.truncate_table = truncate_table

    def execute(self, context):
        self.log.info('Connect to Redshift')
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        
        if self.truncate_table:
            self.log.info(f'Truncating table {self.table} on Redshift')
            redshift.run(f'TRUNCATE TABLE {self.table}')
        
        self.log.info(f'Load data to table {self.table} on Redshift')
        redshift.run(self.sql_query)
        self.log.info(f'Finished loading table {self.table} on Redshift')