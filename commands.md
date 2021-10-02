```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/cities' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Los Vegas",
  "timezone": "America/Los_Angeles"
}'
```

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/cities/' \
  -H 'accept: application/json'
```
