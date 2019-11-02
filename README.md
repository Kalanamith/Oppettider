# Opening hours of restaurants

### Docker setup
```bash
docker build -f ./docker/dev/Dockerfile -t oh . \
&&  docker run -p 5000:5000 --rm -it oh
```
### Deployment installation
*  `pip install --no-cache-dir -e.`
### Test installation
* `pip install --no-cache-dir -e.["tests"]`
