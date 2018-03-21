Author = 'Liu Lei'
#temp account data,only saves the data in memory
user_data={
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
def run():
    '''
    this function will be called right a way when the program started
    :return:
    '''
    acc_data=auth.acc_login(user_data,access_logger)