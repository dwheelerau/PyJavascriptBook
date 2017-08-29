import requests

OECD_ROOT_URL = 'http://stats.oecd.org/sdmx-json/data'

def make_oecd_req(dsname, dimen, params=None,
                  root_dir=OECD_ROOT_URL):

    if not params:
        params = {}

    dim_args = ['+'.join(d) for d in dimen]
    dim_str = '.'.join(dim_args)

    url = root_dir + '/' + dsname + '/' + dim_str + '/all'
    print('Request URL: ' + url)
    return requests.get(url, params=params)

response = make_oecd_req('QNA',
                         (('USA', 'AUS'),('GDP', 'B1_GE'),('CUR', 'VOBARSA'), ('Q')),
                         {'startTime':'2009-Q1', 'endTime':'2010-Q1'})
