from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id, 
                 tables,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables

    def execute(self, context):
        self.log.info('Connect to Redshift')
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        

        self.log.info('Start running tests')
        for table in self.tables:
            self.log.info(f'Tests for table: {self.table}')
            records = redshift_hook.get_records(f'SELECT COUNT(*) FROM {self.table}')
            if len(records) <1 or len(records[0] < 1:
                raise ValueError(f'Data quality check failed: {self.table} returned no records.')  
            num_records = records[0][0]
            if num_records < 1:
                raise ValueError(f'Data quality check failed: {self.table} has 0 rows.')
            self.log.info(f'Data quality checks on table {self.table} have passed with {num_records}')