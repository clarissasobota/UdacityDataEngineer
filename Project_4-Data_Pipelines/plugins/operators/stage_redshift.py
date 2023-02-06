from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    copy_sql = """
            COPY {}
            FROM '{}'
            ACCESS_KEY_ID '{}'
            SECRET_ACCESS_KEY '{}'
            REGION '{}'
            FORMAT AS JSON '{}'
            
    """
    @apply_defaults
    def __init__(self,
                 redshift_connection_id = '',
                 aws_credentials_id = '',
                 table = '',
                 s3_bucket = '',
                 s3_key = '',
                 region = '',
                 file_format = ''
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_connection_id = redshift_connection_id,
        self.aws_credentials_id = aws_credentials_id,
        self.table = table,
        self.s3_bucket = s3_bucket,
        self.s3_key = s3_key,
        self.region = region,
        self.file_format = file_format
        *args, **kwargs):

    def execute(self, context):
        self.log.info('Get AWS credentials')
        aws_hook = AwsHook(self.aws_credential_id)
        credentials = aws_hook.get_credentials()
        
        self.log.info('Connect to Redshift')
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        
        self.log.info('Purge data from table')
        redshift.run('DELETE FROM {}'.format(self.table))
        
        self.log.info('Copy data from S3 to Redshift')
        s3_path = "s3://{}/{}".format(self.s3_bucket, self.s3_key)
        
        self.log.info('Run copy query')
        copy_query = StageToRedshiftOperator.copy_sql.format(
            self.table_name,
            s3_path,
            credentials.access_key,
            credentials.secret_key,
            self.region,
            'auto'
        )
        redshift.run(copy_query)
        
        self.log.info(f'{self.table_name} has been staged')




