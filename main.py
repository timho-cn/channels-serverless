from manager import ManagerFactory
'''
Parse partner_id argument
Use partner_id to decide which object to invoke
'''


def lambda_handler(event, context):
    partner_id = event['partner_id']
    manager = ManagerFactory(partner_id)
    manager.run()
