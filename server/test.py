import requests
import sys
import json

# TODO
# set environment to test and use clean sqlite3 database

# set the header based on the username and password
headers = {
    'Authorization': 'Basic YWRtaW46U2VjcmV0MUA='
}

data = {
    "comment"   :
"""# Howdy

This is a long comment.

## Heading 2

- it
- has lists
- and
- more items

```
print('and code too')
```
    """,
    "name"      : "jim bob",
    "email"     : "r@r.com",
    "honeypot"  : "", # leave empty
    "url"       : "http://localhost:5000/post/everything-is-awesome"
}

BASEURL = 'http://localhost:5000'
API     = '/api/v1'

def post_comment():
    url = BASEURL + API + '/comments'
    print("Making POST request to {}".format(url))
    r = requests.post(url, json=data)
    print(r.text)
    try:
        new_id = json.loads(r.text)['id']
        return r.status_code, new_id
    except:
        return r.status_code, -1

def get_all_comments():
    url = BASEURL + API + '/comments'
    print("Making GET request to {}".format(url))
    r = requests.get(url, headers=headers)
    print(r.text)
    return r.status_code

def get_comment_by_id(id):
    url = BASEURL + API + '/comments' + '/' + str(id)
    print("Making GET request to {}".format(url))
    r = requests.get(url, headers=headers)
    print(r.text)
    return r.status_code

def update_comment(id):
    data['email'] = 'new@email.com'
    url = BASEURL + API + '/comments' + '/' + str(id)
    print("Making PUT request to {}".format(url))
    r = requests.put(url, json=data, headers=headers)
    print(r.text)
    return r.status_code

def delete_comment(id):
    url = BASEURL + API + '/comments' + '/' + str(id)
    print("Making DELETE request to {}".format(url))
    r = requests.delete(url, headers=headers)
    print(r.text)
    return r.status_code

def clean(s, e):
    for i in range(s,e+1):
        delete_comment(i)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("please supply command line params\nexample: test.py <clean 1 5 | test>")
    if sys.argv[1] == 'clean':
        if len(sys.argv) < 4:
            sys.exit("not enough params to clean\nspecify start and end ids")
        clean(int(sys.argv[2]), int(sys.argv[3]))
        sys.exit()
    elif sys.argv[1] == 'test':
        print("-------------------------")
        print("----- RUNNING TESTS -----")
        print("-------------------------")
        status, id = post_comment()
        assert(status == 201)
        assert(get_all_comments() == 200)
        assert(get_comment_by_id(id) == 200)
        assert(update_comment(id) == 200)
        assert(delete_comment(id) == 200)

        assert(delete_comment(id) == 404)
        assert(get_comment_by_id(id) == 404)
        assert(update_comment(id) == 404)
        print("-------------------------")
        print("----- TESTS SUCCESS -----")
        print("-------------------------")
