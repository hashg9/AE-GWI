import io
import boto3
import configparser


class Config():
    def __init__(self):
        client = boto3.client('ssm')
        ssm_value = client.get_parameter(Name="/qa/automation/creds", WithDecryption=True)
        buf = io.StringIO(ssm_value['Parameter']['Value'])
        parser = configparser.ConfigParser()
        print("printing sections before ", parser.sections())
        parser.read_file(buf)
        print("printing sections after ", parser.sections())
        self.config = dict(parser.items('OmniLogin_QA'))
        for section in parser.sections():
            self.config[section] = dict(parser.items(section))

    def get_config(self):
        return self.config
