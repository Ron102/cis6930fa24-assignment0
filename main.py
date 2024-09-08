import requests
import json
import argparse
import sys


def api_call(page=None, file=None):
    if page is not None:
        response = requests.get(f'https://api.fbi.gov/wanted/v1/list', params={'page': page})
        data = json.loads(response.content)
    elif file is not None:
        with open(file,'r',encoding='utf-8') as f:
            data = json.load(f)
    main(data)

    

def main(data):
    i=0
    for item in data['items']:
        if i>=20: break
        title = item.get('title', 'N/A')
        subjects = item.get('subjects', [])
        field_offices = item.get('field_offices', [])
        print(f"{title}þ{','.join(subjects) if subjects else ''}þ{','.join(field_offices) if field_offices else ''}")
        i+=1

        

def parse_func():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="An Example API file.")
    parser.add_argument("--page", type=int, required=False, help="An Example API file.")
     
    args = parser.parse_args()
    if args.page:
        api_call(page=args.page)
    elif args.file:
        api_call(file=args.file)
    else:
        parser.print_help(sys.stderr)


parse_func()

