# GOOGLE APP ENGINE MAIL API

# Setup

```
# install Google Cloud Storage library
pip install GoogleAppEngineCloudStorageClient -t lib

# add config.py file
authkey = "[AUTH_KEY]"

# deploy
gcloud app deploy
```

# API

## Request
#### Request URL
https://email-dot-[PROJ_ID].appspot.com/api

#### Request header
apikey: [AUTH_KEY]

#### Request body
```
{
	"from": "[SENDER_NAME]",
	"to": "[RECEIVER1_NAME] <receiver1@example.com>; [RECEIVER2_NAME] <receiver2@example.com>",
	"subject": "[SUBJECT]",
	"body_header": "[BODY_HEADER]",
	"body_footer": "[BODY_FOOTER]",
	"img_list": ["/[PROJECT_ID]/[PATH_TO_IMG1]", "/[PROJECT_ID]/[PATH_TO_IMG2]""],
	"attach_list": ["/[PROJECT_ID]/[PATH_TO_FILE1]", "/[PROJECT_ID]/[PATH_TO_FILE2]"]
}
```

## Response

#### Response status
```
200: "OK"
400: "Bad Request"
401: "Unauthorized"
```

## Email
#### Email subject
[SUBJECT]

#### Email body
```
[BODY_HEADER]
[image1]
[image2]
[BODY_FOOTER]
```

#### Email attach file
[file1], [file2], [image1], [image2]
