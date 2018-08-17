# Static Comments

A comment system for static sites.

There are already several solutions available, so why write another comment engine?

- It looked fun to make
- I want the comments to be stored in the repo and available at site generation time

## API

### Protected API 

|   Method   |    URL     |  query params   |  data                           | returns               |
|------------|------------|-----------------|---------------------------------|---------------------  |
|  GET       | /comments  | baseURL, slug, active, approved   |               |  comments for the url |
|  GET       | /comments/count | baseURL, slug, active, approved |            |        comment count  |
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

