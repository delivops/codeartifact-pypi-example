# Deploy locally

Make sure you have installed the required dependencies
```
pip install wheel twine build
```

Authenticate with CodeArtifact
```
export CODEARTIFACT_DOMAIN=delivops
export CODEARTIFACT_OWNER=556196322339
export CODEARTIFACT_REPOSITORY=pypi-internal
export CODEARTIFACT_REGION=us-east-1

aws codeartifact login --tool twine --repository $CODEARTIFACT_REPOSITORY --domain delivops --domain-owner $CODEARTIFACT_OWNER --region $CODEARTIFACT_REGION
token=$(aws codeartifact get-authorization-token --domain $CODEARTIFACT_DOMAIN --query authorizationToken --output text)
```

Build and upload your library (expose the desired version as env variable for setup.py)
```
cd my_lib_1

VERSION=1.0.0rc0 python3 -m build

twine upload --repository-url https://$CODEARTIFACT_DOMAIN-$CODEARTIFACT_OWNER.d.codeartifact.$CODEARTIFACT_REGION.amazonaws.com/pypi/$CODEARTIFACT_REPOSITORY/ --username aws --password $token --skip-existing dist/*
```

# Install it locally

```
export CODEARTIFACT_DOMAIN=delivops
export CODEARTIFACT_OWNER=556196322339
export CODEARTIFACT_REPOSITORY=pypi-internal
export CODEARTIFACT_REGION=us-east-1

aws codeartifact login --tool pip --repository $CODEARTIFACT_REPOSITORY --domain delivops --domain-owner $CODEARTIFACT_OWNER --region $CODEARTIFACT_REGION

pip install my-lib-1
```
