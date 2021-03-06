# Static Comments

A comment system for static sites.

There are already several solutions available, so why write another comment engine?

- It looked fun to make
- I want the comments to be stored in the repo and available at site generation time

## Architecture Overview

`server/` contains the Flask server. `client/` contains the Vue admin client that is served at `/`.

### Flask

- SQL Alchemy
- Flask Migrate

### Vue

- [ElementUI](https://element.eleme.io)

## API

### Protected API 

|   Method   |    URL     |  query params   |  data                           | returns               |
|------------|------------|-----------------|---------------------------------|---------------------  |
|  GET       | /comments  | base_url, slug, active, approved   |               |  comments for the url |
|  GET       | /comments/count | base_url, slug, active, approved |            |        comment count  |
|  GET       | /comments/commentID |                 |                        |  the comment          |
|  PUT       | /comments/commentID |                 | update comment (ie approve) |  200             |
|  DELETE    | /comments/commentID |                 |                        |  200                  |

## Public API

|   Method   |    URL     | query params |  data   | returns    |
|------------|------------|--------------|---------|------------|
|  POST      |  /comments |              | `{ comment: string, email: string, honeypot: string, url: string }` | 201 |

## Data Model

```js
{
  id: string,
  comment: string,
  email: md5 hash,
  create_date: date,
  update_date: date,
  approved: bool,
  active: bool,
  base_url: string,
  stub_url: string
}
```

## Config

```ini
acceptURL: ['localhost', 'https://www.website.com',...]
security_key: 'XXXXXXXX'
```

