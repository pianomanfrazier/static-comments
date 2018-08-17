# Static Comments

A comment system for static sites.

There are already several solutions available, so why write another comment engine?

- It looked fun to make
- I want the comments to be stored in the repo and available at site generation time

## API

### Protected API 

|   Method   |    URL     |  query params   |  data                           | returns               |
|------------|------------|-----------------|---------------------------------|---------------------  |
|  GET       | /          | baseURL, slug, active, approved   |               |  comments for the url |
|  GET       | /count     | baseURL         | count for comments for each slug at a baseURL | `{ slug : int, ... }` |
|  PUT       | /commentID |                 | list of commentIDs to approve   |  200                  |
|  PUT       | /commentID |                 | list of commentIDs to unapprove |  200                  |
|  PUT       | /commentID |                 | list of commentIDs to deactivate|  200                  |
|  DELETE    | /          |                 | list of commentIDs to delete    |  200                  |
|            |            |                 |                                 |                       |

## Public API

|   Method   |    URL     | query params |  data   | returns    |
|------------|------------|--------------|---------|------------|
|  POST      |  /comment  |              | `{ comment: string, email: string, honeypot: string, url: string }` | 201 |

## Data Model

```js
{
  id: string,
  comment: string,
  email: md5 hash,
  approved: bool,
  active: bool,
  url: string
}
```

## Config

```ini
acceptURL: ['localhost', 'https://www.website.com',...]
security_key: 'XXXXXXXX'
```

